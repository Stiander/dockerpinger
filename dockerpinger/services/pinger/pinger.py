from kafka import KafkaConsumer
from kafka import KafkaProducer
import time
import os
import json

print('Pinger Demo 1.0')

kafka_url = str(os.environ['KAFKA_URL'])
kafka_port = int(os.environ['KAFKA_PORT'])
kafka_address = kafka_url + ':' + str(kafka_port)
consumer = None

while True:
	try:
		consumer = KafkaConsumer(
			'pongs',
			bootstrap_servers=kafka_address,
			group_id='pingers')
		break
	except Exception:
		time.sleep(1)

producer = KafkaProducer(
	value_serializer=lambda v: json.dumps(v).encode('utf-8'),
	bootstrap_servers=kafka_address)
	
time.sleep(2)
producer.send('pings', {'message' : 'This is a ping!'})
time.sleep(1)

print('Waiting for messages')
for msg in consumer:
	time.sleep(1)
	print('Received ' + str(msg.value))
	print('Writing Ping!')
	producer.send('pings', {'message' : 'This is a ping!'})