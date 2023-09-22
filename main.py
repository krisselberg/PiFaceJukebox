from pydub import AudioSegment
from pydub.playback import play
import cv2
import pickle
import os

# Load the model and label dictionary (if saved previously)
model = cv2.face.LBPHFaceRecognizer_create()
model.read('face_model.yml')
with open('label_dict.pkl', 'rb') as f:
    label_dict = pickle.load(f)

# Start the video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    label, confidence = model.predict(grayscale_img)
    print(label_dict[label], confidence)
    if confidence < 100:  # You can adjust this value based on your requirements
        person_name = label_dict[label]
        mp3_file = f"music/{person_name}.m4a"
            
        if os.path.exists(mp3_file):
            song = AudioSegment.from_file(mp3_file, format="m4a")
            play(song)
    
        cv2.putText(frame, person_name, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()