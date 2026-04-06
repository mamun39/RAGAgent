"""Compatibility shim for the Streamlit app entrypoint."""

from bootstrap_src import ensure_src_path


ensure_src_path(__file__)

from ragagent.app.streamlit_app import *  # noqa: F401,F403
