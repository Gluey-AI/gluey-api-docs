# Gluey API Docs
## Getting started
The Gluey API provides a set of endpoints for developers to perform labeling, manifesting,  tracking and fetching pudo points for parcel carriers. This documentation serves as a guide for integrate your application with the Gluey API.

The deployed docs can be found at [https://developer.gluey.ai](https://developer.gluey.ai) and we recommend that you have a look there to understand integration patterns and endpoints better. 

## Project Structure

├── app <br>
│   ├── main.py <br>
│   ├── api <br>
│   │   ├── v1 <br>
│   │   │   ├── label <br>
│   │   │   ├── manifest <br>
│   │   │   ├── pudo <br>
│   │   │   ├── tracking <br>
├── requirements.txt <br>
└── README.md <br>

In the folders `label`,`manifest`,`pudo`,`tracking` you can find the endpoints including request / response models.


## Authentication
To access the Gluey API, developers need to authenticate their requests using an API key. An API key can be obtained by emailing `engineering@gluey.ai`

You need two things:

* **x-key** - an api key to include in the header and which authenticate you in the APIs.
* **account_number** - your account ID which you need when you subscribe to our webhooks.

## Environments
Gluey are using two environments:

**Sandbox (Test)**
```
https://api-sandbox.gluey.ai
```

**Production**
```
https://api.gluey.ai
```

## Feedback
Feel free to make suggestions on how we can improve our API endpoints by creating a pull request, issue or email us at `engineering@gluey.ai`