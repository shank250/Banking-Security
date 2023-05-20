import subprocess as sp
import re
import time
import json
import os
import shutil
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
def branchLocation():
    wt = 5 # Wait time -- I purposefully make it wait before the shell command
    accuracy = 3 #Starting desired accuracy is fine and builds at x1.5 per loop

    # while True:
    time.sleep(wt)
    pshellcomm = ['powershell']
    pshellcomm.append('add-type -assemblyname system.device; '\
                        '$loc = new-object system.device.location.geocoordinatewatcher;'\
                        '$loc.start(); '\
                        'while(($loc.status -ne "Ready") -and ($loc.permission -ne "Denied")) '\
                        '{start-sleep -milliseconds 100}; '\
                        '$acc = %d; '\
                        'while($loc.position.location.horizontalaccuracy -gt $acc) '\
                        '{start-sleep -milliseconds 100; $acc = [math]::Round($acc*1.5)}; '\
                        '$loc.position.location.latitude; '\
                        '$loc.position.location.longitude; '\
                        '$loc.position.location.horizontalaccuracy; '\
                        '$loc.stop()' %(accuracy))

        #Remove >>> $acc = [math]::Round($acc*1.5) <<< to remove accuracy builder
        #Once removed, try setting accuracy = 10, 20, 50, 100, 1000 to see if that affects the results
        #Note: This code will hang if your desired accuracy is too fine for your device
        #Note: This code will hang if you interact with the Command Prompt AT ALL 
        #Try pressing ESC or CTRL-C once if you interacted with the CMD,
        #this might allow the process to continue

    p = sp.Popen(pshellcomm, stdin = sp.PIPE, stdout = sp.PIPE, stderr = sp.STDOUT, text=True)
    (out, err) = p.communicate()
    out = re.split('\n', out)

    lat = float(out[0])
    long = float(out[1])
    radius = int(out[2])
    data = {"lat" : lat,
            "long" : long}
    locationData = r'data.json'
    print(lat, long, radius)
    with open(locationData, 'w') as f:
        json.dump(data, f)
    current_dir = os.getcwd()
    # G:\My Drive\new folder
    dest_dir = 'G:\\My Drive\\banking' # Replace with the destination directory path

    for filename in os.listdir(current_dir):
        if filename.endswith("data.josn"):
            shutil.move(os.path.join(current_dir, filename), dest_dir)
    print('Moved the file to desiered location.')

branchLocation()