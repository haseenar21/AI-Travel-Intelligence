from urllib import response

import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WATSONX_API_KEY")
INSTANCE_URL = os.getenv("WATSONX_URL")
AGENT_ID = os.getenv("AGENT_ID")


def get_access_token():
    response = requests.post(
        "https://iam.cloud.ibm.com/identity/token",
        headers={
            "Content-Type": "application/x-www-form-urlencoded"
        },
        data={
            "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
            "apikey": API_KEY
        }
    )

    response.raise_for_status()

    return response.json()["access_token"]


def generate_trip(prompt):

    token = get_access_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "text/event-stream"
    }

    payload = {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    url = f"{INSTANCE_URL}/v1/orchestrate/{AGENT_ID}/chat/completions"

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        stream=True
    )
    print("Orchestrate Status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))

    answer = ""
    print("Receiving response...")
    for line in response.iter_lines():
        
        if line:
            print(line)

            line = line.decode("utf-8")

            if line.startswith("data: "):

                data = line[6:]

                if data == "[DONE]":
                    break

                try:
                    import json

                    chunk = json.loads(data)

                    if "choices" in chunk:

                        delta = chunk["choices"][0].get("delta", {})

                        if "content" in delta:
                            answer += delta["content"]

                except Exception:
                    pass

    return answer