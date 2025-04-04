# 🚗 Smart Parking Space Detector using Python & OpenCV

A computer vision-based parking space detection system built with Python and OpenCV. This project uses a video feed of a parking lot and identifies which spaces are occupied and which are available — all in real time.

## 🎯 Features

- 🔍 Detects empty and occupied parking spots
- 🎥 Works with both live camera feed or video files
- 🧠 Position tracking with pre-defined parking zones
- ✅ Visual indicators for each space (green = free, red = taken)
- 🖼️ Includes sample video and static image input
- 🗂️ Parking position coordinates are saved and re-used

## 📁 Project Structure
```
Park Control/ ├── Parking_Space_Control.py # Main detection script ├── main.py # Alternate script (not used) ├── carPark.mp4 # Sample parking video ├── carParkImg.png # Image for manual marking of spaces ├── CarParkPos # File storing parking spot positions └── .git # Git metadata (if applicable)
```

## 🧰 Requirements

- Python 3.x
- OpenCV
- NumPy
- Pickle (standard library)

## 📦 How to Use

Clone the repository:
```
git clone https://github.com/moeinnrz/FileLocker.git
```

### 🔧 Install dependencies

```bash
pip install opencv-python numpy
```

🚀 How to Run

1.Mark parking spots (if not already marked):
- Run main.py
- Click on each parking spot in the image to mark it
- The list will be saved as CarParkPos

2.Run the detector:
```
python Parking_Space_Control.py
```

- The system will open the video carPark.mp4
- It will display colored overlays:
- 🟥 Red boxes = Occupied
- 🟩 Green boxes = Available
- Parking spot count is also shown on the screen

⚙️ How it Works

- Parking spot coordinates are marked manually on a reference image
- On every video frame:
- Each spot is cropped and analyzed using thresholding
- If the spot is visually “full,” it’s marked as occupied
- Final result is drawn on top of the video with spot count
