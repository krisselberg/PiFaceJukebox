import cv2
import os

# Path to the faces dataset
data_folder_path = 'faces'

# The LBPH (Local Binary Patterns Histograms) Face Recognizer
model = cv2.face.LBPHFaceRecognizer_create()

# Read images from each subdirectory
labels = []
face_samples = []
label_dict = {}
current_id = 0

for person_name in os.listdir(data_folder_path):
    person_path = os.path.join(data_folder_path, person_name)
    if os.path.isdir(person_path):
        for filename in os.listdir(person_path):
            img_path = os.path.join(person_path, filename)
            grayscale_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            label_dict[current_id] = person_name
            labels.append(current_id)
            face_samples.append(grayscale_img)
        current_id += 1

# Train the model
model.train(face_samples, np.array(labels))

# Save the model (Optional)
model.save('face_model.yml')

# Save the label dictionary for later use (Optional)
import pickle
with open('label_dict.pkl', 'wb') as f:
    pickle.dump(label_dict, f)