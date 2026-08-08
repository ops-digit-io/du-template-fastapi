# du-template-fastapi

PoC template · **FastAPI service (Python)**.

A small HTTP API exposing the computed metric — when the PoC is a service, not a screen.

Follows [FastAPI Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/). Used by the digitalization
portal's PoC builder via GitHub "generate from template" — the portal creates a
use-case repository from this template, then overlays the case's own files.

Run locally: `uvicorn app.main:app --reload` (from `poc/`).
