#!/usr/bin/env bash
set -euo pipefail

if ! command -v docker >/dev/null 2>&1; then
  echo "Docker is required to run Shydrie locally"
  exit 1
fi

mkdir -p ./data

docker compose up --build -d

printf '\nShydrie is running.\n'
printf 'API: http://localhost:8000/docs\n'
printf 'MinIO: http://localhost:9001\n'
printf 'Redis: localhost:6379\n'
printf 'PostgreSQL: localhost:5432\n'
