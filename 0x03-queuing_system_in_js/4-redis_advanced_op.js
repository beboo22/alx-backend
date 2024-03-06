#!/usr/bin/node
import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
function print (err, reply) {
  console.log(`Reply: ${reply}`);
}
client
  .MULTI()
  .hset('HolbertonSchools', 'Portland', 50, print)
  .hset('HolbertonSchools', 'Seattle', 80, print)
  .hset('HolbertonSchools', 'New York', 20, print)
  .hset('HolbertonSchools', 'Bogota', 20, print)
  .hset('HolbertonSchools', 'Cali', 40, print)
  .hset('HolbertonSchools', 'Paris', 2, print)
  .EXEC();
client.HGETALL('HolbertonSchools', (err, hashset) => {
  console.log(hashset);
});
