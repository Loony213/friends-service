// src/neo4j.js
const neo4j = require('neo4j-driver');
const { neo4jConfig } = require('../config/config');

// Función para insertar relaciones de amistad en Neo4j dentro de una transacción
async function createFriendship(userId, friendId, date) {
  // Validar que la fecha no sea nula y convertirla a formato ISO 8601
  if (!date) {
    console.error('Error: La fecha de amistad no es válida.');
    return;  // No proceder si la fecha es null o inválida
  }

  // Asegurarse de que la fecha esté en el formato adecuado (ISO 8601)
  const isoDate = new Date(date).toISOString(); // Convertir a string ISO 8601

  const driver = neo4j.driver(neo4jConfig.uri, neo4j.auth.basic(neo4jConfig.username, neo4jConfig.password));
  const session = driver.session();  // Crear una nueva sesión para cada transacción

  try {
    await session.run(
      'MERGE (u:User {id: $userId}) ' +
      'MERGE (f:User {id: $friendId}) ' +
      'MERGE (u)-[:FRIENDS_WITH {since: $date}]->(f)',
      { userId, friendId, date: isoDate }
    );
    console.log(`Relación de amistad insertada entre ${userId} y ${friendId}`);
  } catch (error) {
    console.error('Error al insertar relación en Neo4j:', error);
  } finally {
    await session.close();  // Cerrar la sesión después de cada operación
  }
}

module.exports = { createFriendship };