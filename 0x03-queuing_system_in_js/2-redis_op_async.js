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
  console.log(reply);
}

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, print);
}

function displaySchoolValue (schoolName) {
  client.get(schoolName, print);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
