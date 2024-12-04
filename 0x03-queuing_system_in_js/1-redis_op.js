import redis from 'redis'


const client = redis.createClient()
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', err => console.log(`Redis client not connected to the server: ${err.message}`));

async function setNewSchool(schoolName, value) {
  await client.set(schoolName, value, redis.print)
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, res) => console.log(res));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
