from kafka import KafkaProducer
import json
import time
producer1= KafkaProducer(bootstrap_servers='localhost:29092')
topic="bahubali"


for i in range(10):
    data={
        f"msg{i}":"namasthe baahu"
    }
    producer1.send('bahubali',json.dumps(data).encode("utf-8"))
    print("Sending message successfully")
    time.sleep(2)




