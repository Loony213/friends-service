
# Add Friend Microservice

## Overview

This microservice is responsible for handling friend requests between users. It allows users to send friend requests to others, and the server will process and store the data in a relational database.

This service is built with **Python**, leveraging the **Flask** framework to handle HTTP requests and provide RESTful APIs.

### Technologies Used:
- **Python**: Programming language.
- **Flask**: A lightweight WSGI web application framework in Python.
- **SQLServer**: ORM for database interaction.
- **Docker**: Containerization of the microservice.

## Architecture

This microservice follows a **Microservices** architecture, where each service is responsible for a single business function and can scale independently.

The service communicates with the database using SQLAlchemy ORM, and REST API endpoints allow interaction with the service.

- **Service Layer**: Contains the business logic for processing the friend requests.
- **Controller Layer**: Defines API endpoints that users interact with.
- **Model Layer**: Contains the database models and interactions.
- **API Layer**: Handles all the requests, validates, and maps them to the appropriate service functions.

### Architecture Principles
- **SOLID Principles**: Each module adheres to the SOLID principles, ensuring high maintainability and scalability.
- **DRY Principle**: We ensure code reusability by encapsulating repeated logic into reusable functions and services.
- **KISS Principle**: The code is kept simple, following best practices for clear and understandable code.

## Features

- **Add Friend**: Users can send friend requests.
- **Accept Friend Request**: Option to accept or reject incoming friend requests.
- **Retrieve Friends List**: Fetch the list of friends for the authenticated user.

## Patterns Used

- **MVC Pattern**: The microservice follows the Model-View-Controller pattern, separating the logic into:
    - **Model**: Handles all interactions with the database.
    - **View**: Represents the REST API that users interact with.
    - **Controller**: Contains the logic for business operations (e.g., adding friends, processing requests).

- **Singleton Pattern**: Used for initializing the database connection and ensuring a single instance of the connection is used across the service.

## Installation and Setup

### Prerequisites
- **Docker**: To containerize the microservice.
- **Python 3.x**: Ensure Python 3.x is installed on your system.
- **PostgreSQL**: A running PostgreSQL database (this can be configured via Docker).

### Steps to Run the Microservice:

1. Clone the repository:
   ```bash
   git clone 
   cd add_friend
   ```

2. Set up the virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database:
   Ensure your `friend_request.py` model is configured to use a PostgreSQL database or configure it as per your database connection.

5. To run the service locally:
   ```bash
   python app.py
   ```

6. Alternatively, you can use Docker:
   ```bash
   docker build -t add_friend_microservice .
   docker run -d -p 5000:5000 add_friend_microservice
   ```

## API Documentation

### Endpoint: `/add-friend`
- **Method**: `POST`
- **Description**: Adds a new friend to the user's friend list.
- **Request Body**:
   ```json
   {
     "user_email": "user@example.com",
     "friend_email": "friend@example.com"
   }
   ```
- **Response**:
   - **Success**: 
     ```json
     {
       "message": "Friend added successfully"
     }
     ```
   - **Error**:
     ```json
     {
       "error": "User not found"
     }
     ```

### Endpoint: `/get-friends`
- **Method**: `GET`
- **Description**: Retrieves the list of friends for the authenticated user.
- **Response**:
   ```json
   {
     "friends": [
       {"email": "friend1@example.com"},
       {"email": "friend2@example.com"}
     ]
   }
   ```

## Dockerizing the Microservice

To run this microservice inside a Docker container:

1. Build the Docker image:
   ```bash
   docker build -t add_friend_microservice .
   ```

2. Run the Docker container:
   ```bash
   docker run -d -p 5000:5000 add_friend_microservice
   ```



