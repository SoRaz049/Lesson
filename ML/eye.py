import cv2
import dlib
import numpy
from scipy.spatial import distance

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Define constants
EYE_AR_THRESHOLD = 0.25
EYE_AR_CONSEC_FRAMES = 3
COUNTER = 0
ex
# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)
    

    for rect in rects:
        shape = predictor(gray, rect)
        shape_np = shape_to_np(shape)  # Convert to NumPy array

        # Extract eye coordinates (left and right eyes)
        left_eye = shape_np[lStart:lEnd]
        right_eye = shape_np[rStart:rEnd]

        # Calculate the eye aspect ratio (EAR)
        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)

        # Average the EAR for both eyes
        ear = (left_ear + right_ear) / 2.0

        # Detect if blink occurs
        if ear < EYE_AR_THRESHOLD:
            COUNTER += 1
        else:
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                print("Blink detected! Liveness confirmed.")
            COUNTER = 0

    cv2.imshow("Blink Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
