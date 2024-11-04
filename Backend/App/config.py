from dotenv import load_dotenv
import os
from google.cloud import aiplatform_v1beta1
from google.oauth2 import service_account

# Load environment variables from `.env` file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")


# SERVICE_ACCOUNT_PATH=os.getenv("SERVICE_ACCOUNT_PATH")
# # Load Google Cloud credentials
# credentials = service_account.Credentials.from_service_account_file(
#     SERVICE_ACCOUNT_PATH  # Replace with actual path
# )

# # Set up the endpoint
# endpoint = "projects/YOUR_PROJECT_ID/locations/us-central1/publishers/google/models/gemini-embedding"
# endpoint= os.getenv("ENDPOINT")

# # Initialize the Google Cloud client with credentials and endpoint
# client = aiplatform_v1beta1.PredictionServiceClient(credentials=credentials)