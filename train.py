from ultralytics import YOLO

# Load a model
model = YOLO()  # build a new model from scratch
#model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="#path_to_data.yaml", batch=16, epochs=100, save =True)
metrics = model.val()  # evaluate model performance on the validation set
results = model("#path_to_image")  # predict on an image
for result in results:
    result.show()  # Display the predictions

path = model.export(format="onnx")  # export the model to ONNX format
