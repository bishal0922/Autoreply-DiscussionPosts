#!/usr/bin/env python3

import os
import openai
from dotenv import load_dotenv

load_dotenv()

print("Hello World!")

openai.organization = "org-SOiwnRT1gkRHkbx9s7KazzKl"
api_key = os.environ.get("OPENAI_API_KEY")
openai.api_key = api_key

print(openai.Model.list())
