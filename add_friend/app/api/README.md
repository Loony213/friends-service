
# Add Friend API Overview 🤝

The **api** folder contains the API logic for managing friend requests in the Friends Service. Specifically, the `add_friend_api.py` handles the API endpoint for adding a friend to a user's network.

## Purpose 🎯
The **add_friend_api.py** defines a POST API endpoint `/add-friend`, where users can send a request to add another user as a friend. The request data contains the emails of the user and the friend they wish to add. The API interacts with the underlying business logic to process this request and return the appropriate result.

This API is a part of the larger **Friends Service** and acts as the interface through which users can initiate friend requests and add new friends.

## Functionality 🔧
- **Endpoint**: The API listens for POST requests to the `/add-friend` endpoint.
- **Input Validation**: It receives and validates the request data, which includes the emails of the user and the friend to be added.
- **Service Interaction**: The API interacts with the **add_friend_service** to process the logic of adding a friend, which includes checking for existing relationships and performing the necessary actions.
- **Response**: After processing the request, the API returns the result from the `add_friend` service, indicating whether the friend was successfully added or an error occurred.

This API endpoint ensures that the friend request is processed efficiently and provides a clear response for the client.

## Features ✨
- **Add Friend**: Allows users to send a request to add a friend by providing their email and the email of the friend.
- **Service Integration**: Communicates with the **add_friend_service** to handle the core logic of adding a friend.

This API serves as the main interface for adding friends within the **Friends Service** domain.
