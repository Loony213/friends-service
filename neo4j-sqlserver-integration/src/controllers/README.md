
# Event Emitter Overview 📡

The **controllers** folder includes the `eventEmitter.js` file, which is responsible for handling custom events within the application. Specifically, it manages the `addFriend` event, which is emitted whenever a new friend is added, triggering the necessary actions in the system.

## Purpose 🎯
The **eventEmitter.js** file defines the custom event listener for the `addFriend` event. When the event is emitted, it logs the action of adding a friend and then calls the `createFriendship` method from the Neo4j model to establish the relationship between the two users in the Neo4j database.

The **eventEmitter.js** ensures that the process of adding a friend is handled asynchronously and efficiently by decoupling the business logic from the event triggers.

## Functionality 🔧
- **Event Listener**: The file listens for the `addFriend` event, which contains the necessary data to add a new friendship (e.g., `userId`, `friendId`, and the date the friendship was created).
- **Database Integration**: When the event is triggered, the service interacts with the **Neo4j** model to create the relationship between the users in the graph database.
- **Event Emission**: The `addFriend` function emits the `addFriend` event, which triggers the event listener and initiates the database operation.

This file ensures that the system's response to adding a friend is handled asynchronously and allows for better separation of concerns between different parts of the application.

## Features ✨
- **Event-driven Design**: Uses custom events to trigger specific actions within the application, making the system more modular and responsive.
- **Asynchronous Operations**: The event handler performs database operations asynchronously, ensuring non-blocking execution.
- **Integration with Neo4j**: It integrates with the **Neo4j** database to create relationships based on the emitted events.

The **eventEmitter.js** file plays a vital role in enabling an event-driven architecture, making the process of adding friends seamless and efficient within the **Friends Service** domain.
