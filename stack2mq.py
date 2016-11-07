s__author__ = 'falko'

import stackexchange
from loadjson import *
from config import *
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)

'''
The API is rate-limited. The default rate limit,
if no key is provided, is 300 requests per day.
With an API key, however, this is bumped up to 10,000!
You can also then use StackApps to publicise your app.
'''
so = stackexchange.Site(stackexchange.StackOverflow, app_key=USER_API_KEY)
'''
Be aware, though, that even with an API key,
requests are limited to thirty per five seconds.
By default, the library will return an error
before even making an HTTP request if you'll go over this limit.
Alternatively, you can configure it such that
it will wait until it can make another request without returning an error.
To enable this behaviour. set the impose_throttling property
'''
so.impose_throttling = IMPOSE_THROTTLING
so.throttle_stop = THROTTLE_STOP

so.be_inclusive()

def send_to_rabbitMQ():
    cur = 0
    for question in so.questions(fromdate=FROM_DATE, todate=TO_DATE):
        json_obj = getJson(so, question)
        channel.basic_publish(exchange='',
                              routing_key=QUEUE_NAME,
                              body=json_obj)
        cur += 1
        if ( cur == 4500 ):
            break

def main():
    send_to_rabbitMQ()


if __name__ == "__main__":
    main()
