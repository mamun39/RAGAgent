"""Compatibility re-exports for ingestion data loading helpers."""

from bootstrap_src import ensure_src_path


ensure_src_path(__file__)

from ragagent.ingestion.data_loader import *  # noqa: F401,F403
