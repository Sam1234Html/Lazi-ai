#!/bin/bash
cd ../frontend && docker build -f ../infra/Dockerfile.frontend -t lazy-ai-frontend:latest .
cd ../backend && docker build -f ../infra/Dockerfile.backend -t lazy-ai-backend:latest .
cd ../model-pipeline && docker build -f ../infra/Dockerfile.model -t lazy-ai-model:latest .
