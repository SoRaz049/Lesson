import cv2
import dlib
import os
import pickle

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

#TO SET THE BACKGROUND FOR THE CAMARA.  
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


#LOAD THE ENCODING FILE.
file = open("EncodeFile.p", "rb")
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds

#TO OPEN TTTHE CAMARA IN THE DESIRED LOCATION OF BACKGROUND.
while True:
    ret, image = cap.read() 
    # Insert the image into the background at specified locations
    imgBackground[162:162 + 480, 55: 55 + 640] = image
    imgBackground[44:44 + 633, 808: 808 + 414] = imgModeList[1]  

    cv2.imshow("Face Attendance", imgBackground)
    if cv2.waitKey(10) == ord("q"):
        break



cap.release()
cv2.destroyAllWindows()

    

