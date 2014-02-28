# coding: utf-8
import json
import redis

def handle_websocket(ws, group):
    channel = 'pps-'+group
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    conn_pool = redis.client.ConnectionPool()
    sub = redis.client.PubSub(conn_pool)
    sub.subscribe(channel)
    import time
    t = int(time.time())
    for msg in sub.listen():
        j = int(time.time()) - t
        if msg['type'] == 'message' and msg['channel'] == channel:
            c = json.loads(msg['data'])
            for i in c:
                ws.send("%s %s %s \n" % (i, j, c[i]))
