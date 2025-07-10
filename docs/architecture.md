# Architecture

```mermaid
flowchart TD
    B[Browser] -->|HTTP 80| A(🚀 FastAPI app)
    A -->|Reads / Writes| D[(PostgreSQL)]
    A -->|Publishes metrics| M[[Prometheus]]

