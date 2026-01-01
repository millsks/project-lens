# LENS Core

Core functionality for LENS (Lineage & Enterprise eXplainer Service).

## Overview

LENS Core provides the foundational components for the LENS system, including:

- **Data Models**: Pydantic and SQLAlchemy models for lineage and metadata
- **Database Layer**: Schema definitions and migrations (Alembic)
- **Business Logic**: Core processing and transformation logic
- **Metadata Connectors**: Adapters for integrating with data catalogs and lineage platforms
- **Task Processing**: Celery tasks for asynchronous data processing
- **Graph Algorithms**: Lineage traversal and impact analysis

## Installation

```bash
pip install lens-core
```

## Usage

```python
from lens_core import __version__

print(f"LENS Core version: {__version__}")
```

## Development

This package is part of the [project-lens](https://github.com/millsks/project-lens) mono-repo.

See the main repository for development setup instructions.

## License

Apache License, Version 2.0 - See LICENSE file in the repository root for details.
