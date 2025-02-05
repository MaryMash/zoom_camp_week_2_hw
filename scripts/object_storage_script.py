import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# Replace with your Yandex Cloud credentials
AWS_ACCESS_KEY_ID = 'your-access-key-id'
AWS_SECRET_ACCESS_KEY = 'your-secret-access-key'
ENDPOINT_URL = 'https://storage.yandexcloud.net'

# Create a session and S3 client
session = boto3.session.Session()
s3_client = session.client(
    service_name='s3',
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def list_buckets():
    try:
        response = s3_client.list_buckets()
        print("Buckets:")
        for bucket in response.get('Buckets', []):
            print(f"- {bucket['Name']}")
    except NoCredentialsError:
        print("Error: Invalid credentials.")
    except ClientError as e:
        print(f"Client error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def insert_data(file_path, bucket_name, object_name):
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File '{file_path}' uploaded to '{bucket_name}/{object_name}' successfully.")
    except FileNotFoundError:
        print("The file was not found.")
    except NoCredentialsError:
        print("Credentials are not available.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    list_buckets()