#!/usr/bin/env python3

import os
import json
import openai
import requests
from dotenv import load_dotenv

load_dotenv()


openai.organization = "org-SOiwnRT1gkRHkbx9s7KazzKl"
api_key = os.environ.get("OPENAI_API_KEY")
openai.api_key = api_key

ENDPOINT = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{
        "role": "user",
        "content": "Hello!"
    }]
}

response = requests.post(ENDPOINT, data=json.dumps(data), headers=headers, timeout=10)

# Get completion text from response
completion_text = response.json()

# Print completion text
print(completion_text)
