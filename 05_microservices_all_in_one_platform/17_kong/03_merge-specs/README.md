# Combine Microservices OpenAPI Specification

- Goal: Get a merged OpenAPI Specification for all microservices. And it's updated live as any microservice codebase changes.

- Plan: We will have a new microservice `spec-merge` that will:
  1. Fetch/GET all MicroService OpenAPI Specifications 
  2. Combine them to a single specification.
  3. Serve the combined specification as a JSON response in the browser using FastAPI's JSONResponse class. i.e: we can access through an endpoint.
  4. Now we will have a dedicated endpoint to get Live Aggregated OpenAPI Specification that is updated with each microservice spec change.

Right now we have achieved our Goal to get Consolidated Spec through another microservice. In Future we can use a Kong Community plugin to register the OpenAPI specification if needed. This setup can be used in production to reduce this microservice addition. Additionally, it demonstrates how to use Kong community-developed plugins.

## Get Hands on Code

1. Get everything working
```
docker compose --profile database up -d
```

2. Visit Each Microservice Separately

- Todo: http://localhost:8085/docs
- Microservice 2: http://localhost:8086/docs
- Specs Combiner: http://localhost:9000/docs

The Combined OpenAI Spec is present at: 

http://localhost:9000/merged/openapi.json

3. Now let's setup Kong.

Rather than Kong UI we will run this script to register all Gateway services and Routes, In terminal:

```
chmod +x gateway-startup.sh

./gateway-startup.sh
```

Now our API Gateway Microservice Routes are:

- Todo: http://localhost:8000/todo-service/docs
- Microservice 2: http://localhost:8000/service2/docs
- Merged Spec: http://localhost:8000/specs-combiner//merged/openapi.json

## How to Add/Manage More Microservices Spec?

In specs-combiner/app/main.py we have:

```    
services = [
        {"name": "todo-service", "url": "http://host.docker.internal:8085/openapi.json", "base_route": "/todo-service"},
        {"name": "service2", "url": "http://host.docker.internal:8086/openapi.json", "base_route": "/service2"},
    ]
```

Here `url` is our microservice spec url. `base_route` is the route registered in kong gateway. The same base_route is added in that particular microservice `app = FastAPI(root_path="...")` to load the swagger docs.

## Extra: How to Register Custom Spec Plugin?

Community plugins like kong-spec-expose are not available in the Kong plugins section by default. To use it, we will build and use a custom Kong image.

1. See the kong-custom/Dockerfile. 
2. Now in docker-compose.yml Open and replace the kong images to use this custom kong image.

```
curl -i -X POST http://localhost:8001/services/0b1b50fc-34a8-4001-b696-ab849bb0f6de/plugins \
  --data "name=kong-spec-expose" \
  --data "config.spec_url=http://localhost:8000/merge/openapi.json"
```

Add spec route to service
```
curl -i -X POST http://localhost:8001/services/0b1b50fc-34a8-4001-b696-ab849bb0f6de/routes \
  --data "paths[]=/merge/specz"
```