
# Friends Service Logic Overview 🤝

The **services** folder contains the business logic of the Friends Service domain. Specifically, the `friends_service.py` file contains the logic for fetching the list of friends associated with a given user.

## Purpose 🎯
The **friends_service.py** service handles the core business logic for managing friends. It connects to the database to retrieve the list of friends for a given user, based on the user's email.

This service is essential for handling the logic related to retrieving and managing friendships within the **Friends Service** domain.

## Functionality 🔧
- **Database Connection**: Establishes a connection to the SQL Server database using the provided connection string.
- **User Validation**: Retrieves the user by email and validates if the user exists in the database.
- **Friendship Retrieval**: If the user exists, the service fetches the list of friends associated with that user by joining the `friends` and `users` tables.
- **Error Handling**: If the user does not exist, an HTTP exception is raised with a 404 status code, indicating that the user was not found.

This service is the core component responsible for retrieving a user's list of friends, making sure that all necessary checks are performed before returning the data.

## Features ✨
- **Database Integration**: Interacts with a SQL Server database to retrieve the list of friends.
- **User Validation**: Ensures that the user exists before attempting to fetch the list of friends.
- **Efficient Error Handling**: Catches errors such as non-existent users and raises appropriate HTTP exceptions.

This service is crucial for ensuring that friendship data is fetched securely and correctly within the **Friends Service** domain.
