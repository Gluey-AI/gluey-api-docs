# Tracking
Gluey offers customers the ability to receive tracking updates via webhooks, sFTP or polling our API endpoints.

For most use cases it is recommended utilising the tracking webhooks from Gluey to ensure scalability in data transfer, and achieving the best data freshness.

Below is the integration pattern for getting tracking from Gluey.

~~~mermaid
sequenceDiagram
    participant Customer API
    participant Gluey AI
    participant Gluey Carrier Service
    participant Carrier API

    alt Option 1: Webhook
        Note over Gluey Carrier Service, Carrier API: Webhook to Gluey
        Carrier API->>Gluey Carrier Service: POST: tracking events
    else Option 2: sFTP
        Note over Gluey Carrier Service, Carrier API: Timer: Every 1 minute
        Gluey Carrier Service->>Gluey Carrier Service: Dequeue tracking check
        Gluey Carrier Service->>Carrier API: SSH: tracking events
        Carrier API->>Gluey Carrier Service: Tracking Response
    else Option 3: API
        Note over Gluey Carrier Service, Carrier API: Timer: ~5-15 minutes
        Gluey Carrier Service->>Gluey Carrier Service: Dequeue tracking check
        Gluey Carrier Service->>Carrier API: GET: tracking evenst
        Carrier API->>Gluey Carrier Service: Tracking Response
    end
    Gluey Carrier Service->>Gluey Carrier Service: Process Tracking Event
    Gluey Carrier Service->>Gluey AI: Post Tracking
    alt Option 1: Webhook
        Note over Gluey AI, Customer API: Webhook to Customer
        Gluey AI->>Gluey AI: Generate payload
        Gluey AI-->>Customer API: POST (Webhook): tracking_events
    else Option 2: sFTP
        Note over Gluey AI, Customer API: sFTP file transfer to Customer
        Gluey AI->>Gluey AI: Generate file
        Gluey AI-->>Customer API: SSH: tracking_events
    else Option 3: API
        Note over Gluey AI, Customer API: Customer Timer Trigger
        Customer API->>Gluey AI: POST: track
        Gluey AI->>Gluey AI: Batch retrieval
        Gluey AI-->>Customer API: Response: tracking_events
    end
~~~