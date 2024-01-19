import cv2
import mediapipe
import pyautogui

# Initialize the FaceMesh model
face_mesh_landmarks = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)

# Open the webcam
cam = cv2.VideoCapture(0)

# Get the screen size
screen_w, screen_h = pyautogui.size()

while True:
    _, image = cam.read()
    image = cv2.flip(image, 1)
    window_h, window_w, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image with FaceMesh
    processed_image = face_mesh_landmarks.process(rgb_image)

    # Get all face landmark points
    all_face_landmark_points = processed_image.multi_face_landmarks

    if all_face_landmark_points:
        one_face_landmark_points = all_face_landmark_points[0].landmark

        # Calculate mouse coordinates based on specific face landmarks
        for id, landmark_point in enumerate(one_face_landmark_points[474:478]):
            x = int(landmark_point.x * window_w)
            y = int(landmark_point.y * window_h)
            
            if id == 1:
                mouse_x = int(screen_w * x / window_w)
                mouse_y = int(screen_h * y / window_h)
                pyautogui.moveTo(mouse_x, mouse_y)

            cv2.circle(image, (x, y), 3, (0, 0, 255))

        # Detect left eye state
        left_eye = [one_face_landmark_points[145], one_face_landmark_points[159]]
        
        # Calculate left eye positions
        left_eye_x = int((left_eye[0].x + left_eye[0].x) * window_w / 1)
        left_eye_y = int((left_eye[0].y + left_eye[0].y) * window_h / 1)

        cv2.circle(image, (left_eye_x, left_eye_y), 3, (0, 255, 255))

        # Check if the eye is closed (you may need to adjust the threshold)
        if left_eye[0].y - left_eye[1].y < 0.02:
            pyautogui.click()
            pyautogui.sleep(2)
            print('Mouse clicked')
    cv2.imshow("Eye controlled mouse", image)
    key = cv2.waitKey(1)

    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
