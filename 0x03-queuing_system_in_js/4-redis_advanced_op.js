import redis from 'redis'


const client = redis.createClient()
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', err => console.log(`Redis client not connected to the server: ${err.message}`));

const KEYHASH = 'HolbertonSchools';

const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

keys.forEach((key, index) => {
  client.hset(KEYHASH, key, values[index], redis.print)
})

client.hgetall(KEYHASH, (error, value) => {
  console.log(value);
});
