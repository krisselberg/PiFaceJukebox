import pygame
import cv2
import pickle
import os
import face_recognition
from pydub import AudioSegment

def convert_to_mp3(m4a_file):
    mp3_file = m4a_file.replace('.m4a', '.mp3')
    AudioSegment.from_file(m4a_file).export(mp3_file, format='mp3')
    return mp3_file

# Initialize pygame mixer
pygame.mixer.init()

# Load the model and label dictionary (if saved previously)
with open('face_model.pkl', 'rb') as f:  # Changed line
    model = pickle.load(f)  # Changed line
with open('label_dict.pkl', 'rb') as f:
    label_dict = pickle.load(f)

# Start the video capture
cap = cv2.VideoCapture(0)

is_playing = False  # Variable to track if a song is currently playing
person_name = ""

while True:
    ret, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Changed to RGB as face_recognition uses RGB
    face_locations = face_recognition.face_locations(rgb_frame)
    
    if len(face_locations) > 0:
        face_encoding = face_recognition.face_encodings(rgb_frame, face_locations)[0]
        label = model.predict([face_encoding])
        probability = model.predict_proba([face_encoding])
        confidence = 1 - probability[0][label[0]]  # Assuming that a higher probability corresponds to a more confident prediction
        print(label_dict[label[0]], confidence)
        
        if confidence < 0.05 and not is_playing:  # Changed confidence threshold as per SVM probabilities
            person_name = label_dict[label[0]]
            m4a_file = f"music/{person_name}.m4a"
                
            if os.path.exists(m4a_file):
                mp3_file = convert_to_mp3(m4a_file)
                pygame.mixer.music.load(mp3_file)
                pygame.mixer.music.play()
                is_playing = True
        
        elif pygame.mixer.music.get_busy() == 0:
            is_playing = False  # Set the flag to False if no song is playing
        
        cv2.putText(frame, person_name, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()