# Plant Pest Detection Using YOLOv8 Nano 🦟
> [!NOTE]
> This is the third iteration of the model.

## Introduction
This model was developed for our thesis titled **"GroPro: Grow and Protect"**, which focuses in detecting and eliminating plant pests in urban gardens through object and audio detection. It can be used to detect pests in real-time, videos, and images.

## Model 🤖
The model is based on the YOLOv8 Nano architecture, which is a lightweight version of the YOLOv8 object detection algorithm, which is suitable for Raspberry Pi 4. The model was trained on a dataset of images of various plant pests. The dataset was collected through web scraping of various plant pest images.

## Performance ⚙
The model achieved a mean AP over different IoU thresholds, from 0.5 to 0.95, step 0.05 of 0.568 for all classes in validation. The following is a breakdown of the AP for each class:

- aphid: 0.0899
- fruit fly: 0.292
- scale insect: 0.202

The model is able to detect pests at a speed of 0.3ms for preprocessing, 33.7ms for inference, and 4.3ms for postprocessing per image. Overall, the model shows promising performance for pest detection. However, there is still room for improvement, particularly in the detection of aphids.

## Demo 🦟
This is the demonstration of the model inferenced in a test video.

![result](https://github.com/spoodzxs2345/pest-detection/assets/104749581/a4ea3f94-d186-4fdf-ab59-fa6f2180c6b3)


## Additional sources 📖
- [YOLOv8 Ultralytics Documentation](https://docs.ultralytics.com/)
- [About YOLOv8](https://github.com/ultralytics/ultralytics)
- [YOLOv8 using Google Colab](https://github.com/roboflow/notebooks/blob/main/notebooks/train-yolov8-object-detection-on-custom-dataset.ipynb)
