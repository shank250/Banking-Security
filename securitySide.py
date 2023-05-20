import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
def branchLocation():
    url = f'https://www.google.com/maps/search/?api=1&query={lat},{long}'
    webbrowser.register('firefox',
            None,
            webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
    webbrowser.get('firefox').open(url)

def check_for_new_files(directory):
    files = os.listdir(directory)  # Get the list of files in the directory
    new_files = []
    dest_dir = 'G:\\My Drive\\banking'
    file_path = dest_dir + 'data.json'
    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
