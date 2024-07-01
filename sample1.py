import cv2
import os
import numpy as np
import smartcrop.Generator as Generator
# Load cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def evaluate_image_quality(image, original_image):
    """
    Evaluate image quality based on edge content, face presence, and histogram analysis.
    """
    # Edge detection
    edges = cv2.Canny(image, 100, 200)
    edge_score = np.sum(edges) / (image.shape[0] * image.shape[1])

    # Face detection
    faces = face_cascade.detectMultiScale(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), 1.3, 5)
    face_score = len(faces)

    # Histogram analysis
    hist_original = cv2.calcHist([cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)], [0], None, [256], [0, 256])
    hist_crop = cv2.calcHist([cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)], [0], None, [256], [0, 256])
    hist_score = cv2.compareHist(hist_original, hist_crop, cv2.HISTCMP_CORREL)

    # Combine scores (weights can be adjusted)
    total_score = edge_score + face_score * 10 + hist_score * 5
    return total_score

def auto_optimal_smart_crop(image, target_width, target_height, destination):
    # Paths to save temporary images
    temp_output_resize = "temp_resize.jpg"
    temp_output_no_resize = "temp_no_resize.jpg"

    # Perform smart crop with resizing
    Generator.smart_crop(image, target_width, target_height, temp_output_resize, do_resize=True)
    
    # Perform smart crop without resizing
    Generator.smart_crop(image, target_width, target_height, temp_output_no_resize, do_resize=False)

    # Load both results
    resized_image = cv2.imread(temp_output_resize)
    no_resized_image = cv2.imread(temp_output_no_resize)
    original_image = cv2.imread(image)

    # Evaluate the quality of both images
    resized_quality = evaluate_image_quality(resized_image, original_image)
    no_resized_quality = evaluate_image_quality(no_resized_image, original_image)

    # Choose the image with higher quality
    if resized_quality > no_resized_quality:
        optimal_image = resized_image
    else:
        optimal_image = no_resized_image

    # Save the optimal result to the destination path
    cv2.imwrite(destination, optimal_image)
    return optimal_image



# # Example usage
# img_output = "images/output/optimal_output.jpg"
# img_input = "images/input/image5.png"
# img_width = 633
# img_height = 1300

# auto_optimal_smart_crop(img_input, img_width, img_height, img_output)
