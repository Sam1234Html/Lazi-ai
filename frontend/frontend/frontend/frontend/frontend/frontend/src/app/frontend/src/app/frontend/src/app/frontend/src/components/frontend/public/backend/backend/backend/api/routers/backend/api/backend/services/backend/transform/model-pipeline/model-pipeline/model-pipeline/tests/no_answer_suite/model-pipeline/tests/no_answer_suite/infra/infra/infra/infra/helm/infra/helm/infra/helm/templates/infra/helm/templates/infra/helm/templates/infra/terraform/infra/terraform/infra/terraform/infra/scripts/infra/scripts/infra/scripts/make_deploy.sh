#!/bin/bash
helm upgrade --install lazy-ai ../infra/helm --namespace lazy-ai --create-namespace --set env=$1
