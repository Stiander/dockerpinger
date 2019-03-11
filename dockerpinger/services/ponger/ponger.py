from kafka import KafkaConsumer
from kafka import KafkaProducer
import time
import os
import json

print('Ponger Demo 1.0')

kafka_url = str(os.environ['KAFKA_URL'])
kafka_port = int(os.environ['KAFKA_PORT'])
kafka_address = kafka_url + ':' + str(kafka_port)
consumer = None

while True:
	try:
		consumer = KafkaConsumer(
			'pings',
			bootstrap_servers=kafka_address,
			group_id='pongers')
		break
	except Exception:
		time.sleep(1)

producer = KafkaProducer(
	value_serializer=lambda v: json.dumps(v).encode('utf-8'),
	bootstrap_servers=kafka_address)

time.sleep(1)
producer.send('pongs', {'message' : 'This is a pong!'})

print('Waiting for messages')	
for msg in consumer:
	time.sleep(1)
	print('Received ' + str(msg.value))
	print('Writing Pong!')
	producer.send('pongs', {'message' : 'This is a pong!'})