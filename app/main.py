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

contact = {
    "name": "Engineering",
    "url": "https://github.com/Gluey-AI",
    "email": "engineering@gluey.ai"
}


app = FastAPI(
    title="Gluey API",
    description="API endpoints for Gluey"
)

app.include_router(labels_documents_router)
app.include_router(manifest_router)
app.include_router(tracking_router)
app.include_router(pudo_router)

templates = Jinja2Templates(directory="app/api/v1/templates")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.middleware("http")
async def add_gluey_server(request: Request, call_next):
    # header 'server' is removed in Uvicorn by flag --no-server-header
    response = await call_next(request)
    response.headers["server"] = "gluey"
        
    return response

def get_openapi_schema(openapi_title: str, openapi_desc:str, routes: any):
    openapi_schema = get_openapi(
        title=openapi_title,
        version="0.1.0",
        description=openapi_desc,
        servers=servers,
        contact=contact,
        routes=routes
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
    print(schema_type)
    if schema_type == "label":
        openapi_schema = get_openapi_schema("Label API", "API endpoints to create shipments and print labels in Gluey.", labels_documents_router.routes)
    elif schema_type == "manifest":
        openapi_schema = get_openapi_schema("Manifest API", "API endpoints to manifest shipments in Gluey.", manifest_router.routes)
    elif schema_type == "tracking":
        openapi_schema = get_openapi_schema("Tracking API", "API endpoints to track shipments in Gluey.", tracking_router.routes)
    elif schema_type == "pudo":
        openapi_schema = get_openapi_schema("PUDO API", "API endpoints to get PUDO locations in Gluey.", pudo_router.routes)

    return openapi_schema

@app.get("/webhook-endpoints", response_class=HTMLResponse, include_in_schema=False)
async def webhooks(request: Request):
    return templates.TemplateResponse("webhooks.html", {"request": request, "title": "Webhook Endpoints"})

@app.get("/webhook-retry", response_class=HTMLResponse, include_in_schema=False)
async def retry(request: Request):
    return templates.TemplateResponse("retry.html", {"request": request, "title": "Webhook Retry Logic"})