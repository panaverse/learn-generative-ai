#!/bin/sh

KONG_ADMIN_URL="http://localhost:8001"

# Wait for Kong to be ready
until $(curl --output /dev/null --silent --head --fail $KONG_ADMIN_URL); do
  printf '.'
  sleep 5
done

# Register todo
curl -i -X POST $KONG_ADMIN_URL/services/ \
  --data "name=todo-service" \
  --data "url=http://host.docker.internal:8085"

# Register todo-service route
curl -i -X POST $KONG_ADMIN_URL/services/todo-service/routes \
  --data "paths[]=/todo-service" \
  --data "strip_path=true"

# Register service2
curl -i -X POST $KONG_ADMIN_URL/services/ \
  --data "name=service2" \
  --data "url=http://host.docker.internal:8086"

# Register service2 route
curl -i -X POST $KONG_ADMIN_URL/services/service2/routes \
  --data "paths[]=/service2" \
  --data "strip_path=true"

# Register merged spec service
curl -i -X POST $KONG_ADMIN_URL/services/ \
  --data "name=specs-combiner" \
  --data "url=http://host.docker.internal:9000"

# Register merged spec route
curl -i -X POST $KONG_ADMIN_URL/services/specs-combiner/routes \
  --data "paths[]=/specs-combiner" \
  --data "strip_path=true"

# Register kong-spec-expose plugin
# curl -i -X POST $KONG_ADMIN_URL/services/spec-server/plugins \
#   --data "name=kong-spec-expose" \
#   --data "config.spec_url=http://localhost:8000/merge/openapi.json"
