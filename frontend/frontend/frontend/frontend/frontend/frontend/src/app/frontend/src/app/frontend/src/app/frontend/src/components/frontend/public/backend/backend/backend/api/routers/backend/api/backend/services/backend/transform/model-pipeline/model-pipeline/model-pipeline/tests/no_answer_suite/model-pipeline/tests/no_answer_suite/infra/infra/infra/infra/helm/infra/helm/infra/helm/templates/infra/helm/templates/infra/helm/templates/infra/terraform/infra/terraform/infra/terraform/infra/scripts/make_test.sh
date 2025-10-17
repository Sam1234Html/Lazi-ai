#!/bin/bash
cd ../model-pipeline && pytest tests/no_answer_suite/
cd ../frontend && npm test
cd ../backend && pytest
# TODO: Add e2e tests with Cypress, load tests with k6
