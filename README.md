

# YOLO Object Detection and Tracking

This project implements real-time object detection and tracking using the YOLOv4 algorithm combined with OpenCV. It processes video inputs to detect and track objects frame-by-frame, providing a foundation for applications like surveillance, traffic monitoring, and more.

## 📁 Repository Contents

* `app(bassics).py` – Entry point for running the application.
* `object_detection.py` – Contains functions for object detection using YOLOv4.
* `object_tracking.py` – Implements object tracking logic.
* `classes.txt` – List of object classes that the model can detect.
* `yolov4.cfg` – YOLOv4 configuration file.
* `los_angeles.mp4` – Sample video file for testing.
* `requirements.txt` – Python dependencies required to run the project.

## 🚀 Getting Started

### Prerequisites

* Python 3.6 or higher
* `pip` package manager

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/RandomRohit-hub/YOLO-obj-detection-and-tracking.git
   cd YOLO-obj-detection-and-tracking
   ```



2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```



3. **Download YOLOv4 weights:**

   Download the pre-trained YOLOv4 weights from the official source and place them in the project directory.

   ```bash
   wget https://pjreddie.com/media/files/yolov4.weights
   ```



## 🧪 Usage

Run the application using the sample video:

```bash
python app(bassics).py
```



This will process `los_angeles.mp4`, performing object detection and tracking on the video frames.

## 📝 Notes

* Ensure that the `yolov4.weights`, `yolov4.cfg`, and `classes.txt` files are present in the project directory.
* Modify `app(bassics).py` to change the input video or adjust detection parameters as needed.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).([GitHub][1])

---

For more information on YOLO and object detection techniques, you can refer to the following resources:

* [You Only Look Once: Unified, Real-Time Object Detection](https://arxiv.org/abs/1506.02640)
* [A Comprehensive Review of YOLO Architectures in Computer Vision](https://arxiv.org/abs/2304.00501)([arXiv][2], [arXiv][3])

Feel free to explore these materials to deepen your understanding of object detection and tracking methodologies.

---

[1]: https://github.com/leggedrobotics/darknet_ros?utm_source=chatgpt.com "YOLO ROS: Real-Time Object Detection for ROS - GitHub"
[2]: https://arxiv.org/abs/1506.02640?utm_source=chatgpt.com "You Only Look Once: Unified, Real-Time Object Detection"
[3]: https://arxiv.org/abs/2304.00501?utm_source=chatgpt.com "A Comprehensive Review of YOLO Architectures in Computer Vision: From YOLOv1 to YOLOv8 and YOLO-NAS"
