"""Compatibility re-exports for ingestion scanning."""

from bootstrap_src import ensure_src_path


ensure_src_path(__file__)

from ragagent.security.ingestion_scanner import *  # noqa: F401,F403
