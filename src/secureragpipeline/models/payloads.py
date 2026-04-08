"""Payload and retrieved-chunk models."""

import pydantic


class ChunkSecurityMetadata(pydantic.BaseModel):
    """Security-related metadata stored with each chunk payload."""

    doc_id: str
    chunk_id: str
    tenant_id: str = "demo"
    owner_id: str = "local_user"
    classification: str = "internal"
    trust_level: str = "user_uploaded"
    ingest_scan_flags: list[str] = pydantic.Field(default_factory=list)
    ingest_decision: str = "allow"
    content_hash: str
    created_at: str


class RAGChunkPayload(ChunkSecurityMetadata):
    """Full payload stored in Qdrant for one chunk."""

    source: str
    text: str


class RetrievedChunk(pydantic.BaseModel):
    """Retrieved chunk plus payload metadata needed for safe prompt assembly."""

    text: str
    source: str = ""
    classification: str = "internal"
    trust_level: str = "user_uploaded"
    ingest_decision: str = "allow"
    ingest_scan_flags: list[str] = pydantic.Field(default_factory=list)


class QueryAPIRequest(pydantic.BaseModel):
    """Request body for the external query API."""

    question: str | None = None
    role: str | None = None
    tenant_id: str | None = None
    source_id: str | None = None
