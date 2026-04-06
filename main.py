"""Compatibility shim for the FastAPI and Inngest app entrypoint."""

from bootstrap_src import ensure_src_path


ensure_src_path(__file__)

from ragagent.app.inngest_app import app, inngest_client, rag_inngest_pdf, rag_query_pdf_ai

__all__ = ["app", "inngest_client", "rag_inngest_pdf", "rag_query_pdf_ai"]
