
# Neo4j Model Overview 📚

The **models** folder contains the core data models used in the application. The `neo4j.js` model is responsible for interacting with the Neo4j graph database to handle operations related to friendships. Specifically, it defines the logic for creating and managing friendships between users in the graph database.

## Purpose 🎯
The **neo4j.js** model contains the logic for creating relationships between users in the Neo4j database. It uses Neo4j's graph database structure to model friendships as **FRIENDS_WITH** relationships. This model is an essential part of the **Friends Service**, ensuring that the friendships are correctly represented in a graph database.

## Functionality 🔧
- **Graph Database Integration**: This model connects to the Neo4j database to insert and manage relationships between users.
- **Create Friendship**: It defines a function, `createFriendship`, that takes user IDs, a friend's ID, and the date of the friendship, and inserts them as a **FRIENDS_WITH** relationship in the Neo4j graph.
- **Transaction Handling**: The model ensures that the operation is handled within a Neo4j transaction, ensuring the integrity and consistency of the database.
- **Date Handling**: It ensures that the date of the friendship is valid and converts it into the ISO 8601 format before inserting it into the database.

This model plays a critical role in maintaining and managing the relationships (friendships) between users in the **Friends Service** domain.

## Features ✨
- **Friendship Relationship**: Creates a **FRIENDS_WITH** relationship between two users in Neo4j, storing the date the friendship was established.
- **Transaction Management**: Handles database operations within a transaction to ensure consistency.
- **Data Validation**: Ensures that the provided date is valid and correctly formatted before inserting the friendship relationship.

The **neo4j.js** model is fundamental in enabling the graph-based representation of relationships, providing efficient and scalable ways to manage friendships in the **Friends Service** domain.
