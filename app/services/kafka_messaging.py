from time import sleep
from kafka import KafkaProducer
from shared.models import OperationRecord

print("Setting up Kafka connection...")
producer = None
for attempt in range(30):
    try:
        producer = KafkaProducer(
            bootstrap_servers='kafka:9092',
        )
        print("Kafka connection established.")
        break  # Exit loop if connection is successful
    except Exception:
        print(f"Attempt {attempt + 1}: Failed to connect to Kafka")
        print("Trying again in 3 seconds...")
        sleep(3)
if not producer:
    raise Exception("Failed to connect to Kafka after 30 attempts.")


def send_operation_record(record: OperationRecord):
    """
    Sends an OperationRecord to the Kafka topic 'math_api_logging'.

    :param record: The OperationRecord to send.
    """
    message = record.model_dump_json().encode('utf-8')
    producer.send('math_api_logging', value=message)
    producer.flush()
    print(f"DEBUG: Sent {record} via Kafka as {message}")
