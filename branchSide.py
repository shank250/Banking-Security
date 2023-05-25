import subprocess as sp
import cv2
import mediapipe as mp
import cv2
import numpy as np
import re
import time
import json
import os
import shutil
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyaudio
import wave
# import face_recognition
import cv2


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

    p = sp.Popen(pshellcomm, stdin = sp.PIPE, stdout = sp.PIPE, stderr = sp.STDOUT, text=True)
    (out, err) = p.communicate()
    out = re.split('\n', out)

    lat = float(out[0])
    long = float(out[1])
    # radius = int(out[2])
    data = {"lat" : lat,
            "long" : long}
    locationData = r'data.json'
    print(lat, long)
    with open(locationData, 'w') as f:
        json.dump(data, f)
    current_dir = os.getcwd()
    # G:\My Drive\new folder
    dest_dir = r'C:\\Users\\980ar\\OneDrive\\Pictures\\Documents\\Projects\\Hackathons\\Hack-a-prenure-nsut(1)20-05-2023\\Hack-a-prenure' # Replace with the destination directory path
    # dest_dir = r"Z:\Banking--main\Banking--main\Banking--main\output"

    for filename in os.listdir(current_dir):
        if filename.endswith("data.json"):
            shutil.move(os.path.join(current_dir, filename), dest_dir)
    print('Moved the file to desiered location.')

def weaponDetection():
    # Load Yolo
    net = cv2.dnn.readNet("yolov3_training_2000.weights", "yolov3_testing.cfg")
    classes = ["Weapon"]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # Enter file name for example "ak47.mp4" or press "Enter" to start webcam
    def value():
        val = input("Enter file name or press enter to start webcam: \n")
        if val == "":
            val = 0
        return val

    # For video capture
    cap = cv2.VideoCapture(value())

    while True:
        _, img = cap.read()
        height, width, channels = img.shape

        # Detecting objects
        # blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        blob = cv2.dnn.blobFromImage(img, 0.00392, (608, 608), (0, 0, 0), True, crop=False)
        # blob = cv2.dnn.blobFromImage(img, 0.00392, (750, 750), (0, 0, 0), True, crop=False)

        net.setInput(blob)
        outs = net.forward(output_layers)

        # Showing information on the screen
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.3:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.3)
        if indexes == 0:
            print("Weapon detected in frame")
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                # Retrieve the rectangle coordinates
                x1 = x
                y1 = y
                x2 = x + w
                y2 = y + h
                label = str(classes[class_ids[i]])
                color = colors[class_ids[i]]
                confidence = confidences[i]
                percentage = f"{round(confidence * 100, 2)}%"
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
                cv2.putText(img, percentage, (x, y + 60), font, 3, color, 3)
                print("Weapon detected at coordinates:", (x1, y1, x2, y2))

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

def bodyMoments():
    # body detection

    # cap = cv2.VideoCapture('1.mp4')
    cap = cv2.VideoCapture(0)

    mpDraw = mp.solutions.drawing_utils
    # mpDraw.DrawingSpec(color=(255, 0, 255), thickness=2, circle_radius=2)
    mpPose = mp.solutions.pose
    mpFaceDetection = mp.solutions.face_detection
    faceDEtection = mpFaceDetection.FaceDetection()
    pose = mpPose.Pose()

    while True:
        success,  img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result_pose = pose.process(imgRGB)
        # result_face = mpFaceDetection.process(imgRGB)
        # print(img, result_pose.pose_landmarks, mpPose.POSE_CONNECTIONS)
        if result_pose.pose_landmarks:
            mpDraw.draw_landmarks(img, result_pose.pose_landmarks)
            for id, ln in enumerate(result_pose.pose_landmarks.landmark):
                h, w, c =img.shape
                if 13 <= id <= 22:
                    print(id, ln.x, ln.y)
                # from 13 to 22 locations could have weapons
                # cx, cy = int(ln.x*w) + int(ln.y*h)
        # if result_face.detections :
        #     for id, detection in enumerate(result_face.detections):
        #         print(id, detection)


        cv2.imshow("IMAGE",img)
        cv2.waitKey(1)


bodyMoments()
branchLocation()

    
