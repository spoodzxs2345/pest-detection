import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('C:/Users/PCX/Desktop/projects/object_counter_v3/best.pt')

# Open the video file
video_path = "C:/Users/PCX/Desktop/projects/object_counter_v3/test_video.mp4"
cap = cv2.VideoCapture(video_path)

out = cv2.VideoWriter('C:/Users/PCX/Desktop/projects/object_counter_v3/result.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20.0, (1280, 720))

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Write the annotated frame to the output video file
        out.write(annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
out.release()
cv2.destroyAllWindows()