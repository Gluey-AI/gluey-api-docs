# Synchronous Label Generation
Synchronous label printing means that the label is printed in the same call as when the shipment is created.

**Use case / application:**

1. **Moderate Latency Requirements (~1-2 seconds)** - An average of 1-2 seconds of latency is acceptable for the workload, and even up to 4-5 seconds in extreme cases.
2. **Label needs to be printed immediately** - You have a user that is sitting and waiting for a label, qr code or parcel locker pin code to be generated immediately.

Below is the integration pattern used for asynchronous label printing.

~~~mermaid
sequenceDiagram
    participant Customer API
    participant Gluey AI
    participant Carrier API

    Customer API->>Gluey AI: POST: Create Shipment (/shipment_with_labels_documents)
    Gluey AI->>Gluey AI: Pre-process: Address / Exchange rates etc
    Gluey AI->>Carrier API: Process Label Request
    Carrier API-->>Gluey AI: Return Label Data
    Gluey AI->>Gluey AI: Convert Label Format
    Gluey AI->>Gluey AI: Generate Addititonal Documents
    Gluey AI-->>Customer API: Response: label / documents / tracking data
~~~