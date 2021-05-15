docker run --rm \
  --network fastapi_boilerplate_default \
  --link fastapi_boilerplate_postgres_1:postgres \
  --name migrate \
  -w /source \
  --env-file $PWD/../.env \
  -v $PWD/../source:/source \
  tw4204/fastapi-boilerplate \
  python migrate.py
