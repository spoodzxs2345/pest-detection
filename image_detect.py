from ultralytics import YOLO
import cv2

model = YOLO('C:/Users/PCX/Desktop/projects/object_counter_v3/best.pt')

image = cv2.imread('C:/Users/PCX/Desktop/projects/object_counter_v3/test_image.jpg')

# detect objects in the image and show the results in imshow
results = model(image)

for r in results:
    im_array = r.plot()
    cv2.imshow('image', im_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('C:/Users/PCX/Desktop/projects/object_counter_v3/image_result.jpg', im_array)