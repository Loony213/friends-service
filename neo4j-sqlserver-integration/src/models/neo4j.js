// src/neo4j.js
const neo4j = require('neo4j-driver');
const { neo4jConfig } = require('../config/config');

const driver = neo4j.driver(neo4jConfig.uri, neo4j.auth.basic(neo4jConfig.username, neo4jConfig.password));
const session = driver.session();

async function createFriendship(userId, friendId, date) {
  if (!date) {
    console.error('Error: La fecha de amistad no es válida.');
    return;  
  }

  const isoDate = new Date(date).toISOString(); 

  const tx = session.beginTransaction(); 

  try {
    await tx.run(
      'MERGE (u:User {id: $userId}) ' +
      'MERGE (f:User {id: $friendId}) ' +
      'MERGE (u)-[:FRIENDS_WITH {since: $date}]->(f)',
      { userId, friendId, date: isoDate }
    );
    await tx.commit();  
    console.log(`Relación de amistad insertada entre ${userId} y ${friendId}`);
  } catch (error) {
    console.error('Error al insertar relación en Neo4j:', error);
    await tx.rollback(); 
  } finally {
    session.close();  
  }
}

module.exports = { createFriendship };
