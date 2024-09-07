import cv2
import os
import face_recognition


## TO ENABLE THE CAMARA
# video_cap = cv2.VideoCapture(0)
# while True :
#     ret, video_data = video_cap.read()
#     cv2.imshow("video_live", video_data)
#     if cv2.waitKey(10) == ord("a"):
#         break
    
# video_cap.release()


## TO CREATE THE RECTANGLE WHERE THE FACE CAN BE DETECTED.
    
# face_capture = cv2.CascadeClassifier("D:/Data Science/practice files/ML/.venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
# video_cap = cv2.VideoCapture(0)

# while True :
#     ret, video_data = video_cap.read()
#     color = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
#     face = face_capture.detectMultiScale(
#         color,
#         scaleFactor= 1.1, 
#         minNeighbors=5,
#         minSize=(30,30),
#         flags= cv2.CASCADE_SCALE_IMAGE
#     )
    
#     for(x,y,w,h) in face:
#         cv2.rectangle(video_data, (x,y), (x+w, y+h), (0,255,0),2)
#     cv2.imshow("video_live", video_data)
#     if cv2.waitKey(10) == ord("a"):
#         break
    
# ## TO CAPTURE THE IMAGE 
#     # if ret:  
#     # # saving image in local storage 
#     #     cv2.imwrite("image.png",video_data)
    
# video_cap.release()



face_capture = cv2.CascadeClassifier("D:/Data Science/practice files/ML/.venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)
image_saved = False

while True :
    ret, video_data = video_cap.read()
    color = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    face = face_capture.detectMultiScale(
        color,
        scaleFactor= 1.1, 
        minNeighbors=5,
        minSize=(30,30),
        flags= cv2.CASCADE_SCALE_IMAGE
    )
    
    for(x,y,w,h) in face:
        cv2.rectangle(video_data, (x,y), (x+w, y+h), (0,255,0),2)
    cv2.imshow("video_live", video_data)
    
    if cv2.waitKey(10) == ord("a") and not image_saved: # Can directly capture and save the image
        capture_image = video_data.copy()
        cv2.imwrite("D:/Data Science/practice files/ML/captured_image/image.png",capture_image)
        print("Image has been successfully captured and saved.")
        image_saved = True
    
    if cv2.waitKey(10) == ord("q"):
        break
    
video_cap.release()
cv2.destroyAllWindows()

folder_path = "D:/Data Science/practice files/ML/stored_image"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

#image = "D:/Data Science/practice files/ML/IMG_3612.jpg"
#capture_image = cv2.imread(image, 0)
if image_saved and capture_image is not None:
    gcolor = cv2.cvtColor(capture_image, cv2.COLOR_RGB2BGR)
    crop = face_capture.detectMultiScale(
        gcolor,
        scaleFactor=1.1,
        minNeighbors=10,
        minSize=(100,100)
    )

i = 0
for (x, y, w, h) in crop:
    cropped_image = capture_image[y:y+h, x:x+w]  # Correct way to crop the image
    target_file = os.path.join(folder_path, f"cropped_image_{i}.jpg")  # Correct file path
    cv2.imwrite(target_file, cropped_image)  # Save the cropped image
    print(f"Cropped image saved as {target_file}")
    i += 1
 
    

    

