"""Compatibility re-exports for shared workflow models."""

from pathlib import Path
import sys

_SRC_PATH = Path(__file__).resolve().parent / "src"
if str(_SRC_PATH) not in sys.path:
    sys.path.insert(0, str(_SRC_PATH))

from ragagent.models.payloads import ChunkSecurityMetadata, RAGChunkPayload, RetrievedChunk
from ragagent.models.policy import RetrievalPolicyContext
from ragagent.models.results import (
    IngestScanResult,
    OutputFilterResult,
    RAGChunkAndSrc,
    RAGQueryResult,
    RAGSearchResult,
    RAGUpsertResult,
)

__all__ = [
    "ChunkSecurityMetadata",
    "RAGChunkPayload",
    "RetrievedChunk",
    "RetrievalPolicyContext",
    "IngestScanResult",
    "OutputFilterResult",
    "RAGChunkAndSrc",
    "RAGQueryResult",
    "RAGSearchResult",
    "RAGUpsertResult",
]
