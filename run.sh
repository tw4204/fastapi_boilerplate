docker-compose -f docker/docker-compose.yml -p fastapi_boilerplate down
docker-compose -f docker/docker-compose.yml -p fastapi_boilerplate up -d
docker logs -f fastapi_boilerplate_api_1
