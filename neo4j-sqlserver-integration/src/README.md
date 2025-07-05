
# Neo4j SQL Server Integration - Microservice

🚀 **Welcome to the Neo4j SQL Server Integration Microservice repository!** 🚀

This repository integrates **Neo4j** (a graph database) with **SQL Server**, providing the ability to manage and synchronize data across both databases. The service enables seamless querying and data interaction between SQL Server and Neo4j databases.

## 📂 Project Structure

```
neo4j-sqlserver-integration/
├── src/
│   ├── config/
│   │   └── config.js
│   ├── controllers/
│   │   └── eventEmitter.js
│   ├── models/
│   │   ├── db.js
│   │   └── neo4j.js
├── .dockerignore
├── Dockerfile
├── index.js
├── package-lock.json
├── package.json
└── README.md
```

## 🛠️ Technologies & Tools

- **Node.js**: JavaScript runtime for building server-side applications ⚙️
- **Neo4j**: Graph database for modeling complex relationships 🔗
- **SQL Server**: Relational database for structured data 💾
- **Docker**: Containerization tool for deployment 🐳
- **EventEmitter**: To handle asynchronous events in Node.js ⚡

## 🔗 Architecture

- **Style**: Microservice-based Architecture 🌍
- **Design Pattern**: 
  - **Singleton**: Used for initializing single instances for database connections.
  - **Observer**: Implemented via EventEmitter to handle custom events.
- **Databases**: Neo4j (Graph database) & SQL Server (Relational database) 💾

### Core Principles
- **Single Responsibility**: Each microservice performs a single task—integrating Neo4j and SQL Server.
- **Loose Coupling**: Independent database operations for Neo4j and SQL Server via APIs.
- **Scalability**: The microservice scales horizontally to handle larger datasets from both databases.

## 🧑‍💻 Running the Application

1. Clone this repository to your local machine:

```bash
git clone https://github.com/Loony213/neo4j-sqlserver-integration.git
cd neo4j-sqlserver-integration
```

2. Install dependencies:

```bash
npm install
```

3. To run the application locally:

```bash
node index.js
```

4. To run using Docker:

```bash
docker build -t neo4j-sqlserver-integration .
docker run -p 5000:5000 neo4j-sqlserver-integration
```

This will make your service available at `http://localhost:5000`.


## 🔧 Docker Configuration

The project includes a **Dockerfile** to build and run the service inside a container.

### Build the Docker image:

```bash
docker build -t neo4j-sqlserver-integration .
```

### Run the Docker container:

```bash
docker run -d -p 5000:5000 neo4j-sqlserver-integration
```

The service will be available on port `5000` inside the container.

## 📑 Requirements

- **Neo4j**: Graph database for managing complex relationships
- **SQL Server**: Relational database for storing structured data
- **Node.js**: JavaScript runtime environment
- **Express.js**: Web framework for creating APIs
- **EventEmitter**: Used for managing asynchronous operations in Node.js

## 🔒 Security Considerations

- **Authentication**: Implementing secure token-based authentication (JWT)
- **Authorization**: Users need valid credentials to perform data synchronization

## 🌍 DockerHub & Deployment

You can push this Docker image to DockerHub with your `kamartinez` account:

```bash
docker tag neo4j-sqlserver-integration kamartinez/neo4j-sqlserver-integration:latest
docker push kamartinez/neo4j-sqlserver-integration:latest
```

## 🔄 Contributing

Feel free to fork this repository, submit issues, and contribute to improving the integration!

---

**Author**: Kamartinez 🧑‍💻  

