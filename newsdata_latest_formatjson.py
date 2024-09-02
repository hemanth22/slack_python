from kafka import KafkaProducer
import six
import sys
if sys.version_info >= (3, 12, 0):
    sys.modules['kafka.vendor.six.moves'] = six.moves
import requests
import os
import json

# Kafka configuration
bootstrap_servers_sv1 = os.environ.get('BOOTSTRAP_SERVER_NAME')
sasl_mechanism_sv1 = os.environ.get('SASL_MECH')
security_protocol_sv1 = os.environ.get('SSL_SEC')
sasl_plain_username_sv1 = os.environ.get('SASL_USERNAME')
sasl_plain_password_sv1 = os.environ.get('SASL_PASSD')

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers_sv1,
    sasl_mechanism=sasl_mechanism_sv1,
    security_protocol=security_protocol_sv1,
    sasl_plain_username=sasl_plain_username_sv1,
    sasl_plain_password=sasl_plain_password_sv1,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic_name = 'news'

# Function to serialize data to JSON string
def serialize_data(data):
    """
    Serialize the given data to a JSON string.

    Args:
        data (dict): The data to serialize

    Returns:
        str: The serialized JSON string
    """
    return json.dumps(data)

NEWS_DATA_API = os.environ.get('NEWSDATA_API_KEY')
base_url = 'https://newsdata.io/api/1/latest'
queries = ['dbs', 'gold', 'deposits', 'mutual', 'dalal', 'sensex', 'nifty', 'gift', 'bank', 'crude', 'oil', 'fed', 'recession']

for query in queries:
    parameters = {
        'q': query,
        'apiKey': NEWS_DATA_API,
        'domainurl': 'news.google.com'
    }

    try:
        response = requests.get(base_url, params=parameters)
        if response.status_code == 200:
            news_data = response.json()
            if 'results' in news_data:
                for result in news_data['results']:
                    formatted_json = {
                        "source": "news",
                        "message": {
                            "title": result.get('title', 'no news'),
                            "description": result.get('description', 'no news'),
                            "source_id": result.get('source_id', 'unknown')
                        }
                    }
                    formatted_output = json.dumps(formatted_json, ensure_ascii=False, indent=4)
                    print(formatted_output)
                    # Produce JSON message to the Kafka topic
                    producer.send(topic_name, value=formatted_json)
                    print(f"Produced: {formatted_output}")
        else:
            print(f"Request failed with status code {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Ensure all messages are sent before closing
producer.flush()
producer.close()
