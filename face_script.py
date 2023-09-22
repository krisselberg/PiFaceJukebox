import cv2
import os

def capture_images(folder_name):
    # Construct the full path for the new folder inside the 'faces' directory
    full_folder_path = os.path.join('faces', folder_name)
    
    # Ensure the folder exists
    if not os.path.exists(full_folder_path):
        os.makedirs(full_folder_path)

    # Open a connection to the first webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Could not open webcam")
        exit()
    
    print("Press spacebar to capture an image, 'q' to quit")

    img_count = 0
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Display the frame
        cv2.imshow('Capture Images', frame)

        key = cv2.waitKey(1)
        if key == ord(' '):  # Spacebar pressed
            img_filename = os.path.join(full_folder_path, f'image{img_count}.jpg')
            cv2.imwrite(img_filename, frame)
            print(f'Image saved: {img_filename}')
            img_count += 1
        elif key == ord('q'):  # 'q' key pressed
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    folder_name = input("Enter the folder name where images should be saved: ")
    capture_images(folder_name)