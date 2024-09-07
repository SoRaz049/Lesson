import cv2
import face_recognition
import pickle
import os

#importing the sample images.
FolderPath = "D:/Data Science/practice files/ML/Trying/Images"
PathList = os.listdir(FolderPath)  # This will give a list of file names
imgList = []

studentIds = []

# Load each mode image and append it to the list
for path in PathList:
    img = cv2.imread(os.path.join(FolderPath, path))
    
    #to split the files in the foler and only extract the id of the files and store it in studentIDs.
    studentIds.append(os.path.splitext(path)[0])
    
    #print(os.path.splitext(path)[0]) #to split the files in the foler and only extract the id of the files.
    
    if img is not None:
        imgList.append(img)

#to check the number of images imported.
print(studentIds)


def findEncodings(imageList):
    encodeList = []
    for img in imgList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
        
    return encodeList

print("Encoding Started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Completed")

file = open("EncodeFile.p", "wb")
pickle.dump(encodeListKnownWithIds, file)

file.close()
print("File Saved.")
