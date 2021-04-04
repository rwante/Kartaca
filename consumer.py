from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads


bootstrap_server = ['localhost:9092']
mongo_server = 'localhost:27017'
consumer = KafkaConsumer('kartaca',bootstrap_servers=bootstrap_server
                         ,auto_offset_reset='earliest')
client = MongoClient(mongo_server)
db = client.kartaca
collection = db.kartaca
for message in consumer:
    print(message.value)
    message = message.value
    message = loads(message)
    collection.insert_one(message)