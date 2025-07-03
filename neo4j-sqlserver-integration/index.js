// index.js
const { getFriends } = require('./src/models/db');
const { addFriend } = require('./src/controllers/eventEmitter');

async function main() {
  try {

    const friends = await getFriends();

    friends.forEach(friend => {
   
      if (friend.datee && !isNaN(Date.parse(friend.datee))) {
        addFriend(friend.user_id, friend.friend_id, friend.datee);
      } else {
        console.log(`Fecha inválida para el usuario ${friend.user_id}`);
      }
    });
  } catch (error) {
    console.error("Error al obtener amigos:", error);
  }
}

main();
