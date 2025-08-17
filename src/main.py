import os
import time
from fetch_api import api


def main():
    response = api("get_db", "your_api_key")
    print(response)

    pass




if __name__ == "__main__":
    main()
    print("Created with Copilot")