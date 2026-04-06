"""Main application entry point for the RAG demo."""

import logging
from pathlib import Path
import sys
from fastapi import FastAPI
import inngest
import inngest.fast_api
from dotenv import load_dotenv

_SRC_PATH = Path(__file__).resolve().parent / "src"
if str(_SRC_PATH) not in sys.path:
    sys.path.insert(0, str(_SRC_PATH))

from ragagent.workflows.ingest_pdf import run_ingest_pdf
from ragagent.workflows.query_pdf import run_query_pdf

# Load values from the local .env file before the app starts.
# This is where API keys and other local configuration usually live.
load_dotenv()

# Create one shared Inngest client for this application.
# Inngest uses this object to register and serve event-driven functions.
inngest_client = inngest.Inngest(
    app_id="rag_app",
    logger=logging.getLogger("uvicorn"),
    is_production=False,
    serializer=inngest.PydanticSerializer()
)

@inngest_client.create_function(
    fn_id="RAG: Inngest PDF",
    trigger=inngest.TriggerEvent(event="rag/ingest_pdf")
)

async def rag_inngest_pdf(ctx: inngest.Context):
    """Ingest a PDF into the vector database when a PDF event is received."""
    return await run_ingest_pdf(ctx)

@inngest_client.create_function(
    fn_id="RAG: Query PDF",
    trigger=inngest.TriggerEvent(event="rag/query_pdf_ai")
)

async def rag_query_pdf_ai(ctx: inngest.Context):
    """Answer a user's question using text previously stored from PDFs."""
    return await run_query_pdf(ctx)

# FastAPI hosts the HTTP endpoint that Inngest talks to.
app = FastAPI()

# Register the Inngest functions on the FastAPI app.
# After this, the app can receive Inngest requests at the mounted route.
inngest.fast_api.serve(app, inngest_client, [rag_inngest_pdf, rag_query_pdf_ai])
