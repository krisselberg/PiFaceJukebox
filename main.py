import pygame
import cv2
import pickle
import os
import face_recognition
import subprocess
from pydub import AudioSegment
from picamera2 import Picamera2

def convert_to_mp3(m4a_file):
    mp3_file = m4a_file.replace('.m4a', '.mp3')
    AudioSegment.from_file(m4a_file).export(mp3_file, format='mp3')
    return mp3_file

def convert_all_m4a(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.m4a'):
            m4a_file = os.path.join(directory, filename)
            convert_to_mp3(m4a_file)

# Initialize pygame mixer
pygame.mixer.init()

# Convert all .m4a files to .mp3
convert_all_m4a('./music')

# Load the model and label dictionary
with open('face_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('label_dict.pkl', 'rb') as f:
    label_dict = pickle.load(f)

# Initialize PiCamera
print('initializing camera')
camera = Picamera2()
camera_config = camera.create_preview_configuration(main={"size": (640, 480)})
camera.configure(camera_config)
camera.start()
print('initialized camera')

is_playing = False
person_name = ""

while True:
    frame = camera.capture_array()
    print('frame')
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)

    if len(face_locations) > 0:
        face_encoding = face_recognition.face_encodings(rgb_frame, face_locatio>
        label = model.predict([face_encoding])
        probability = model.predict_proba([face_encoding])
        confidence = 1 - probability[0][label[0]]
        print(label_dict[label[0]], confidence)
        
        if confidence < 0.5 and not is_playing:
                person_name = label_dict[label[0]]
                mp3_file = f"music/{person_name}.mp3"
                if not is_playing:
                    subprocess.run(['espeak', f"hello {person_name}"])
                
                if os.path.exists(mp3_file):
                        pygame.mixer.music.load(mp3_file)
                        pygame.mixer.music.play()
                        is_playing = True
        
        elif pygame.mixer.music.get_busy() == 0:
                is_playing = False

# Cleanup
camera.stop()