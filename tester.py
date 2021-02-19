import cv2
import faceRecognition as fr

test_img=cv2.imread('C:/Users/DELL/Desktop/st20156678/FaceRecognition/TestImages/Saru.jpg')
faces_detected,gray_img=fr.faceDetection(test_img)
print("faces_detected:",faces_detected)

#for(x,y,w,h) in faces_detected:
 #   cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=5)
    
  #  resized_img=cv2.resize(test_img,(1000,1000))
   # cv2.imshow("face dtecetion",resized_img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows
    
#faces,faceID=fr.labels_for_training_data('C:/Users/DELL/Desktop/st20156678/FaceRecognition/resizedTrainingImages')
#face_recognizer=fr.train_classifier(faces,faceID)
#face_recognizer.save('trainingData.yml')

face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trainingData.yml')

name={0:"Nayan",1:"Saru"}

for face in faces_detected:
    (x,y,w,h)=face
    roi_gray=gray_img[y:y+h,x:x+h]
    label,confidence=face_recognizer.predict(roi_gray)
    print("confidence:",confidence)
    print("label:",label)
    fr.draw_rect(test_img,face)
    predicted_name=name[label]
    if(confidence>24):
        continue
    fr.put_text(test_img,predicted_name,x,y)

resized_img=cv2.resize(test_img,(1000,1000))
cv2.imshow("face dtecetion",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows
