
# Add Friend Service Overview 🤝

The **services** folder contains the business logic for the Friends Service domain. Specifically, the `add_friend_service.py` file contains the logic for adding a friend to a user's network, which is triggered when a user sends a request to add another user as a friend.

## Purpose 🎯
The **add_friend_service.py** service is responsible for handling the core business logic related to adding friends. It connects to the database to verify the existence of both users involved in the friend request and then performs the operation to establish a friendship between them.

This service ensures that the friend request is processed correctly and that the users' data is updated in the database accordingly.

## Functionality 🔧
- **Database Connection**: Establishes a connection to the SQL Server database using the provided connection string.
- **User Validation**: Verifies that both users involved in the friend request exist in the database.
- **Friendship Creation**: If both users exist, the service creates a new record in the `friends` table, representing the friendship.
- **Error Handling**: If either user does not exist, an HTTP exception is raised with a 404 status code and an error message.

This service is the core component responsible for handling the logic of adding friends, making sure that all necessary checks are performed before modifying the database.

## Features ✨
- **Database Integration**: Interacts with a SQL Server database to store friendship data.
- **User Validation**: Ensures that both users involved in the friend request exist before proceeding.
- **Efficient Error Handling**: Catches errors such as non-existent users and raises appropriate HTTP exceptions.

This service is crucial for ensuring that friendships are added securely and correctly within the **Friends Service** domain.
