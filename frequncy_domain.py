import cv2
import numpy as np
from matplotlib import pyplot as plt

def image_to_frequency_domain(image):
    """
    Transform an image to the frequency domain using FFT.
    
    Parameters:
    image (numpy.ndarray): Input image.
    
    Returns:
    numpy.ndarray: Frequency domain representation of the image.
    """
    # Perform FFT
    frequncies = np.fft.fft2(image)
    fshift = np.fft.fftshift(frequncies)
    magnitude_spectrum = 20 * np.log(np.abs(fshift))
    
    return magnitude_spectrum, fshift

# Create a circular low pass filter


def low_pass_filter(image,radius):
    fft_image = np.fft.fft2(image)
    fft_shifted = np.fft.fftshift(fft_image)

    rows, cols = image.shape
    center_row, center_col = rows // 2, cols // 2
    x, y = np.ogrid[:rows, :cols]
    mask = np.zeros((rows, cols))
    mask[(x - center_row) ** 2 + (y- center_col) ** 2 <= radius ** 2] = 1
    masked_image=fft_shifted *mask
    ifft_shifted_filtered = np.fft.ifftshift(masked_image)
    ifft_filtered = np.fft.ifft2(ifft_shifted_filtered)

    # Convert back to uint8
    filtered_image = np.abs(ifft_filtered).astype(np.uint8)
    return filtered_image

def high_pass_filter(image,radius):
    fft_image = np.fft.fft2(image)
    fft_shifted = np.fft.fftshift(fft_image)

    rows, cols = image.shape
    center_row, center_col = rows // 2, cols // 2
    x, y = np.ogrid[:rows, :cols]
    # print(x , y)
    mask = np.ones((rows, cols))
    mask[(x - center_row) ** 2 + (y- center_col) ** 2 <= radius ** 2] = 0


    masked_image=fft_shifted *mask

    ifft_shifted_filtered = np.fft.ifftshift(masked_image)
    ifft_filtered = np.fft.ifft2(ifft_shifted_filtered)

    # Convert back to uint8
    filtered_image = np.abs(ifft_filtered).astype(np.uint8)
    return filtered_image

def hyprid(image1, image2,radius1,radius2):
    """
    Create a hybrid image by combining a low-pass filtered version of image1 with a high-pass filtered version of image2.
    
    Parameters:
    image1 (numpy.ndarray): Input image 1.
    image2 (numpy.ndarray): Input image 2.
    radius1 (int): Radius for the low-pass filter.
    radius2 (int): Radius for the high-pass filter.
    
    Returns:
    numpy.ndarray: Hybrid image.
    """
    # Ensure both images are of the same size
    if image1.shape != image2.shape:
        image2=cv2.resize(image2 ,(  image1.shape[1] , image1.shape[0] ))
    
    # Perform FFT on both images
    hyprid_low_pass = low_pass_filter(image1, radius1)
    hyprid_high_pass = high_pass_filter(image2, radius2)
    
    # Combine the low-pass and high-pass filtered images
    hybrid_image = hyprid_low_pass + hyprid_high_pass
    
    # Clip the values to be in the valid range for image data
    hybrid_image = np.clip(hybrid_image, 0, 255).astype(np.uint8)
    
    return hybrid_image


    