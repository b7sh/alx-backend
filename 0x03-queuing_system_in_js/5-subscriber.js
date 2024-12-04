import redis from 'redis'


const client = redis.createClient()
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', err => console.log(`Redis client not connected to the server: ${err.message}`));

const CHANNEL = 'holberton school channel';

client.subscribe(CHANNEL);

client.on('message', (channel, message) => {
  if (channel === CHANNEL) {
    console.log(message);
  }
  if (message === 'KILL_SERVER') {
    client.unsubscribe(CHANNEL);
    client.quit();
  }
});
