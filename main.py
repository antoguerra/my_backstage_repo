from fastapi import FastAPI, status
from fastapi.responses import PlainTextResponse

app = FastAPI(
    title="Hello-World API",
    version="0.1.0",
    description="Dummy ping endpoint for Backstage demo",
)

@app.get("/ping", response_class=PlainTextResponse,
         status_code=status.HTTP_200_OK, tags=["health"])
async def ping() -> str:
    """Health-check endpoint that answers with `pong`."""
    return "pong"
