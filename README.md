# Real-Time Hand Gesture Recognition

A real-time hand gesture recognition system built with OpenCV and MediaPipe. It detects a hand via webcam, tracks 21 hand landmarks, and classifies the hand shape into one of several recognized gestures — all live, frame by frame.

## What it does

- Captures live webcam video
- Detects a hand and tracks 21 landmark points using MediaPipe Hands
- Determines whether each finger is extended or curled by comparing landmark coordinates
- Classifies the overall hand shape into a named gesture
- Displays the detected gesture directly on the video feed
- Smooths detection across frames to reduce flicker near ambiguous hand positions

## Gestures currently recognized

- Open palm
- Closed fist
- Peace sign
- Thumbs up
- (add any others you've implemented)

## How it works

1. **Hand detection** — MediaPipe Hands returns 21 (x, y, z) landmark coordinates per detected hand, per frame.
2. **Finger state** — For each finger, the fingertip's y-coordinate is compared to that finger's own knuckle (PIP joint) y-coordinate. A smaller y-value (higher up in the frame) means the finger is extended.
3. **Thumb state** — Since the thumb moves side-to-side rather than up-down, its state is determined by the distance between the thumb tip and the base of the pinky, rather than a simple y-coordinate comparison.
4. **Gesture classification** — The five finger states (extended/curled) are combined with simple conditional logic to determine the named gesture.
5. **Stability** — A short rolling history of recent detections is used so a gesture is only displayed once it's held consistently across several frames, reducing flicker.

## Tech stack

- Python 3.11
- OpenCV — video capture and display
- MediaPipe — hand landmark detection
- NumPy / math — geometric calculations

## Setup

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/gesture-recognition-cv.git
cd gesture-recognition-cv

# Create and activate a virtual environment (Python 3.11 recommended)
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install opencv-python mediapipe numpy
```

## Usage

```bash
python 5_gesturerecog.py
```

- Hold your hand up to the webcam.
- The detected gesture will be displayed on screen in real time.
- Press `q` to quit.

## Known limitations

- Detects one hand at a time.
- Currently supports static hand-shape gestures only — motion-based signs are not yet handled.
- Gesture thresholds were tuned on a specific lighting/camera setup and may need adjustment for different environments.

## Future improvements

- Expand gesture vocabulary
- Add a practical use-case on top of detection (e.g., triggering an action on a specific gesture)
- Support two-hand gestures
