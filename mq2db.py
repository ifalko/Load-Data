s__author__ = 'falko'

from pymongo import MongoClient
import pika
import json

client = MongoClient()
db = client.data

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='iFalko')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    json_obj = json.loads(body)
    db.stackoverdb.insert_one(json_obj)

channel.basic_consume(callback,
                      queue='iFalko',
                      no_ack=True)

channel.start_consuming()
