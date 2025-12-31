# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

LENS (Lineage & Enterprise eXplainer Service) is an open-source service that transforms technical lineage and metadata into human-readable explanations. It sits on top of existing data catalogs and lineage platforms, providing APIs to answer questions about data lineage, system dependencies, and impact analysis.

**Status**: Early exploratory phase. Expect breaking changes to APIs and data structures.

## Core Concepts

LENS is designed around three main layers:

1. **Metadata Integration Layer**
   - Connectors to lineage stores (graph DB or vendor API), data catalogs, and optional report registries
   - Normalizes metadata into a simple graph model for reasoning

2. **LENS Service API**
   - Stateless service exposing endpoints like:
     - `GET /explanations/lineage?asset_id=...`
     - `GET /explanations/impact?asset_id=...`
   - Orchestrates metadata retrieval, graph summarization, and LLM calls

3. **Client Integrations**
   - UI buttons/panels in existing catalog or lineage tools
   - Optional CLI or web UI for experimentation

## Technology Stack

- **Python**: 3.12
- **Package Manager**: pixi (conda-based)
- **Build System**: hatch with hatch-vcs for dynamic versioning
- **Web Framework**: FastAPI
- **Data Validation**: Pydantic v2
- **Database**: PostgreSQL with SQLAlchemy 2.0 ORM and Alembic for migrations
- **Task Queue**: Celery with Flower for monitoring
- **Message Broker**: Redis (for Celery)
- **Development Tools**:
  - Linting & Formatting: ruff
  - Type Checking: pyright
  - Testing: pytest with pytest-cov, pytest-asyncio
- **LLM Integration**: Uses LLMs to generate narratives from graph-shaped metadata

## Key Design Principles

- **Metadata-First**: Works only with metadata, never touches raw data
- **Adapter Pattern**: Integrates with existing tools via connectors/adapters
- **Stateless Service**: API designed to be stateless for easy scaling
- **Narrative Generation**: Converts technical graphs into structured text (executive summary, technical summary, upstream/downstream highlights)

## Setup and Installation

### Prerequisites

- [pixi](https://pixi.sh) package manager installed
- [Docker](https://www.docker.com/) and Docker Compose (for local PostgreSQL and Redis)

### Initial Setup

```bash
# Install all dependencies (creates .pixi environment)
pixi install

# Install dev environment with development tools
pixi install -e dev

# Copy environment variables template and configure as needed
cp .env.example .env

# Start PostgreSQL and Redis using Docker Compose
pixi run docker-up
```

**Note**: Most development commands require the `dev` environment. Use `pixi run -e dev <command>` or activate the dev shell with `pixi shell -e dev`.

## Docker Services

The project uses Docker Compose to manage PostgreSQL and Redis for local development.

### Docker Compose Commands

```bash
# Start all services (PostgreSQL + Redis) in detached mode
pixi run docker-up

# Stop all services
pixi run docker-down

# View logs from all services
pixi run docker-logs

# Check status of services
pixi run docker-ps

# Restart all services
pixi run docker-restart

# Stop services and remove volumes (⚠️ deletes all data)
pixi run docker-clean
```

### Service Details

**PostgreSQL**:
- Image: `postgres:16-alpine`
- Default Port: `5432`
- Default Credentials: `lens` / `lens_dev_password`
- Database: `lens`
- Data persisted in Docker volume `postgres_data`

**Redis**:
- Image: `redis:7-alpine`
- Default Port: `6379`
- Default Password: `lens_dev_password`
- Data persisted in Docker volume `redis_data`

**Environment Configuration**:
- Copy `.env.example` to `.env` and customize as needed
- All connection strings and credentials are configurable via `.env`

## Common Commands

### Development Server

```bash
# Run FastAPI development server with auto-reload
pixi run dev
```

### Code Quality

```bash
# Run linter
pixi run -e dev lint

# Format code
pixi run -e dev format

# Check formatting without making changes
pixi run -e dev format-check

# Run type checker
pixi run -e dev typecheck
```

### Testing

```bash
# Run all tests
pixi run -e dev test

# Run tests with coverage report
pixi run -e dev test-cov

# Run specific test file
pixi run -e dev pytest tests/test_main.py

# Run tests matching pattern
pixi run -e dev pytest -k "test_health"
```

### Building

```bash
# Build Python wheel and sdist (using hatch) - Recommended
pixi run -e dev build-python

# Note: pixi build for conda packages is a preview feature and currently
# has limitations with Python build backends. Use the Python wheel/sdist
# for PyPI distribution. For conda packages, use conda-build or grayskull
# to convert the PyPI package if needed.
```

### Database Migrations (Alembic)

```bash
# Create a new migration
pixi run alembic revision --autogenerate -m "description"

# Apply migrations
pixi run alembic upgrade head

# Rollback one migration
pixi run alembic downgrade -1

# Show current migration status
pixi run alembic current
```

### Celery Tasks

```bash
# Start Celery worker
pixi run celery -A lens.tasks worker --loglevel=info

# Start Flower monitoring UI
pixi run celery -A lens.tasks flower
```

## Project Structure

```text
project-lens/
├── src/lens/              # Main application package
│   ├── __init__.py
│   ├── _version.py        # Auto-generated by hatch-vcs
│   └── main.py            # FastAPI application entry point
├── tests/                 # Test suite
├── pixi.toml              # Pixi package manager configuration
├── pyproject.toml         # Python project metadata and tool configs
├── pixi.lock              # Lock file for reproducible environments
├── docker-compose.yml     # Docker services (PostgreSQL, Redis)
├── .env.example           # Environment variables template
└── .env                   # Local environment variables (git-ignored)
```

## Configuration Files

- **pixi.toml**: Pixi environment and dependency management
- **pyproject.toml**: Python project metadata, build configuration (hatch), and tool settings (ruff, pyright, pytest, coverage)
- **pixi.lock**: Auto-generated lock file for reproducible builds (commit to version control)
- **docker-compose.yml**: Local development services (PostgreSQL 16, Redis 7)
- **.env.example**: Template for environment variables (commit to version control)
- **.env**: Local environment configuration (git-ignored, copy from .env.example)

## Current Development Goals

1. Solidify core data model for lineage and impact
2. Provide minimal reference implementation of LENS API
3. Add example adapters for common catalog/lineage tools

## License

Apache License, Version 2.0
