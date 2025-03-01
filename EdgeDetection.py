import numpy as np
import cv2


def Sobel_Filter(image):
    height, width = image.shape
    kernel_size = 3
    padding = 1

    # Convert image to float32
    image = image.astype(np.float32)

    # Initialize output arrays
    x_filtered = np.zeros((height, width), dtype=np.float32)
    y_filtered = np.zeros((height, width), dtype=np.float32)

    # Apply padding (use BORDER_DEFAULT for better match with OpenCV)
    image_padded = cv2.copyMakeBorder(image, padding, padding, padding, padding, borderType=cv2.BORDER_DEFAULT)

    # Sobel Kernels
    kernel_x = np.array([[-1, 0, 1], 
                          [-2, 0, 2], 
                          [-1, 0, 1]], dtype=np.float32)

    kernel_y = np.array([[-1, -2, -1], 
                          [ 0,  0,  0], 
                          [ 1,  2,  1]], dtype=np.float32)

    # Flip the kernels
    kernel_x = np.flip(kernel_x) 
    kernel_y = np.flip(kernel_y) 


    # Apply convolution manually
    for i in range(height):
        for j in range(width):
            region = image_padded[i:i+kernel_size, j:j+kernel_size]
            x_filtered[i, j] = np.multiply(region, kernel_x).sum()
            y_filtered[i, j] = np.multiply(region, kernel_y).sum()

    # Convert to uint8 (for visualization)
    x_filtered_uint8 = cv2.convertScaleAbs(x_filtered)
    y_filtered_uint8 = cv2.convertScaleAbs(y_filtered)

    # # OpenCV's Sobel for comparison
    # opencv_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    # opencv_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # opencv_x = cv2.convertScaleAbs(opencv_x)
    # opencv_y = cv2.convertScaleAbs(opencv_y)

    # # Check if the results match
    # print("Does x_filtered match OpenCV? ", np.allclose(opencv_x, x_filtered_uint8, atol=1))
    # print("Does y_filtered match OpenCV? ", np.allclose(opencv_y, y_filtered_uint8, atol=1))

    return x_filtered_uint8, y_filtered_uint8






def Prewitt_Filter(image):
    height, width = image.shape
    kernel_size = 3
    padding = 1

    # Convert image to float32
    image = image.astype(np.float32)

    # Initialize output arrays
    x_filtered = np.zeros((height, width), dtype=np.float32)
    y_filtered = np.zeros((height, width), dtype=np.float32)

    # Apply padding (use BORDER_DEFAULT for better match with OpenCV)
    image_padded = cv2.copyMakeBorder(image, padding, padding, padding, padding, borderType=cv2.BORDER_DEFAULT)

    # Prewitt Kernels
    kernel_x = np.array([[-1, 0, 1], 
                          [-1, 0, 1], 
                          [-1, 0, 1]], dtype=np.float32)

    kernel_y = np.array([[-1, -1, -1], 
                          [ 0,  0,  0], 
                          [ 1,  1,  1]], dtype=np.float32)

        # Flip the kernels
    kernel_x = np.flip(kernel_x) 
    kernel_y = np.flip(kernel_y) 

    # Apply convolution manually
    for i in range(height):
        for j in range(width):
            region = image_padded[i:i+kernel_size, j:j+kernel_size]
            x_filtered[i, j] = np.multiply(region, kernel_x).sum()
            y_filtered[i, j] = np.multiply(region, kernel_y).sum()

    # Convert to uint8 (for visualization)
    x_filtered_uint8 = cv2.convertScaleAbs(x_filtered)
    y_filtered_uint8 = cv2.convertScaleAbs(y_filtered)

    # # OpenCV's Prewitt for comparison
    # opencv_x = cv2.filter2D(image, ddepth=-1, kernel=kernel_x)
    # opencv_y = cv2.filter2D(image, ddepth=-1, kernel=kernel_y)

    # opencv_x = cv2.convertScaleAbs(opencv_x)
    # opencv_y = cv2.convertScaleAbs(opencv_y)

    # # Check if the results match
    # print("Does x_filtered match OpenCV? ", np.allclose(opencv_x, x_filtered_uint8, atol=1))
    # print("Does y_filtered match OpenCV? ", np.allclose(opencv_y, y_filtered_uint8, atol=1))


    return x_filtered_uint8 , y_filtered_uint8 
    

def Robert_Filter(image):   
    height, width = image.shape
    kernel_size = 2
    padding = 1

    # Convert image to float32
    image = image.astype(np.float32)

    # Initialize output arrays
    x_filtered = np.zeros((height, width), dtype=np.float32)
    y_filtered = np.zeros((height, width), dtype=np.float32)

    # Apply padding 
    image_padded = cv2.copyMakeBorder(image, padding, padding, padding, padding, borderType=cv2.BORDER_DEFAULT)

    kernel_x = np.array([[1, 0],
                        [0, -1]] , dtype=np.float32)
    kernel_y = np.array([[0, 1],
                        [-1, 0]] , dtype=np.float32)

    # Flip the kernels
    kernel_x = np.flip(kernel_x) 
    kernel_y = np.flip(kernel_y) 

    # Apply convolution manually
    for i in range(height):
        for j in range(width):
            region = image_padded[i:i+kernel_size, j:j+kernel_size]
            x_filtered[i, j] = np.multiply(region, kernel_x).sum()
            y_filtered[i, j] = np.multiply(region, kernel_y).sum()

    # Convert to uint8 (for visualization)
    x_filtered_uint8 = cv2.convertScaleAbs(x_filtered)
    y_filtered_uint8 = cv2.convertScaleAbs(y_filtered)

    #     # OpenCV's Robert_Filter for comparison
    # opencv_x = cv2.filter2D(image, ddepth=-1, kernel=kernel_x)
    # opencv_y = cv2.filter2D(image, ddepth=-1, kernel=kernel_y)

    # opencv_x = cv2.convertScaleAbs(opencv_x)
    # opencv_y = cv2.convertScaleAbs(opencv_y)

    # # Check if the results match
    # print("Does x_filtered match OpenCV? ", np.allclose(opencv_x, x_filtered_uint8, atol=1))
    # print("Does y_filtered match OpenCV? ", np.allclose(opencv_y, y_filtered_uint8, atol=1))


    return x_filtered_uint8 , y_filtered_uint8 
    




def Canny_Filter(image):
    height, width = image.shape
    edges = cv2.Canny(image, 100, 200, apertureSize=3)
    return edges , np.full((height , width) , 255 , dtype=np.uint8)
