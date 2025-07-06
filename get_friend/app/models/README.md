
# Friend Request Model Overview 📄

The **models** folder defines the data models used within the **Friends Service** domain. The `friend_request.py` model defines the structure of the data related to a friend request. This model ensures that the data provided for adding a friend is correctly structured and validated.

## Purpose 🎯
The **friend_request.py** model is used to define the structure of a friend request, including the necessary fields such as `user_email` and `friend_email`. It is responsible for validating the input data for adding a friend to the user's network.

By using **Pydantic**, the model ensures that the data passed through the API is in the correct format and follows the required schema.

## Functionality 🔧
- **Data Structure**: Defines the data structure for a friend request, which includes the email addresses of both the user and the friend they want to add.
- **Input Validation**: Ensures that the provided data is valid, including checking for the correct data types and ensuring the emails are provided.
- **Integration**: This model is used throughout the service to ensure that data passed through the API is consistent and valid.

The **FriendRequest** model provides a clear and structured way of handling the data needed to add a friend, ensuring that the system can process requests correctly and securely.

## Features ✨
- **Data Validation**: Automatically validates the input data to ensure that both email fields are present and valid.
- **Simple Structure**: The model uses **Pydantic** to define and enforce the structure, making it easy to maintain and extend.

This model is an essential part of the **Friends Service** domain, ensuring that all friend requests are handled with proper validation and structure.
