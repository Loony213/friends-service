// src/db.js
const sql = require('mssql');
const { sqlConfig } = require('../config/config');

async function getFriends() {
  try {
    await sql.connect(sqlConfig);
    const result = await sql.query`SELECT user_id, friend_id, datee FROM friends`;
    return result.recordset;  
  } catch (err) {
    console.error('Error en la consulta de SQL Server:', err);
  } finally {
    sql.close();
  }
}

module.exports = { getFriends };
