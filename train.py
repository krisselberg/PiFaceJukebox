import face_recognition
import os
import numpy as np
import pickle
from sklearn import svm

data_folder_path = 'faces'

# Collecting labels and embeddings
labels = []
embeddings = []
label_dict = {}
current_id = 0

for person_name in os.listdir(data_folder_path):
    person_path = os.path.join(data_folder_path, person_name)
    if os.path.isdir(person_path):
        for filename in os.listdir(person_path):
            img_path = os.path.join(person_path, filename)
            image = face_recognition.load_image_file(img_path)
            face_locations = face_recognition.face_locations(image)
            print(img_path, face_locations)
            
            if len(face_locations) == 0:
                print(f"No faces found in {img_path}. Skipping...")
                continue
            
            # Assuming the first face is the desired one
            face_embedding = face_recognition.face_encodings(image, face_locations)[0]
            label_dict[current_id] = person_name
            labels.append(current_id)
            embeddings.append(face_embedding)
        current_id += 1

# Train a SVM classifier on the embeddings
clf = svm.SVC(gamma='scale', probability=True)
clf.fit(embeddings, labels)

# Save the SVM classifier (Optional)
with open('face_model.pkl', 'wb') as f:
    pickle.dump(clf, f)

# Save the label dictionary for later use (Optional)
with open('label_dict.pkl', 'wb') as f:
    pickle.dump(label_dict, f)