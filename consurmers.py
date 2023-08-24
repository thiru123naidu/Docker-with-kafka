from kafka import KafkaConsumer
import json
consumer1=KafkaConsumer('bahubali',bootstrap_servers='localhost:29092')
print("hi")
print(consumer1)
for i in consumer1:
    print(json.loads(i.value))

