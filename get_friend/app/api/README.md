
# Friends API Overview 🤝

The **api** folder contains the API logic for managing friend-related requests in the Friends Service. Specifically, the `friends_api.py` defines the API endpoint for retrieving a list of a user's friends.

## Purpose 🎯
The **friends_api.py** file exposes a GET API endpoint `/friends/{email}`, where users can send a request to retrieve the list of friends associated with a specific email address. It communicates with the underlying business logic to fetch and return the friends of the user.

This API is part of the **Friends Service** and acts as the interface for fetching friends' information based on the provided email.

## Functionality 🔧
- **Endpoint**: The API listens for GET requests to the `/friends/{email}` endpoint.
- **Input**: The email of the user whose friends are to be fetched is passed as a URL parameter.
- **Service Interaction**: The API calls the **get_friends** service to retrieve the list of friends associated with the provided email.
- **Response**: The API returns a response containing the list of friends or an appropriate error message if something goes wrong.

This API ensures that users can securely retrieve their friends' data through a well-defined RESTful endpoint.

## Features ✨
- **Get Friends**: Allows users to send a request to get the list of their friends based on their email.
- **Service Integration**: Communicates with the **friends_service** to handle the core logic of fetching friends.

This API serves as the main interface for retrieving friends' data within the **Friends Service** domain.
