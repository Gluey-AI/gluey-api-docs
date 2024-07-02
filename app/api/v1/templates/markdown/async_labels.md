# Asynchronous Label Generation
Asynchronous label printing means that the label is printed in a separate process the initial shipment have been created.

## Use case / application

1. **Demanding Low Latency Workloads (<100ms)** - Less than 100 ms response time for label printing is required
2. **Demanding Volume** - You are printing high volumes of labels and need a system that can scale to high workloads.
3. **Label can be printed separately from shipment creation** - You do not have a user that is sitting and waiting for a label to be printed, but rather you can allow for the initial shipment to be created minutes, or even hours, before the label is needed.

## How asynchronous label generation works at Gluey
Gluey provides an efficient process for asynchronous label printing, which allows customers to create shipments and print labels separately. This is ideal for high-volume and low-latency needs. The process ensures that all necessary information is collected, processed, and communicated effectively.

1. **Creating a Shipment** - The customer initiates the process by making a POST request to Gluey to create a shipment. This request includes all the details required for generating labels and documents. Gluey returns a shipment ID but no labels yet.
    - **Endpoint:** [Create Shipment](https://developer.gluey.ai/api-label#operation/create_shipment_shipments_post)
2. **Pre-processing Data** - Gluey AI performs pre-processing on the provided shipment data. This may include tasks such as address validation and exchange rate conversion, depending on the specific Gluey API services the customer has chosen to use.
3. **Queueing the Label Request** - Gluey queues the label request and processes it when the carrier API allows.
4. **Generating the Label** - The label can be generated in two ways:
    - **Gluey In-House** - Gluey's internal system generates the label.
    - **Carrier API** - Gluey requests the label from the carrier's API. The carrier processes the request and returns the label data to Gluey AI.
5. **Converting and Caching the Label** - Once the label data is received, Gluey AI converts it into the required format suitable for the customer, such as JPG, PDF, ZPL200, or ZPL300, and caches it for quick access.
6. **Notifying the Customer** - Customers can retrieve the generated label using one of two methods:
    - **Webhook** - Gluey notifies the customer via a webhook.
        - **Endpoint:** [Webhook Notification](https://developer.gluey.ai/webhook-label#operation/receive_webhook_webhook_shipment_post)
    - **Polling** - Customers periodically check Gluey for the label.
        - **Endpoint:** [Check Label](https://developer.gluey.ai/api-label#operation/get_labels_shipments__id__labels_get)

This structured process ensures that customers can efficiently handle high volumes of shipments and retrieve labels when needed without waiting during shipment creation.

## How to build the integration
Below is the integration pattern used for asynchronous label printing, including the relevant endpoints to use, and a step-by-step explanation.

~~~mermaid
sequenceDiagram
    participant Customer
    participant Gluey AI
    participant Gluey LabelEngine
    participant Carrier API

    Customer->>Gluey AI: (1) POST: Create Shipment (/shipments)
    Gluey AI->>Gluey AI: (2) Pre-process: Address / Exchange rates etc
    Gluey AI->>Customer: (3) Response: shipment_id
    Gluey AI->>Gluey AI: (4) Queue Label Request
    alt Step (5a) Gluey In-House
        Note over Gluey AI, Gluey LabelEngine: Gluey Generate In-house
        Gluey AI->>Gluey LabelEngine: (5a.1) Request Label 
        Gluey LabelEngine->>Gluey AI: (5a.2) Return Label Data
    else Step (5b) Carrier API:
        Note over Gluey AI, Carrier API: Request from Carrier API
        Gluey AI->>Carrier API: (5b.1) Request Label
        Carrier API->>Gluey AI: (5b.1) Return Label Data
    end
    Gluey AI->>Gluey AI: (6) Convert and Cache Label
    alt Step (7a) Webhook
        Note over Gluey AI, Customer: Gluey Notify Customer
        Gluey AI->>Customer: (7a.1) POST(Webhook): /webhook/shipment
    else Step (7b) Polling
        Note over Gluey AI, Customer: Customer Poll Gluey
        Customer->>Customer: (7b.1) Trigger label check
        Customer->>Gluey AI: (7b.2) GET: shipment/{id}/label
        Gluey AI->>Customer: (7b.3) Response: label / no label
    end
~~~

### Explanation of steps

1. **POST: Create Shipment (/shipments)** - You as a customer make a POST request towards Gluey to create a shipment. You will receive back a shipment_id but no labels or documents.
    - **Endpoint:** [POST - Create Shipment](https://developer.gluey.ai/api-label#operation/create_shipment_shipments_post)
2. **Pre-process: Address / Exchange rates etc** - Depending on which Gluey api services you have chosen to use, Gluey will attempt to do some pre-processing of the data such as exchange rate conversion etc.
3. **Response: shipment_id** - You will receive back a shipment_id but no labels or documents.
4. **Queue Label Request** - Gluey will now queue the label request towards the carrier and execute it as soon as the rate limit of the carrier api allows for requesting labels. Gluey will now execute the following steps.
5. **Process Label Request** - Gluey processes the label request, which can follow two different paths:
    - **Step 5a: Gluey In-House** - The label is generated in Gluey through a local implementation.
        - **Step 5a.1: Request Label** - Gluey AI sends the label request to Gluey LabelEngine.
        - **Step 5a.2: Return Label Data** - Gluey LabelEngine processes the request and returns the label data to Gluey AI.
    - **Step 5b: Carrier API** - Gluey request the label from the carrier's API.
        - **Step 5b.1: Request Label** - Gluey AI sends the label request to the Carrier API.
        - **Step 5b.2: Return Label Data** - The Carrier API processes the request and returns the label data to Gluey AI.
6. **Convert and Cache Label** - Gluey AI converts the label data into the required format (JPG, PDF, ZPL200, ZPL300) and caches the label data for low latency retrieval.
7. **Notification to Customer** - There are two options to retrieve the label that has been generated:
    - **Step 7a: Webhook**
        - **Step 7a.1: Notify Customer** - Gluey AI notifies you via a webhook you have previously subscribed to.
            - **Endpoint:** [POST - Update Shipment Webhook](https://developer.gluey.ai/webhook-label#operation/receive_webhook_webhook_shipment_post)
    - **Step 7b: Polling**
        - **Step 7b.1: Customer Timer Trigger** - Your system triggers a timer-triggered check for the label.
        - **Step 7b.2: Trigger Label Check** - Your system initiates a request to Gluey to check for the label.
            - **Endpoint:** [GET - Get Labels for Shipment](https://developer.gluey.ai/api-label#operation/get_labels_shipments__id__labels_get)
        - **Step 7b.3: Retrieve Label** - The customer's system retrieves the label if available or receives a response indicating no label is available.