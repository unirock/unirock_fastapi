from faststream import FastStream
from faststream.redis import RedisBroker

broker = RedisBroker(host='localhost', port=6379, db=0)