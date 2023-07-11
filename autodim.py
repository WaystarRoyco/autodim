#!/usr/bin/env python3

# Import the required modules
import cv2
import numpy as np
import subprocess
import time

# Define the camera device index (0 for default camera)
camera_index = 0

# Define the redshift command template
redshift_command = "redshift -P -O 4100 -b {}"

# Define the brightness range for redshift (0.1 to 1) 
brightness_min = 0.1
brightness_max = 1

# Define the brightness threshold for ambient light (0 to 255)                                              brightness_threshold = 128
# brightness_threshold =

# Define the time interval for checking ambient light (in seconds)
time_interval = 10

# Create a video capture object
cap = cv2.VideoCapture(camera_index)

# Check if the camera is opened
if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

# Start a while loop
while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Check if the frame is valid
    if not ret:
        print("Error: Could not read frame")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate the mean brightness of the frame
    brightness = np.mean(gray)

    # Print the brightness value for debugging
    print("Brightness: {}".format(brightness))

    # Map the brightness value to the redshift brightness range
    redshift_brightness = np.interp(brightness, [0, 255], [brightness_min, brightness_max])

    # Print the redshift brightness value for debugging
    print("Redshift brightness: {}".format(redshift_brightness))

    # Run the redshift command with the redshift brightness value
    subprocess.run(redshift_command.format(redshift_brightness), shell=True)

    # Wait for the time interval
    time.sleep(time_interval)

# Release the video capture object
cap.release()
