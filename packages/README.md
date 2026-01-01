# LENS Packages

This directory contains the Python packages that make up the LENS (Lineage & Enterprise eXplainer Service) project.

## Packages

### lens-core

Core functionality for LENS, including:

- Data models (Pydantic, SQLAlchemy)
- Database schemas and migrations
- Business logic and utilities
- Metadata connectors and adapters
- Celery tasks for async processing
- Graph algorithms for lineage analysis

**Location**: `packages/lens-core/`
**PyPI**: `lens-core`
**Import**: `from lens_core import ...`

### lens-api

REST API service for LENS, built with FastAPI:

- HTTP endpoints for lineage queries
- Impact analysis endpoints
- Metadata retrieval APIs
- OpenAPI documentation

**Location**: `packages/lens-api/`
**PyPI**: `lens-api`
**Import**: `from lens_api import ...`
**Depends on**: `lens-core`

## Versioning

Each package has independent versioning using git tags:

- **lens-core**: Tagged with `core-v*` (e.g., `core-v1.0.0`)
- **lens-api**: Tagged with `api-v*` (e.g., `api-v1.0.0`)

Versions are automatically generated from git tags using hatch-vcs.

## Development

For development setup and contribution guidelines, see the main [README.md](../README.md) in the repository root.

## Where to Add Code

**Add to lens-core** if the code is:
- Data models, schemas, or migrations
- Business logic or core utilities
- Database access or connectors
- Background tasks (Celery)
- Graph algorithms or lineage processing

**Add to lens-api** if the code is:
- FastAPI routes or endpoints
- Request/response models (API-specific)
- API middleware or authentication
- OpenAPI schema customization

## License

Apache License, Version 2.0 - See LICENSE file in the repository root for details.
