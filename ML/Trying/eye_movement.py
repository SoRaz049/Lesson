import random
import cv2
import dlib
import numpy as np

# Load necessary models for face detection and eye tracking
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("D:/Data Science/practice files/ML/Trying/shape_predictor_68_face_landmarks.dat")

# Define possible directions
directions = ['left', 'right', 'up', 'down']

# Randomly select two directions
challenge = random.sample(directions, 2)
print(f"Please move your eyes {challenge[0]} and then {challenge[1]}")

# Initialize camera
cap = cv2.VideoCapture(0)

def get_eye_landmarks(shape):
    left_eye = shape[36:42]
    right_eye = shape[42:48]
    return left_eye, right_eye

def compute_centroid(landmarks):
    points = np.array(landmarks)
    centroid = np.mean(points, axis=0)
    return centroid

def eye_direction(eye_centroid, frame_size, direction):
    x, y = eye_centroid
    width, height = frame_size

    if direction == 'left':
        return x < width / 3
    elif direction == 'right':
        return x > 2 * width / 3
    elif direction == 'up':
        return y < height / 3
    elif direction == 'down':
        return y > 2 * height / 3
    return False

# Buffer to store previous eye centroids
eye_buffer = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)
        shape = [(p.x, p.y) for p in landmarks.parts()]
        left_eye, right_eye = get_eye_landmarks(shape)

        # Compute centroids
        left_centroid = compute_centroid(left_eye)
        right_centroid = compute_centroid(right_eye)

        # Append centroids to buffer
        eye_buffer.append((left_centroid, right_centroid))
        if len(eye_buffer) > 10:  # Maintain a buffer of 10 frames
            eye_buffer.pop(0)

        # Check if user follows the eye movement challenge
        if len(eye_buffer) >= 2:
            initial_left, initial_right = eye_buffer[0]
            final_left, final_right = eye_buffer[-1]
            if (eye_direction(initial_left, frame.shape[1::-1], challenge[0]) and
                eye_direction(final_left, frame.shape[1::-1], challenge[1])):
                print("Challenge completed!")
                break

        # Debug: Draw landmarks and centroids
        for (x, y) in shape:
            cv2.circle(frame, (x, y), 1, (255, 0, 0), -1)

        cv2.circle(frame, (int(left_centroid[0]), int(left_centroid[1])), 2, (0, 255, 0), -1)
        cv2.circle(frame, (int(right_centroid[0]), int(right_centroid[1])), 2, (0, 255, 0), -1)

    cv2.imshow('Eye Movement Challenge', frame)
    
    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
