import cv2
import mediapipe as mp
import pyautogui
import time
from pynput.keyboard import Controller

# Initialize the FaceMesh model
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

# Open the webcam
cam = cv2.VideoCapture(0)

# Get the screen size
screen_w, screen_h = pyautogui.size()

# Initialize keyboard controller
keyboard = Controller()

# Define blink thresholds
right_blink_threshold = 0.3
left_blink_threshold = 0.3

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                pyautogui.moveTo(screen_x, screen_y)
            if id == 2:
                if landmark.z > right_blink_threshold:
                    pyautogui.click(button='right')
                    time.sleep(0.1)
            if id == 3:
                if landmark.z > left_blink_threshold:
                    pyautogui.click(button='left')
                    time.sleep(0.1)
            if id == 4:
                keyboard.type('Hello World')
