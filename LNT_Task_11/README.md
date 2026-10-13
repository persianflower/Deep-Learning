# Task 11: Full Application Containerization

### Objective

To containerize the complete deep learning solution including model, Flask API, and  Streamlit UI.

Deliverables

• Dockerized application.

[Application](https://github.com/persianflower/Deep-Learning/tree/main/LNT_Task_11)

• Architecture diagram.

```mermaid
flowchart TD
    A[Start] --> B
    B[Dockerfile] --> C{Run container}
    C -->|Backend| D[Flask runs on port: 8501]
    C -->|Frontend| D[Streamlit runs on local device via entrypoint command]
    C --> F[Prediction]
    D --> F
    F --> G[End]
```
 
• Testing report.

[Outputs]()
