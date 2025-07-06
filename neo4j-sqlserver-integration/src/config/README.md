
# Config Folder Overview ⚙️

The **config** folder contains the configuration files used by the application to define and manage various settings. Specifically, the `config.js` file is used to configure the application's connection settings for both SQL Server and Neo4j.

## Purpose 🎯
The **config.js** file provides all necessary configuration parameters for the application to interact with both SQL Server (used for relational data storage) and Neo4j (used for graph-based data storage).

This file ensures that the application has the right settings to connect to the databases and properly perform required operations. It acts as a central place to configure connection strings, authentication credentials, and connection options.

## Functionality 🔧
- **SQL Server Configuration**: Provides settings for connecting to a SQL Server database, including authentication credentials and options for encryption and certificate trust.
- **Neo4j Configuration**: Configures the connection details for interacting with a Neo4j database, including the URI, username, and password.

This file allows the application to interact seamlessly with both the SQL Server and Neo4j databases by centralizing the connection configurations.

## Features ✨
- **SQL Server Integration**: Allows the application to communicate with SQL Server for relational data storage and retrieval.
- **Neo4j Integration**: Configures connection details for interacting with Neo4j, enabling graph-based data modeling and queries.
- **Centralized Configuration**: Keeps all the necessary database connection settings in one place, making it easy to manage and update them.

The **config** folder is crucial for setting up and managing the database configurations for the application, ensuring that the application can connect to both SQL Server and Neo4j databases correctly.
