# Pi Face Jukebox

Welcome to the Pi Face Jukebox! This project allows you to create a fun and interactive experience by playing unique theme songs for people who enter a room based on facial recognition. The system utilizes a Raspberry Pi, a camera module, and the OpenCV library to achieve this functionality (for the MacOS alternative, click [here](https://github.com/jaslevy/PiFaceJukebox)).

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Quickstart](#quickstart)

## Introduction

This project aims to create a personalized and entertaining environment by associating theme songs with individuals through facial recognition. When someone enters a room monitored by the Raspberry Pi camera, the system will identify their face and play a predefined theme song associated with that person.

**Key features of the Facial Recognition Theme Song Generator:**

- **Facial Recognition:** The system uses OpenCV + an SVM to perform facial recognition.

- **Personalized Theme Songs:** You can configure the system to play unique theme songs for different people.

- **Raspberry Pi Integration:** The project is designed to run on a Raspberry Pi.

## Requirements

Before getting started, ensure you have the following hardware requirements:

### Hardware

- Raspberry Pi (3 or later recommended)
- Raspberry Pi Camera Module
- Speaker or audio output device
- Computer running macOS

## Quickstart

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/krisselberg/PiFaceJukebox
   ```

2. **Install Dependencies:**

Navigate to the project directory and install the required Python packages:

```bash
cd PiFaceJukebox
pip install -r requirements.txt
```

3. **Test Camera Configuration**
   To confirm that the camera is functioning properly with libcamera, capture a test image:

```bash
libcamera-still -o test.jpg
```

4. **Connect Audio Output Device**
   Connect your speaker or audio output device to the Raspberry Pi. Ensure that it is recognized by the Pi and properly configured. You can test the audio output by playing a test sound:

```bash
speaker-test -t wav -c 2
```

This command will play a test sound through the speaker to verify that the audio output is working correctly.

5. **Prepare the Music Directory:**
   Create a directory named music in the project folder and place the theme song files (.mp3 or .m4a formats) in this directory. Each file should be named after the person it is associated with.

6. **Collect Training Data:**
   Capture images of the people you want to recognize and assign theme songs to. This step should be done on a computer running MacOS. Use the face_script script included in the project:

```bash
python face_script.py
```

Enter the name of the person when prompted (should be the same as their associated music file), and capture several images of their face in different angles and lighting conditions.

7. **Train the Facial Recognition Model:**
   Once you have collected enough images, run the training script to generate the face recognition model:

```bash
python train.py
```

8. **Run the Pi Face Jukebox**
   Start the facial recognition theme song player (either headless from another computer or on the Raspberry Pi itself):

```bash
python main.py
```

## Troubleshooting

If you encounter issues, here are some common troubleshooting steps:

- Ensure all hardware components are correctly connected and configured.
- Check if the audio output is configured correctly on your Raspberry Pi.
- Ensure all dependencies are correctly installed and compatible with your Raspberry Pi.
