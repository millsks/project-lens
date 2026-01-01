# LENS API

API service for LENS (Lineage & Enterprise eXplainer Service).

## Overview

LENS API provides a RESTful API for querying and analyzing data lineage and metadata. It sits on top of the `lens-core` package and exposes endpoints for:

- **Lineage Queries**: Retrieve upstream and downstream lineage for data assets
- **Impact Analysis**: Understand the impact of changes to data assets
- **Metadata Retrieval**: Access enriched metadata from connected catalogs
- **Narrative Generation**: Get human-readable explanations of technical lineage

## Installation

```bash
pip install lens-api
```

Note: Installing `lens-api` will automatically install `lens-core` as a dependency.

## Usage

### Running the API Server

```bash
uvicorn lens_api.main:app --reload
```

The API will be available at http://localhost:8000

### API Documentation

Once the server is running, visit:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Example API Calls

```python
import requests

# Health check
response = requests.get("http://localhost:8000/health")
print(response.json())  # {"status": "healthy"}

# Get API version
response = requests.get("http://localhost:8000/")
print(response.json())  # {"message": "LENS API", "version": "..."}
```

## Development

This package is part of the [project-lens](https://github.com/millsks/project-lens) mono-repo.

See the main repository for development setup instructions.

## License

Apache License, Version 2.0 - See LICENSE file in the repository root for details.
