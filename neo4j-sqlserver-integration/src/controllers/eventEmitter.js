// src/eventEmitter.js
const EventEmitter = require('events');
const eventEmitter = new EventEmitter();
const { createFriendship } = require('../models/neo4j');

eventEmitter.on('addFriend', async (userId, friendId, date) => {
  console.log(`Evento: Se ha agregado un amigo. Usuario: ${userId}, Amigo: ${friendId}, Fecha: ${date}`);

  await createFriendship(userId, friendId, date);
});

function addFriend(userId, friendId, date) {
  eventEmitter.emit('addFriend', userId, friendId, date);
}

module.exports = { addFriend };
