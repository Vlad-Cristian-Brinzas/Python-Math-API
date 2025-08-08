from time import sleep
from kafka import KafkaConsumer
from shared.models import OperationRecord
from persistence import setup_database, log_api_call


print("Setting up database...")
setup_database()


print("Setting up Kafka consumer...")
consumer = None
for attempt in range(30):
    try:
        consumer = KafkaConsumer(
            'math_api_logging',
            bootstrap_servers='kafka:9092',
            # If restarting, read only new messages
            auto_offset_reset='latest',
            # Consumer group, to continue from where we left off
            group_id='math_api_consumer_group',
        )
        print("Kafka consumer established.")
        break  # Exit loop if connection is successful
    except Exception:
        print(f"Attempt {attempt + 1}: Failed to connect to Kafka")
        print("Trying again in 3 seconds...")
        sleep(3)
if not consumer:
    raise Exception("Failed to connect to Kafka after 30 attempts.")


print("Listening for messages from Kafka...")
for message in consumer:
    decoded_message = message.value.decode('utf-8')
    record = OperationRecord.model_validate_json(decoded_message)
    log_api_call(record)
    print(f"DEBUG: Received {record} from Kafka as {message}")
