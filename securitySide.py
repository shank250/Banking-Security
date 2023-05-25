# for the branch manager

import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import json
from datetime import datetime
def branchLocation(lat,long):
    url = f'https://www.google.com/maps/search/?api=1&query={lat},{long}'
    webbrowser.register('firefox',
            None,
            webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
    webbrowser.get('firefox').open(url)

def check_for_new_files(directory):
    with open("C:","r") as rf:
        data= json.load(rf)
    filename="data.json"
    while True:
        if os.path.isfile(os.path.join(directory, filename)):
            print("file found")
            break
        # time.sleep(1)
        # print("not get")
directory = "C:\\data.json"
# directory= r"Z:\Banking--main\Banking--main\Banking--main\output"
check_for_new_files(directory)
# branchLocation()

import threading

# Function to handle user prompt
def handle_user_prompt():
    global user_response
    user_response = input("Seems to be a bank robbery continue with SOS [y/n]: ")

# Start the user prompt in a separate thread
prompt_thread = threading.Thread(target=handle_user_prompt)
prompt_thread.start()

# Wait for the user response or timeout
prompt_thread.join(timeout=120)  # Timeout set to 2 minutes

# Check if the prompt thread is still alive
if prompt_thread.is_alive():
    print("No reply. SOS initiated.")
    with open("C:\\data.json","r") as rf:
        data= json.load(rf)
    print(data['lat'])
    print(data['long'])
    branchLocation(data['lat'],data['long'])
else:
    print("User response:", user_response)
    # Continue the program based on the user response
    if user_response.lower() == 'y':
        print("Program continues...")
        print("SOS initiated.")
        with open("C:\\data.json","r") as rf:
            data= json.load(rf)
        print(data['lat'])
        print(data['long'])
        branchLocation(data['lat'],data['long'])

    elif user_response.lower() == 'n':
        print("Program stops...")
    else:
        print("Invalid response. Program continues...")

# Continue with the rest of the program
# a = input("Seems to be a bank robbery continue with SOS [y/n]")
