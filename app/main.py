from collections import defaultdict
import csv
import io
import json

from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.utils import get_openapi
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.extra import ExtraExtension
from markdown.extensions.toc import TocExtension
from app.api.v1.templates.MermaidExtension import MermaidExtension

from app.api.v1.label.endpoints import router as labels_documents_router
from app.api.v1.manifest.endpoints import router as manifest_router
from app.api.v1.pudo.endpoints import router as pudo_router
from app.api.v1.tracking.endpoints import router as tracking_router

from app.api.v1.label.webhooks import webhook_router as label_webhook_router
from app.api.v1.label.webhooks import webhook_subscription_router as label_webhook_subscription_router

from app.api.v1.tracking.webhooks import webhook_router as tracking_webhook_router
from app.api.v1.tracking.webhooks import webhook_subscription_router as tracking_webhook_subscription_router

servers = [
    {
        "url": "https://api.gluey.ai",
        "description": "Production"
    },
    {
        "url": "https://api-sandbox.gluey.ai",
        "description": "Sandbox / Test"
    }
]

github_base = "https://github.com/Gluey-AI/gluey-api-docs/tree/master/app/api/v1/"

app = FastAPI(
    title="Gluey API",
    description="API endpoints for Gluey"
)

app.include_router(labels_documents_router)
app.include_router(manifest_router)
app.include_router(tracking_router)
app.include_router(pudo_router)

app.include_router(label_webhook_router)
app.include_router(label_webhook_subscription_router)

app.include_router(tracking_webhook_router)
app.include_router(tracking_webhook_subscription_router)

templates = Jinja2Templates(directory="app/api/v1/templates")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.middleware("http")
async def add_gluey_server(request: Request, call_next):
    # header 'server' is removed in Uvicorn by flag --no-server-header
    response = await call_next(request)
    response.headers["server"] = "gluey"
        
    return response

def get_openapi_schema(openapi_title: str, openapi_desc:str, doc_path:str, routes: any, webhooks: any = None):
    contact = {
        "name": "Engineering",
        "url": f"{github_base}{doc_path}",
        "email": "engineering@gluey.ai"
    }

    openapi_schema = get_openapi(
        title=openapi_title,
        version="0.1.0",
        description=openapi_desc,
        servers=servers,
        contact=contact,
        routes=routes,
        webhooks=webhooks
    )

    return openapi_schema

milestone_icons = {
    "start": "circle-plus",
    "collection": "truck-ramp-box",
    "in_transit": "truck",
    "delivery": "flag-checkered",
    "post_delivery": "check-circle",
    "return_to_sender": "warehouse",
    "exception": "exclamation-circle",
    "return_centre": "undo",
    "admin": "user-cog",
    "customs": "hand",
}

csv_files = {
    "all_events": "./app/static/all_events.csv",
    "outbound": "./app/static/outbound.csv",
    "return": "./app/static/return.csv",
    "international": "./app/static/international.csv",
    "exceptions": "./app/static/exceptions.csv",
}

def read_csv_stream_for_json(file_like):
    data = []
    file_like.seek(0)
    reader = csv.DictReader(file_like)
    for row in reader:
        data.append({
            "milestone": row['milestone'],
            "code": row['code'],
            "sub_code": row['sub_code'] or "No Sub Event",
            "description": row['detailed_explanation']
        })
    return data

def read_csv_for_json(file_path: str):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append({
                "milestone": row['milestone'],
                "code": row['code'],
                "sub_code": row['sub_code'] or "No Sub Event",
                "description": row['detailed_explanation']
            })
    return data

def read_csv(file_path: str):
    data = defaultdict(lambda: defaultdict(dict))
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            milestone = row['milestone']
            code = row['code']
            sub_code = row['sub_code'] or "No Sub Event"
            explanation = row['detailed_explanation']
            data[milestone][code][sub_code] = explanation
    return data

def combine_csv_files_in_memory(primary_file: str, international_file: str, exception_file: str):
    output = io.StringIO()
    primary_reader = csv.reader(open(primary_file, 'r', newline='', encoding='utf-8'))
    international_reader = csv.reader(open(international_file, 'r', newline='', encoding='utf-8'))
    exception_reader = csv.reader(open(exception_file, 'r', newline='', encoding='utf-8'))
    combined_writer = csv.writer(output)

    header = next(primary_reader)
    combined_writer.writerow(header)

    for row in primary_reader:
        combined_writer.writerow(row)

    next(international_reader)
    next(exception_reader)

    for row in international_reader:
        combined_writer.writerow(row)

    for row in exception_reader:
        combined_writer.writerow(row)

    output.seek(0)
    return output

def __create_template(request: Request, markdown_file: str, title: str):
    with open(f"./app/api/v1/templates/markdown/{markdown_file}", "r") as md_file:
        md_content = md_file.read()
    html_content = markdown.markdown(md_content, extensions=[
        MermaidExtension(),
        CodeHiliteExtension(linenums=False, guess_lang=False, use_pygments=True, pygments_formatter="html", css_class="highlight"),
        ExtraExtension(),
        TocExtension(toc_depth="2-3")])
    
    return templates.TemplateResponse("markdown.html", {"request": request, "markdown_content": html_content, "title": "Getting Started"})

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def home(request: Request):
    return templates.TemplateResponse("getting_started.html", {"request": request, "title": "Getting Started"})

@app.get("/async-labels", response_class=HTMLResponse, include_in_schema=False)
async def async_labels(request: Request):
    return __create_template(request, "async_labels.md", "Generating Labels Asynchronously")

@app.get("/sync-labels", response_class=HTMLResponse, include_in_schema=False)
async def sync_labels(request: Request):
    return __create_template(request, "sync_labels.md", "Generating Labels Synchronously")

