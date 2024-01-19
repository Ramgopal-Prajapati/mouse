import cv2
import mediapipe
import pyautogui

face_mesh_landmarks = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)
cam = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

while True:
    _, image = cam.read()
    image = cv2.flip(image, 1)
    window_h, window_w, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    processed_image = face_mesh_landmarks.process(rgb_image)
    all_face_landmark_points = processed_image.multi_face_landmarks

    if all_face_landmark_points:
        one_face_landmark_points = all_face_landmark_points[0].landmark

        # Extracting specific facial landmarks for mouse control
        left_eye_landmarks = [one_face_landmark_points[145], one_face_landmark_points[159]]
        right_eye_landmarks = [one_face_landmark_points[386], one_face_landmark_points[374]]

        # Calculating coordinates for left and right eye
        left_eye_x = int(left_eye_landmarks[0].x * window_w)
        left_eye_y = int(left_eye_landmarks[0].y * window_h)
        right_eye_x = int(right_eye_landmarks[0].x * window_w)
        right_eye_y = int(right_eye_landmarks[0].y * window_h)

        # Moving mouse based on left eye position
        mouse_x = int(screen_w / window_w * left_eye_x)
        mouse_y = int(screen_h / window_h * left_eye_y)
        pyautogui.moveTo(mouse_x, mouse_y)

        # Checking for left-click and right-click based on the movement of the left eye
        if right_eye_y - left_eye_y < 5:
            pyautogui.click(button='right')  # Right-click
            print('Right-click')

        elif left_eye_y - right_eye_y < 5:
            pyautogui.click(button='left')  # Left-click
            print('Left-click')

    # Display the processed image
    cv2.imshow("Eye controlled mouse", image)

    # Break the loop on 'Esc' key press
    key = cv2.waitKey(100)
    if key == 27:
        break

# Release the webcam and close OpenCV windows
cam.release()
cv2.destroyAllWindows()
    