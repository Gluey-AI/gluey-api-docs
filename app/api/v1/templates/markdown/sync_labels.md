# Synchronous Label Generation
Synchronous label printing means that the label is printed in the same call as when the shipment is created.

## Use case / application

1. **Moderate Latency Requirements (~1-2 seconds)** - An average of 1-2 seconds of latency is acceptable for the workload, and even up to 4-5 seconds in extreme cases.
2. **Label needs to be printed immediately** - You have a user that is sitting and waiting for a label, qr code or parcel locker pin code to be generated immediately.

## How synchronous label generation works at Gluey
Gluey provides an efficient process for synchronous label printing, which allows customers to create shipments, generate shipping labels, and receive additional documents and tracking data seamlessly. This process involves several steps to ensure that all necessary information is collected, processed, and communicated effectively.

1. **Creating a Shipment** - The customer initiates the process by making a POST request to Gluey to create a shipment. This request includes all the details required for generating labels and additional documents.
2. **Pre-processing Data** - Gluey AI performs pre-processing on the provided shipment data. This may include tasks such as address validation and exchange rate conversion, depending on the specific Gluey API services the customer has chosen to use.
3. **Processing the Label Request** - Gluey processes the label request using one of two methods:
    - **Gluey In-House** - Gluey AI sends the label request to its internal LabelEngine, which generates the label data and returns it to Gluey AI.
    - **Carrier API** - Gluey AI sends the label request to the carrier's API. The carrier processes the request and returns the label data to Gluey AI.
4. **Converting the Label Format** - Once the label data is received, Gluey AI converts it into the required format suitable for the customer, such as JPG, PDF, ZPL200, or ZPL300.
5. **Generating Additional Documents** - Gluey generates any additional documents needed for the shipment, such as commercial invoices.
6. **Responding to the Customer** - Finally, Gluey returns a response to the customer that includes the shipping label, any additional documents, and tracking data. This comprehensive response ensures that the customer has all the necessary information to proceed with the shipment.

This structured process ensures that customers can efficiently create shipments and receive all the required documentation and tracking information, whether Gluey generates the labels in-house or retrieves them from the carrier's API.

## How to build the integration
Below is the integration pattern used for asynchronous label printing, including the relevant endpoints to use, and a step-by-step explanation.

~~~mermaid
sequenceDiagram
    participant Customer
    participant Gluey AI
    participant Gluey LabelEngine
    participant Carrier API

    Customer->>Gluey AI: (1) POST Create Shipment (/shipment_with_labels_documents)
    Gluey AI->>Gluey AI: (2) Pre-process: Address / Exchange rates etc
    alt Step (3a) Gluey In-House
        Note over Gluey AI, Gluey LabelEngine: Gluey Generate In-house
        Gluey AI->>Gluey LabelEngine: (3a.1) Request Label 
        Gluey LabelEngine->>Gluey AI: (3a.2) Return Label Data
    else Step (3b) Carrier API:
        Note over Gluey AI, Carrier API: Request from Carrier API
        Gluey AI->>Carrier API: (3b.1) Request Label
        Carrier API->>Gluey AI: (3b.1) Return Label Data
    end
    Gluey AI->>Gluey AI: (4) Convert Label Format
    Gluey AI->>Gluey AI: (5) Generate Addititonal Documents
    Gluey AI-->>Customer: (6) Response: label / documents / tracking data
~~~

### Explanation of steps

1. **POST: Create Shipment (/shipment_with_labels_documents)** - You as a customer make a POST request towards Gluey to create a shipment. This request includes details required for generating labels and additional documents.
    - **Endpoint:** [Create Shipment with Labels and Documents](https://developer.gluey.ai/api-label#operation/shipment_labels_documents_shipment_with_labels_documents_post)
2. **Pre-process: Address / Exchange rates etc** - Depending on which Gluey API services you have chosen to use, Gluey will attempt to do some pre-processing of the data such as exchange rate conversion, address validation, etc.
3. **Process Label Request** - Gluey processes the label request, which can follow two different paths:
    - **Step 3a: Gluey In-House** - The label is generated in Gluey through a local implementation.
        - **Step 3a.1: Request Label** - Gluey AI sends the label request to Gluey LabelEngine.
        - **Step 3a.2: Return Label Data** - Gluey LabelEngine processes the request and returns the label data to Gluey AI.
    - **Step 3b: Carrier API** - Gluey requests the label from the carrier's API.
        - **Step 3b.1: Request Label** - Gluey AI sends the label request to the Carrier API.
        - **Step 3b.2: Return Label Data** - The Carrier API processes the request and returns the label data to Gluey AI.
4. **Convert Label Format** - Gluey AI converts the label data into the required format suitable for the customer (JPG, PDF, ZPL200, ZPL300).
5. **Generate Additional Documents** - Gluey generates any additional documents that are needed for the shipment, such as commercial invoices etc.
6. **Response: label / documents / tracking data** - Gluey returns the response to the Customer, including the label, any additional documents, and tracking data.