@app.get("/book", response_class=HTMLResponse, include_in_schema=False)
async def book(request: Request):
    return __create_template(request, "book.md", "Book Collections")

@app.get("/tracking", response_class=HTMLResponse, include_in_schema=False)
async def tracking(request: Request):
    return __create_template(request, "tracking.md", "Integrating Tracking From Gluey")

@app.get("/tracking-codes", response_class=HTMLResponse, include_in_schema=False)
async def get_event_codes(request: Request):
    all_data = {
        "all_events": read_csv(csv_files["all_events"]),
        "outbound": read_csv(csv_files["outbound"]),
        "return": read_csv(csv_files["return"]),
        "international": read_csv(csv_files["international"]),
        "exceptions": read_csv(csv_files["exceptions"]),
    }

    return templates.TemplateResponse("events.html", {"request": request, "data": all_data, "icons": milestone_icons})

@app.get("/json/{file_name}", response_class=JSONResponse, include_in_schema=False)
async def get_json(file_name: str):
    if file_name not in csv_files:
        return JSONResponse({"error": "File not found"}, status_code=404)

    if file_name == "outbound" or file_name == "return":
        primary_file = csv_files[file_name]
        international_file = csv_files["international"]
        exception_file = csv_files["exceptions"]
        
        combined_csv = combine_csv_files_in_memory(primary_file, international_file, exception_file)
        data = read_csv_stream_for_json(combined_csv)
        return JSONResponse(data)

    data = read_csv_for_json(csv_files[file_name])
    return JSONResponse(data)

@app.get("/csv/{file_name}", response_class=StreamingResponse, include_in_schema=False)
async def get_combined_csv(file_name: str):
    if file_name not in csv_files:
        return JSONResponse({"error": "File not found"}, status_code=404)
    
    primary_file = csv_files[file_name]
    international_file = csv_files["international"]
    exception_file = csv_files["exceptions"]
    
    combined_csv = combine_csv_files_in_memory(primary_file, international_file, exception_file)
    
    headers = {
        'Content-Disposition': f'attachment; filename={file_name}.csv'
    }
    return StreamingResponse(combined_csv, media_type='text/csv', headers=headers)

@app.get("/api-label", response_class=HTMLResponse, include_in_schema=False)
async def redoc(request: Request):
    return templates.TemplateResponse("redoc.html", {"request": request, "spec_url": "/openapi-label.json", "title": "Label Endpoints"})

@app.get("/api-manifest", response_class=HTMLResponse, include_in_schema=False)
async def redoc(request: Request):
    return templates.TemplateResponse("redoc.html", {"request": request, "spec_url": "/openapi-manifest.json", "title": "Manifest Endpoints"})

@app.get("/api-tracking", response_class=HTMLResponse, include_in_schema=False)
async def redoc(request: Request):
    return templates.TemplateResponse("redoc.html", {"request": request, "spec_url": "/openapi-tracking.json", "title": "Tracking Endpoints"})

@app.get("/api-pudo", response_class=HTMLResponse, include_in_schema=False)
async def redoc(request: Request):
    return templates.TemplateResponse("redoc.html", {"request": request, "spec_url": "/openapi-pudo.json", "title": "PUDO Endpoints"})

@app.get("/openapi-{schema_type}.json", include_in_schema=False)
async def gluey_openapi(schema_type: str):
    if schema_type == "label":
        openapi_schema = get_openapi_schema("Label API", "API endpoints to create shipments and print labels in Gluey.", "label", labels_documents_router.routes)
    elif schema_type == "manifest":
        openapi_schema = get_openapi_schema("Manifest API", "API endpoints to manifest shipments in Gluey.", "manifest", manifest_router.routes)
    elif schema_type == "tracking":
        openapi_schema = get_openapi_schema("Tracking API", "API endpoints to track shipments in Gluey.", "tracking", tracking_router.routes)
    elif schema_type == "pudo":
        openapi_schema = get_openapi_schema("PUDO API", "API endpoints to get PUDO locations in Gluey.", "pudo",pudo_router.routes)
    elif schema_type == "book":
        openapi_schema = get_openapi_schema("Book API", "API endpoints to book appointments with carriers.", "book",book_router.routes)

    return openapi_schema

@app.get("/webhook-retry", response_class=HTMLResponse, include_in_schema=False)
async def retry(request: Request):
    return templates.TemplateResponse("retry.html", {"request": request, "title": "Webhook Retry Logic"})

@app.get("/webhook-label", response_class=HTMLResponse, include_in_schema=False)
async def redoc(request: Request):
    return templates.TemplateResponse("redoc.html", {"request": request, "spec_url": "/openapiwebhook-label.json", "title": "Shipment Webhooks"})

@app.get("/webhook-tracking", response_class=HTMLResponse, include_in_schema=False)
async def redoc(request: Request):
    return templates.TemplateResponse("redoc.html", {"request": request, "spec_url": "/openapiwebhook-tracking.json", "title": "Tracking Webhooks"})

@app.get("/openapiwebhook-{schema_type}.json", include_in_schema=False)
async def gluey_webhook_openapi(schema_type: str):
    print(schema_type)
    if schema_type == "label":
        openapi_schema = get_openapi_schema("Shipment Webhook", "Webhook to subscribe to, and receive, updates to a Shipment.", "label", label_webhook_subscription_router.routes, label_webhook_router.routes)
    elif schema_type == "tracking":
        openapi_schema = get_openapi_schema("Tracking Webhook", "Webhooks to subscribe to, and receive, tracking events for a shipment.", "tracking", tracking_webhook_subscription_router.routes, tracking_webhook_router.routes)

    return openapi_schema