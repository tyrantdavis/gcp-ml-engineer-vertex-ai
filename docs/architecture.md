```mermaid
flowchart LR
    A[Data Sources] --> B[Feature Engineering]
    B --> C[Training Code<br/>training/]
    C --> D[Training Pipeline<br/>mlops/pipelines/]
    D --> E[Model Artifact]
    E --> F[Deployment Config<br/>deployment/]
    F --> G[Serving Endpoint]
    G --> H[Monitoring<br/>mlops/monitoring/]
    H --> D
```

This:

- Shows system boundaries
- Shows directory ownership
- Shows feedback loop
- Looks professional
- Signals architectural maturity