from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import requests
import logging
from jsonmerge import merge

app = FastAPI(docs_url="/docs", root_path="/specs-combiner")


class ServiceSpec(BaseModel):
    url: str
    base_route: str


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fetch_openapi_specs():
    services = [
        {"name": "todo-service", "url": "http://host.docker.internal:8085/openapi.json", "base_route": "/todo-service"},
        {"name": "service2", "url": "http://host.docker.internal:8086/openapi.json", "base_route": "/service2"},
    ]
    specs = []
    for service in services:
        try:
            logger.info(f"Fetching spec from {service['url']}")
            response = requests.get(service["url"], headers={'Cache-Control': 'no-cache'})
            response.raise_for_status()
            spec = response.json()
            # Add base route to all paths
            spec_with_base_route = add_base_route_to_paths(spec, service["base_route"])
            specs.append(spec_with_base_route)
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching {service['name']} spec: {e}")
            raise HTTPException(status_code=500, detail=f"Error fetching {service['name']} spec: {e}")
    return specs


def add_base_route_to_paths(spec, base_route):
    new_paths = {}
    for path, path_item in spec.get("paths", {}).items():
        new_path = f"{base_route}{path}"
        new_paths[new_path] = path_item
    spec["paths"] = new_paths
    return spec


def merge_openapi_specs(specs):
    merged_spec = {
        "openapi": "3.0.0",
        "info": {
            "title": "Merged API",
            "version": "1.0.0"
        },
        "servers": [
            {"url": "/"}  # Define a single server URL
        ],
        "paths": {},
        "components": {
            "schemas": {},
            "responses": {},
            "parameters": {},
            "examples": {},
            "requestBodies": {},
            "headers": {},
            "securitySchemes": {},
            "links": {},
            "callbacks": {}
        }
    }

    for spec in specs:
        # Merge paths
        merged_spec["paths"] = merge(merged_spec["paths"], spec.get("paths", {}))

        # Merge components
        for component, items in spec.get("components", {}).items():
            if component not in merged_spec["components"]:
                merged_spec["components"][component] = items
            else:
                merged_spec["components"][component] = merge(merged_spec["components"][component], items)

    return merged_spec


@app.get("/merged/openapi.json")
async def get_merged_openapi_spec():
    specs = fetch_openapi_specs()
    merged_spec = merge_openapi_specs(specs)
    response = JSONResponse(content=merged_spec)
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

