from ultralytics import YOLO
import os,cv2
from PIL import Image, ImageDraw

# Load the trained YOLOv8 model
model = YOLO("path_to_trained_model")  #yolov8.pt or best.pt

# Set paths
image_folder_path ="input_images"
output_folder_path = "detected_frames"

# Ensure output folder exists
os.makedirs(output_folder_path, exist_ok=True)

def process_image(image_path):
    try:
        # Perform inference
        results = model(image_path)
        
        for i, result in enumerate(results):
            # Generate output file path
            output_file_path = os.path.join(output_folder_path, f"{os.path.splitext(os.path.basename(image_path))[0]}result{i}.jpg")
            print("output_file_path", output_file_path)
            
            # Save the annotated image
            annotated_image = result.plot()  # Plot returns the image with detections
            
             # Save the annotated image manually
            success = cv2.imwrite(output_file_path, annotated_image)
            if not success:
                print(f"Failed to save image: {output_file_path}")
            
            # Display the predictions (optional)
            #result.show()
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")


# Process each image in the folder
for image_name in os.listdir(image_folder_path):
    image_path = os.path.join(image_folder_path, image_name)
    if os.path.isfile(image_path):
        process_image(image_path)

print("Detection completed and results saved.")
