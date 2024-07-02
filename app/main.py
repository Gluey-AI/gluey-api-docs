from fastapi import FastAPI
from fastapi.responses import HTMLResponse
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
async def home(request: Request):
    return __create_template(request, "async_labels.md", "Generating Labels Asynchronously")

@app.get("/sync-labels", response_class=HTMLResponse, include_in_schema=False)
async def home(request: Request):
    return __create_template(request, "sync_labels.md", "Generating Labels Synchronously")

@app.get("/tracking", response_class=HTMLResponse, include_in_schema=False)
async def home(request: Request):
    return __create_template(request, "tracking.md", "Integrating Tracking From Gluey")

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
        openapi_schema = get_openapi_schema("Label API", "API endpoints to create shipments and print labels in Gluey.", "label", labels_documents_router.routes, label_webhook_router.routes)
    elif schema_type == "manifest":
        openapi_schema = get_openapi_schema("Manifest API", "API endpoints to manifest shipments in Gluey.", "manifest", manifest_router.routes)
    elif schema_type == "tracking":
        openapi_schema = get_openapi_schema("Tracking API", "API endpoints to track shipments in Gluey.", "tracking", tracking_router.routes)
    elif schema_type == "pudo":
        openapi_schema = get_openapi_schema("PUDO API", "API endpoints to get PUDO locations in Gluey.", "pudo",pudo_router.routes)

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