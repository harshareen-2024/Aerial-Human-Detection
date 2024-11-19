#Introduction:

This project utilizes YOLOv8 for detecting objects in aerial images. The primary focus is on detecting objects from a dataset created from raw aerial images. It uses OpenCV to save the images with detected objects and can optionally display the images. The results are saved in a specified output folder.
Dataset:

The dataset used for training and testing the YOLOv8 model consists of aerial images that were annotated and labeled using Roboflow. The dataset is structured into train, val, and test folders and includes a data.yaml file that defines the dataset configuration for YOLO training.

The command line argument for training the dataset in Linux:

#command-line argument for training 
----->yolo task=detect mode=train data= #path_to_data.yaml model=yolov8n.pt epochs=100 imgsz=640

    Annotation Tool: Roboflow
    Image Sources: Aerial images captured using drones
    Labels: human

#Prerequisites:

    Python 3.8 or higher
    GPU support is recommended for faster inference but is not mandatory


#Usage

    Place your input images in the input_images folder.
    Run the detection script:

python yolo_detect.py

The script will process each image in the folder and save the results with detections to the detected_frames folder.


