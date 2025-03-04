import cv2
import numpy as np
from matplotlib import pyplot as plt

def image_to_frequency_domain(image):
    """
    Transform an image to the frequency domain using FFT.
    
    Parameters:
    image (numpy.ndarray): Input image (grayscale).
    
    Returns:
    tuple: Contains the magnitude spectrum and the shifted frequency spectrum.
    """
    # Perform FFT
    frequncies = np.fft.fft2(image)
    fshift = np.fft.fftshift(frequncies)
    magnitude_spectrum = 20 * np.log(np.abs(fshift))
    
    return magnitude_spectrum, fshift

def low_pass_filter(image, radius):
    """
    Apply a circular low pass filter to an image.
    
    Parameters:
    image (numpy.ndarray): Input image (grayscale).
    radius (int): Radius of the circular filter.
    
    Returns:
    numpy.ndarray: Low-pass filtered image.
    """
    # Perform FFT
    fft_image = np.fft.fft2(image)
    fft_shifted = np.fft.fftshift(fft_image)
    
    # Get image dimensions
    rows, cols = image.shape[:2]
    center_row, center_col = rows // 2, cols // 2
    
    # Create circular mask
    x, y = np.ogrid[:rows, :cols]
    mask = np.zeros((rows, cols))
    mask[(x - center_row) ** 2 + (y - center_col) ** 2 <= radius ** 2] = 1
    
    # Apply mask
    masked_image = fft_shifted * mask
    ifft_shifted_filtered = np.fft.ifftshift(masked_image)
    ifft_filtered = np.fft.ifft2(ifft_shifted_filtered)
    
    # Convert back to uint8
    filtered_image = np.abs(ifft_filtered).astype(np.uint8)
    return filtered_image

def high_pass_filter(image, radius):
    """
    Apply a circular high pass filter to an image.
    
    Parameters:
    image (numpy.ndarray): Input image (grayscale).
    radius (int): Radius of the circular filter.
    
    Returns:
    numpy.ndarray: High-pass filtered image.
    """
    # Perform FFT
    fft_image = np.fft.fft2(image)
    fft_shifted = np.fft.fftshift(fft_image)

    # Get image dimensions
    rows, cols = image.shape[:2]
    center_row, center_col = rows // 2, cols // 2
    
    # Create circular mask
    x, y = np.ogrid[:rows, :cols]
    mask = np.ones((rows, cols))
    mask[(x - center_row) ** 2 + (y - center_col) ** 2 <= radius ** 2] = 0
    
    # Apply mask
    masked_image = fft_shifted * mask
    ifft_shifted_filtered = np.fft.ifftshift(masked_image)
    ifft_filtered = np.fft.ifft2(ifft_shifted_filtered)
    
    # Convert back to uint8
    filtered_image = np.abs(ifft_filtered).astype(np.uint8)
    return filtered_image

def hybrid(image1, image2, radius1, radius2):
    """
    Create a hybrid image by combining a low-pass filtered version of image1
    with a high-pass filtered version of image2.
    
    Parameters:
    image1 (numpy.ndarray): Input image 1 (grayscale).
    image2 (numpy.ndarray): Input image 2 (grayscale).
    radius1 (int): Radius for the low-pass filter.
    radius2 (int): Radius for the high-pass filter.
    
    Returns:
    numpy.ndarray: Hybrid image.
    """
    # Ensure both images are of the same size
    if image1.shape != image2.shape:
        image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
    
    # Convert images to floating point for FFT
    image1_fft = image1.astype(np.float32)
    image2_fft = image2.astype(np.float32)
    
    # Apply filters
    low_pass = low_pass_filter(image1_fft, radius1)
    high_pass = high_pass_filter(image2_fft, radius2)
    
    # Combine filtered images
    hybrid_image = cv2.addWeighted(low_pass, 0.5, high_pass, 0.5, 0)
    
    # Ensure proper image format
    hybrid_image = np.clip(hybrid_image, 0, 255).astype(np.uint8)
    
    return hybrid_image

