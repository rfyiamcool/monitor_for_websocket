#!/usr/bin/python
#coding=utf-8

import config
import socket
import traceback
import struct
#import utils
import time
import redis
from redis.exception import ConnectionError
from logger import logger


#r = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=config.REDIS_DB)
r = redis.StrictRedis(host="127.0.0.1", port=6379)


for i in xrange(1, 10000):
    import random
    import json
    #result.append('%s|%s' % (ip, pps))
    x = {}
    for i in config.group1:
        x[i] = random.random() * random.random() * 10000
    r.publish('pps-group1', json.dumps(x))
    for i in config.group2:
        x[i] = random.random() * random.random() * 10000
    r.publish('pps-group2', json.dumps(x))
    for i in config.group3:
        x[i] = random.random() * random.random() * 10000
    r.publish('pps-group3', json.dumps(x))
    time.sleep(1)
