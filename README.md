# Interactive-Image-Annotation-Tool-with-Hand-Gestures

This Python script utilizes computer vision to create an interactive image annotation tool that recognizes hand gestures to navigate through a folder of images, write annotations, and erase them. It uses the `cv2` library for computer vision, and the `cvzone` HandTrackingModule for hand tracking.

## Prerequisites

Before running the script, make sure you have the following libraries installed:

- OpenCV (`cv2`)
- NumPy
- cvzone (HandTrackingModule)

You can install the required libraries using `pip`:

```bash
pip install opencv-python-headless
pip install numpy
pip install cvzone
```

## Usage

1. Place the images you want to annotate in a folder (e.g., "meme") in the same directory as the script.

2. Run the script:

```bash
python interactive_annotation_tool.py
```

3. The script will open a window displaying the images from the specified folder.

4. Use your hand gestures to interact with the tool:
   - **Next Image:** Show the next image by raising your index and middle fingers.
   - **Previous Image:** Show the previous image by raising all five fingers.
   - **Quit:** Quit the tool by raising your index and pinky fingers.
   - **Write Annotation:** Write annotations by showing only your index finger.
   - **Erase Annotation:** Erase annotations by showing four fingers except the pinky.

5. Annotations are drawn as lines on the current image. You can save or export the annotated images as needed.

6. To exit the tool, press the 'q' key in the window.

## Notes

- Make sure your camera is working and is correctly set up as the video source (change `cap=cv2.VideoCapture(0)` if necessary).
- The gesture threshold (300 pixels) can be adjusted to your liking for better recognition.
- The annotation lines will be drawn with a red color.

Feel free to modify and customize this script according to your needs.
