// src/config.js

module.exports = {
  sqlConfig: {
    user: 'admin',
    password: 'Distribuida123',
    server: 'auth-db.cnck2sieyjue.us-east-1.rds.amazonaws.com', 
    database: 'auth_db',
    options: {
      encrypt: true,  
      trustServerCertificate: true,  
    }
  },

  neo4jConfig: {
    uri: 'bolt://100.29.132.85:7687',  
    username: 'neo4j',
    password: 'strongPassword123'
  }
};
