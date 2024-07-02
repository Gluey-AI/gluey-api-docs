# Asynchronous Label Generation
Asynchronous label printing means that the label is printed in a separate process the initial shipment have been created.

**Use case / application:**

1. **Demanding Low Latency Workloads (<100ms)** - Less than 100 ms response time for label printing is required
2. **Demanding Volume** - You are printing high volumes of labels and need a system that can scale to high workloads.
3. **Label can be printed separately from shipment creation** - You do not have a user that is sitting and waiting for a label to be printed, but rather you can allow for the initial shipment to be created minutes, or even hours, before the label is needed.

Below is the integration pattern used for asynchronous label printing.

~~~mermaid
sequenceDiagram
    participant Customer API
    participant Gluey AI
    participant Gluey Carrier Service
    participant Carrier API

    Customer API->>Gluey AI: POST: Create Shipment (/shipments)
    Gluey AI->>Gluey AI: Pre-process: Address / Exchange rates etc
    Gluey AI->>Customer API: Response: shipment_id
    Gluey AI->>Gluey Carrier Service: Queue Label Request
    Note over Gluey Carrier Service, Gluey Carrier Service: Timer Triggered Process
    Gluey Carrier Service->>Gluey Carrier Service: De-queue label request
    Gluey Carrier Service->>Carrier API: Process Label Request 
    Carrier API-->>Gluey Carrier Service: Return Label Data
    Gluey Carrier Service->>Gluey AI: Post label
    Gluey AI->>Gluey AI: Convert Label Format
    Gluey AI->>Gluey AI: Cache Label
    alt Option 1: Webhook
        Note over Gluey AI, Customer API: Gluey Notify Customer
        Gluey AI->>Customer API: POST(Webhook): label_update
        Customer API->>Gluey AI: GET: shipment/{id}/label
        Gluey AI->>Customer API: Response: label
    else Option 2: Scheduled Call
        Note over Gluey AI, Customer API: Customer Timer Trigger
        Customer API->>Customer API: Trigger label check
        Customer API->>Gluey AI: GET: shipment/{id}/label
        Gluey AI->>Customer API: Response: label / no label
    end
~~~