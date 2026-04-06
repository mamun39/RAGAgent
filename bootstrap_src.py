"""Shared helper for making the local src/ package importable."""

from pathlib import Path
import sys


def ensure_src_path(relative_to: str, levels_up: int = 0) -> Path:
    """Insert the repository src/ directory into sys.path if needed."""
    base_path = Path(relative_to).resolve()
    for _ in range(levels_up):
        base_path = base_path.parent
    src_path = base_path.parent / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))
    return src_path
