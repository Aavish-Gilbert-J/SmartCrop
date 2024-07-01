import cv2
import os
import numpy as np
import smartcrop.Generator as Generator
# Load cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def calculate_entropy2(image):
    """
    Calculate the entropy of an image.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    hist_norm = hist.ravel()/hist.sum()
    entropy = -np.sum(hist_norm * np.log2(hist_norm + 1e-7))
    return entropy

def evaluate_image_quality2(image, original_image):
    """
    Evaluate image quality based on edge content, face presence, histogram analysis, and entropy.
    """
    # Edge detection with adaptive threshold
    edges = cv2.Canny(cv2.GaussianBlur(image, (5, 5), 0), 50, 150)
    edge_score = np.sum(edges) / (image.shape[0] * image.shape[1])

    # Face detection
    faces = face_cascade.detectMultiScale(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), 1.1, 4)
    face_score = len(faces)

    # Histogram analysis
    hist_original = cv2.calcHist([cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)], [0], None, [256], [0, 256])
    hist_crop = cv2.calcHist([cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)], [0], None, [256], [0, 256])
    hist_score = cv2.compareHist(hist_original, hist_crop, cv2.HISTCMP_CORREL)

    # Entropy measurement
    entropy_score = calculate_entropy2(image)

    # Combine scores (weights can be adjusted)
    total_score = edge_score * 0.3 + face_score * 5 + hist_score * 0.2 + entropy_score * 0.3
    return total_score

def auto_optimal_smart_crop2(image, target_width, target_height, destination):
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
    resized_quality = evaluate_image_quality2(resized_image, original_image)
    no_resized_quality = evaluate_image_quality2(no_resized_image, original_image)

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
# img_width = 990
# img_height = 1030

# auto_optimal_smart_crop2(img_input, img_width, img_height, img_output)
