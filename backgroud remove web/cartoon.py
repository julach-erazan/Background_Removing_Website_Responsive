import cv2
import numpy as np

def cartoonize_image(image_path, output_path):
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Unable to read image at {image_path}")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median blur to the grayscale image
    gray_blur = cv2.medianBlur(gray, 5)

    # Detect edges in the image using adaptive thresholding
    edges = cv2.adaptiveThreshold(
        gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
    )

    # Apply bilateral filter to the original image to reduce color palette
    color = cv2.bilateralFilter(img, 9, 300, 300)

    # Combine the edges with the color image
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Save the result
    cv2.imwrite(output_path, cartoon)
    print(f"Cartoon image saved at {output_path}")

# Example usage
input_image_path = '../backgroud remove web/static/uploads/before.png'
output_image_path = '../image.jpg'
cartoonize_image(input_image_path, output_image_path)
