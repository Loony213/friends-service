
# Friends Service Microservices 🤝

This repository is part of the **Friends Service** domain, which provides the configuration and logic for managing friend requests and relationships. It includes microservices that handle adding friends, retrieving friend lists, and creating relationships through graph-based models using Neo4j.

## Repository Link 📁
- [GitHub Repository](https://github.com/Loony213/friends-service)

## Microservices Overview 🚀
### 1. **Add Friend**
   - Purpose: Allows users to send friend requests and add friends to their network.

### 2. **Get Friend**
   - Purpose: Retrieves a list of a user's friends.

### 3. **Neo4j Integration**
   - Purpose: Uses Neo4j to create and manage relationships between users, representing friendships in a graph format.

## Architecture Style 🏗️
- **Microservice Architecture**: Each service operates independently and communicates via APIs, allowing for scalability and modularity.
- **Design Pattern**: The system follows the **Event-Driven Architecture** (EDA), where actions such as adding a friend or retrieving friends are treated as events, triggering responses in the system.

## Technologies 💻
- **Programming Language**: Python
- **Graph Database**: Neo4j for handling relationship-based data modeling
- **API Integration**: REST APIs for adding friends and retrieving friend lists
- **Containerization**: Docker for deploying microservices

## Project Structure 🧑‍💻
The repository is structured as follows:

```
friends-service/
├── .github/workflows/         # Contains GitHub Actions workflows for CI/CD.
│   └── new.yml                # Configuration for CI/CD pipelines.
│
├── add_friend/                # Microservice for adding friends.
│   └── requirements.txt       # Lists the dependencies for the add_friend service.
│
├── get_friend/                # Microservice for retrieving the list of friends.
│   └── requirements.txt       # Lists the dependencies for the get_friend service.
│
├── neo4j-sqlserver-integration/ # Microservice for integrating Neo4j with SQL Server.
│   └── requirements.txt       # Lists the dependencies for the Neo4j integration service.
│
├── README.md                  # This file.
└── requirements.txt           # Lists the global dependencies for the project.
```

### Folder Descriptions 📂
- **.github/workflows/**: Contains GitHub Actions configurations for CI/CD automation.
- **add_friend/**: The microservice that handles adding friends, including sending friend requests.
- **get_friend/**: The microservice that retrieves a list of a user's friends.
- **neo4j-sqlserver-integration/**: Handles the integration between Neo4j and SQL Server for managing friendship relationships in a graph-based structure.
- **requirements.txt**: Specifies the dependencies necessary for the microservices to function.

## How to Deploy ⚙️
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Loony213/friends-service.git
   ```

2. **Install Dependencies:**
   Navigate to each service folder (e.g., `add_friend/`, `get_friend/`, `neo4j-sqlserver-integration/`) and install the dependencies listed in their `requirements.txt`.

3. **Run the Microservices:**
   - After setting up the dependencies, you can start each microservice individually.
   - Example for running `add_friend` service:
     ```bash
     python app.py
     ```

4. **Docker Deployment:**
   - Build the Docker image for each microservice:
     ```bash
     docker build -t kamartinez/add_friend .
     docker build -t kamartinez/get_friend .
     docker build -t kamartinez/neo4j-sqlserver-integration .
     ```
   - Run the containers:
     ```bash
     docker run -p 5000:5000 kamartinez/add_friend
     docker run -p 5001:5000 kamartinez/get_friend
     docker run -p 5002:5000 kamartinez/neo4j
     ```

5. **Access the Services:**
   - The services will be accessible at `http://localhost:5000`, `http://localhost:5001`, and `http://localhost:5002` (or different ports depending on your configuration).

## Features ✨
- **Add Friend**: Enables users to send friend requests and add friends to their network.
- **Get Friend**: Retrieves the list of friends of a given user.
- **Graph-Based Relationship Management**: Uses Neo4j for efficient management of friendship relationships.
- **Modular and Scalable**: The services are modular, allowing for easy scalability and integration with other systems.

## License 📜
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
