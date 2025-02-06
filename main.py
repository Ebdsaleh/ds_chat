# main.py
"""
This is the main entry point for the application.
requires to import requests and a Deepseek API key
"""
from src.core.cli import cli_instance


def main():
    cli_instance.run()


if __name__ == "__main__":
    main()
