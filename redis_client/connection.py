from redis import Redis
from redis.exceptions import ConnectionError
#from os import getenv

try: 
    redis_client = Redis(
        
        host= 'us1-advanced-seagull-38266.upstash.io',
        port= '38266',
        password= "334f4150403b4d37a6938d6ab9e65c8a",
    )

    print("Connected to redis")
except ConnectionError as e:
    print(e)

