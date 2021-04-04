import flask
from datetime import datetime
import time
from kafka import KafkaProducer
import json

app = flask.Flask(__name__)
bootstrap_server = ['localhost:9092']
topic_name = 'kartaca'
producer = KafkaProducer(bootstrap_servers= bootstrap_server)

@app.route('/get', methods = ['GET'])
def get():
    start = time.clock()
    file = open("ozet.log","a")
    now = datetime.now()
    timestamp = str(int(datetime.timestamp(now)))
    request_time = (time.clock() - start)*1000.0
    request_time = str(round(request_time,4))
    global producer
    global topic_name
    message = "GET,"+request_time+","+timestamp+"\n"
    kafka_message = {
  "metot_tipi": "GET",
  "istek_cevaplama_ms": str(request_time),
  "timestamp": str(timestamp)
}
    producer.send(topic_name, json.dumps(kafka_message).encode('utf-8'))
    file.write(message)
    file.close()
    return ""
@app.route('/post', methods = ['POST'])
def post():
    start = time.clock()
    file = open("ozet.log","a")
    now = datetime.now()
    timestamp = str(int(datetime.timestamp(now)))
    request_time = (time.clock() - start)*1000.0
    request_time = str(round(request_time,4))
    message = "POST,"+request_time+","+timestamp+"\n"
    kafka_message = {
        "metot_tipi": "POST",
        "istek_cevaplama_ms": str(request_time),
        "timestamp": str(timestamp)
    }
    producer.send(topic_name, json.dumps(kafka_message).encode('utf-8'))
    file.write(message)
    file.close()
    return ""
@app.route('/put', methods = ['PUT'])
def put():
    start = time.clock()
    file = open("ozet.log","a")
    now = datetime.now()
    timestamp = str(int(datetime.timestamp(now)))
    request_time = (time.clock() - start)*1000.0
    request_time = str(round(request_time,4))
    message = "PUT,"+request_time+","+timestamp+"\n"
    kafka_message = {
        "metot_tipi": "PUT",
        "istek_cevaplama_ms": str(request_time),
        "timestamp": str(timestamp)
    }
    producer.send(topic_name, json.dumps(kafka_message).encode('utf-8'))
    file.write(message)
    file.close()
    return ""
@app.route('/delete', methods = ['DELETE'])
def delete():
    start = time.clock()
    file = open("ozet.log","a")
    now = datetime.now()
    timestamp = str(int(datetime.timestamp(now)))
    request_time = (time.clock() - start)*1000.0
    request_time = str(round(request_time,4))
    message = "DELETE,"+request_time+","+timestamp+"\n"
    kafka_message = {
        "metot_tipi": "DELETE",
        "istek_cevaplama_ms": str(request_time),
        "timestamp": str(timestamp)
    }
    producer.send(topic_name, json.dumps(kafka_message).encode('utf-8'))
    file.write(message)
    file.close()
    return ""
app.run()
