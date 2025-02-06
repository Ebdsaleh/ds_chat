# src/core/cli.py
"""
This file is responsible for creating and maintaining the CLI
interface to chat with Deepseek AI
"""

import requests
API_KEY = ""
API_URL = "https://api.deepseek.com/v1/chat/completions"
class Cli:
    _instance = None
    def __new__(cls, *args, **kwargs):
        return cls._instance

    def call_deepseek_api(self, prompt):
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "deepseek-chat",  # Replace with the correct model name
            "messages": [{"role": "user", "content": prompt}]
        }
        response = requests.post(API_URL, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"Error: {response.status_code}, {response.text}"

    def run(self):
        print("Welcome to the DeepSeek CLI! Type 'exit' to quit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
            response = self.call_deepseek_api(user_input)
            print(f"DeepSeek: {response}")


cli_instance = Cli()
