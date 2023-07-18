# importing necessary libraries i.e... opencv,mediapipe
import cv2 # open cv
import mediapipe as mp # pose estimation

mp_drawing = mp.solutions.drawing_utils # pose landmarks
mp_pose = mp.solutions.pose # performing pose estimation

# Initialize the pushup counter and detection flag
pushup_counter = 0 # track number of pushup
is_pushup = False # detect weather pushup being performed or not

# function to detect push up

# Modify the detect_pushups function to include pull-up detection

def detect_pushups(image):
    global pushup_counter, is_pushup

    # Convert the image to RGB format
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect the pose landmarks in the image
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        results = pose.process(image_rgb)

        # Draw the pose landmarks on the image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2))

        # Check if the left and right wrists are above the corresponding shoulders
        if results.pose_landmarks:
            left_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y
            left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y

            right_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y
            right_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y

            # Check if wrists are above shoulders
            if left_wrist < left_shoulder and right_wrist < right_shoulder:
                # If wrists are above the shoulders, it's a potential push-up
                if not is_pushup:
                    # Check for specific pose/movement for pull-ups
                    # Modify the condition below according to the pose/movement for pull-ups
                    if pull_up_condition_met():
                        is_pushup = False
                        cv2.putText(image, "NOT A PUSH UP", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    else:
                        pushup_counter += 1
                        is_pushup = True
            else:
                is_pushup = False

    # Display the push-up count on the image
    cv2.putText(image, f"Push-ups: {pushup_counter}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    return image


# start pushup detection

cap = cv2.VideoCapture(0)  # Change the parameter to the desired camera index if needed

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip the frame horizontally for mirror effect

    # Detect and track pushups
    frame = detect_pushups(frame)

    # Display the resulting frame
    cv2.imshow('Pushup Detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
