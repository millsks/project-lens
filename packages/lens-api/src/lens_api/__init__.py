"""LENS API - API service for Lineage & Enterprise eXplainer Service."""

try:
    from lens_api._version import version as __version__
except ImportError:
    __version__ = "0.0.0+unknown"

__all__ = ["__version__"]
