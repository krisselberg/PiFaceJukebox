import cv2
from playsound import playsound
import os

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def recognize_and_play_music(video_source=0):
    cap = cv2.VideoCapture(video_source)
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            
            # Assuming the face recognition identifies John Doe
            person_name = "CHANGE_ME"
            
            # Look up their theme song and play it
            music_file = f"music/{person_name}.mp3"
            if os.path.exists(music_file):
                playsound(music_file)

        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:  # Press 'Esc' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize_and_play_music()