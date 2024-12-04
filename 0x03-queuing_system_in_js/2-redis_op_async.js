import redis from 'redis'
import { promisify } from 'util'


const client = redis.createClient()
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', err => console.log(`Redis client not connected to the server: ${err.message}`));

const addAsync = promisify(client.get).bind(client);

async function setNewSchool(schoolName, value) {
  await client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  await client.get(schoolName, (err, res) => console.log(res));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
