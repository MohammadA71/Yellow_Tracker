# Yellow_Tracker
This project uses OpenCV and Pygame to simulate a robot that tracks and follows a yellow object in real time. The webcam captures video, applies color detection to identify the object's position, and updates the robot's movement accordingly. Pygame visualizes the robot's movement, creating an interactive object-tracking simulation.

# Files
**Project1.py** 
  - Captures video from the webcam  
  - Converts frames to HSV color space  
  - Filters yellow objects  
  - Tracks and displays them using Pygame

# Libraries & Frameworks
  - Python
  - OpenCV (cv2) - (Used for capturing webcam video, converting frames to HSV color space, and detecting yellow objects.)
  - numpy - (Helps with numerical operations and efficient array processing for image data.)
  - pygame - (Handles visualization of the tracked objects in a display window.)

# How it works!
  - Captures video from your webcam
  - Converts the frame to HSV color space
  - Filters out non yellow colors
  - Tracks the yellow object
  - Displays the results using Pygame

# Adjustments
  - You can modify the HSV range inside Project1.py to fine-tune color detection.
  - Try different lighting conditions to improve accuracy.

