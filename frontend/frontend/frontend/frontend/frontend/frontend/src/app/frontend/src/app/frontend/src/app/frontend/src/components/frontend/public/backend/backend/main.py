from fastapi import FastAPI
from api.routers import conversation, upload, profile

app = FastAPI(title="Lazy AI API", openapi_url="/openapi.json")

app.include_router(conversation.router, prefix="/v1/conversation")
app.include_router(upload.router, prefix="/v1/upload")
app.include_router(profile.router, prefix="/v1/profile")

# TODO: Add middleware for auth (JWT), logging (Sentry), and metrics (Prometheus)
