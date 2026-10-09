#!/usr/bin/env bash
set -euo pipefail

docker compose down -v

echo "Shydrie stack stopped and volumes removed."
