import cv2
import dlib
import os
import pickle
import face_recognition
import numpy as np
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Load the background image
imgBackground = cv2.imread("D:/Data Science/practice files/ML/Trying/Resources/Background.png")

# Import the mode images into a list
FolderModePath = "D:/Data Science/practice files/ML/Trying/Resources/Modes"
modePath = os.listdir(FolderModePath)  # This will give a list of file names
imgModeList = []

# Load each mode image and append it to the list
for path in modePath:
    img = cv2.imread(os.path.join(FolderModePath, path))
    if img is not None:
        imgModeList.append(img)

# Load the encoding file
file = open("EncodeFile.p", "rb")
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds

# Open the camera feed and run face recognition
while True:
    ret, image = cap.read() 
    
    imgS = cv2.resize(image, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
    # Find the encoding of the current face in the current frame
    face_curFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, face_curFrame)
    

    # Insert the image into the background at specified locations
    imgBackground[162:162 + 480, 55: 55 + 640] = image
    imgBackground[44:44 + 633, 808: 808 + 414] = imgModeList[1]  


    # Loop through each face encoding and its corresponding location in the current frame
    for encoFace, FaceLoc in zip(encodeCurFrame, face_curFrame): 
        # Compare the current face encoding with the known encodings to check for a match
        matches = face_recognition.compare_faces(encodeListKnown, encoFace)
        
        # Calculate the distance between the current face encoding and known encodings
        # A lower distance means the face is more similar to the known faces
        face_distance = face_recognition.face_distance(encodeListKnown, encoFace)
        
        # # Print the results of the match (True/False for each known encoding)
        # print("Matches", matches)
        
        # # Print the calculated distance for each known encoding (lower values are better matches)
        # print("Face Distance", face_distance)

        matchIndex = np.argmin(face_distance)
        # print("Match Index", matchIndex)

        if matches[matchIndex]:
            # print(f"Known Face detected.")
            # print(studentIds[matchIndex])
            y1, x2, y2, x1 = FaceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
            imgBackground = cvzone.cornerRect(imgBackground, bbox, rt = 0)
            
            
    # To display he camara with tthe tile "Face Attendance."
    cv2.imshow("Face Attendance", imgBackground)
    if cv2.waitKey(10) == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
