# Book
Book is for when you wish to query a carrier for available collection dates/times/time windows and then book a collection with them.

## How booking works at Gluey
Gluey provides an efficient process for booking collection dates and times, allowing customers to arrange their shipments smoothly. This process involves several steps to ensure that all necessary information is collected, processed, and communicated effectively.

1. **Creating a Shipment** - The customer initiates the process by making a POST request to Gluey to create a shipment. This request includes all the details required for the booking process.

Once the shipment is created, you can proceed with the booking process.

## How to build the integration
Below is the integration pattern used for booking collection dates, including the relevant endpoints to use, and a step-by-step explanation.

~~~mermaid
sequenceDiagram
    participant 👤 User
    participant 🏭 Customer
    participant 🤖 Gluey AI
    participant 🚚 Carrier API
    participant 💳 Payment Provider

    🏭 Customer->>🤖 Gluey AI: (1) POST: Create Shipment
    🤖 Gluey AI->>🏭 Customer: (2) Return Shipment ID
    🏭 Customer->>🤖 Gluey AI: (3) POST: Request Available Collection Dates (/shipments/{id}/collections)
    🤖 Gluey AI->>🚚 Carrier API: (4) Fetch Collection Dates
    🚚 Carrier API->>🤖 Gluey AI: (5) Return Collection Dates
    🤖 Gluey AI->>🏭 Customer: (6) Return Collection Dates
    🏭 Customer->>👤 User: (7) Show Available Collection Dates
    👤 User->>🏭 Customer: (8) Select Collection Date
    🏭 Customer->>🤖 Gluey AI: (9) POST: Book Collection (/shipments/{id}/collections/{collect_id}/time/{time_id})
    🤖 Gluey AI->>🚚 Carrier API: (10) Book Collection Date
    🚚 Carrier API->>🤖 Gluey AI: (11) Return Booking Result
    🤖 Gluey AI->>🏭 Customer: (12) Return Booking Result
    alt (13) Payment redirect
        Note over 👤 User, 🏭 Customer: (Optional) Consumer pays for return
        🏭 Customer->>👤 User: (13.1) Notify of payment redirect
        👤 User->>💳 Payment Provider: (13.2) Pay for collection
    end
~~~

### Explanation of steps

1. **POST: Create Shipment** - The first step is to create a shipment in Gluey. This can be done in two different ways, either with our asynchronous pattern or our synchronous one.
    - **Endpoint:** [Async](https://developer.gluey.ai/async-labels)
    - **Endpoint:** [Sync](https://developer.gluey.ai/sync-labels)
2. **Shipment ID** - Gluey returns a shipment ID, which is needed for further processing.
3. **Request Available Collection Dates (/shipments/{id}/collections)** - Using the shipment reference, you call our endpoint to request available collection dates and times.
    - **Endpoint:** [Request Collection Dates](https://developer.gluey.ai/api-book#operation/request_collection_dates_shipments__id__collection_post)
4. **Fetch Collection Dates** - Gluey calls the carrier in the background to fetch the available collection dates and times.
5. **Return Collection Dates** - The carrier returns the available collection dates and times to Gluey.
6. **Return Collection Dates** - Gluey returns the available collection dates and times to you, the customer.
7. **Show Available Collection Dates** - The customer provides the available collection dates to the user.
8. **Select Collection Date** - The user selects the date, time, or time window that suits them.
9. **POST: Book Collection (/shipments/{id}/collections/{collect_id}/time/{time_id})** - The customer sends the selected date, time, or time window to Gluey.
    - **Endpoint:** [Book Collection](https://developer.gluey.ai/api-book#operation/book_collection_shipments__id__collection__collection_id__time__time_id__post)
10. **Book Collection Date** - Gluey books the selected date and time with the carrier.
11. **Return Booking Result** - The carrier returns the booking result to Gluey.
12. **Return Booking Result** - Gluey returns the booking result to you.
13. **Payment Redirect** - If the selected collection date and time incurs additional charges:
    1. **Notify of Payment Redirect** - The customer notifies the user of the payment redirect.
    2. **Pay for Collection** - The user pays for the collection through the payment provider.