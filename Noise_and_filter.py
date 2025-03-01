import cv2
import numpy as np

def apply_gaussian_noise(image, mean=0, var=10):
    """
    Apply Gaussian noise to an image.
    
    Parameters:
    image (numpy.ndarray): Input image.
    mean (float): Mean of the Gaussian noise.
    var (float): Variance of the Gaussian noise.
    
    Returns:
    numpy.ndarray: Image with Gaussian noise added.
    """
    row, col = image.shape
    sigma = var ** 0.5
    gauss = np.random.normal(mean, sigma, (row, col))
    noisy = image + gauss
    return np.clip(noisy, 0, 255).astype(np.uint8)

def apply_uniform_noise(image, low=0, high=50):
    """
    Apply Uniform noise to an image.
    
    Parameters:
    image (numpy.ndarray): Input image.
    low (int): Lower bound of the uniform noise.
    high (int): Upper bound of the uniform noise.
    Returns:
    numpy.ndarray: Image with Uniform noise added.
    """
    row, col = image.shape
    uniform_noise = np.random.uniform(low, high, (row, col))
    noisy = image + uniform_noise
    return np.clip(noisy, 0, 255).astype(np.uint8)

def apply_salt_and_pepper_noise(image, salt_prob=0.05, pepper_prob=0.05):
    """
    Apply Salt-and-Pepper noise to an image.
    
    Parameters:
    image (numpy.ndarray): Input image.
    salt_prob (float): Probability of salt noise.
    pepper_prob (float): Probability of pepper noise.
    
    Returns:
    numpy.ndarray: Image with Salt-and-Pepper noise added.
    """
    row, col = image.shape
    noisy = np.copy(image)
    
    # Salt noise
    num_salt = np.ceil(salt_prob * image.size)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
   #converts the coordinates into a tuple cause numpy arrays are indexed by tuples
    noisy[tuple(coords)] = 255
    
    # Pepper noise
    num_pepper = np.ceil(pepper_prob * image.size)
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy[tuple(coords)] = 0
    return noisy

def convolve2d(image, kernel):
    """
    Apply a convolution operation to an image using a given kernel.
    
    Parameters:
    image (numpy.ndarray): Input image.
    kernel (numpy.ndarray): Convolution kernel.
    
    Returns:
    numpy.ndarray: Convolved image.
    """
    kernel = np.flipud(np.fliplr(kernel))  # Flip the kernel
    output = np.zeros_like(image)
    image_padded = np.pad(image, ((kernel.shape[0] // 2, kernel.shape[0] // 2), (kernel.shape[1] // 2, kernel.shape[1] // 2)), mode='constant')
    
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            output[y, x] = (kernel * image_padded[y: y + kernel.shape[0], x: x + kernel.shape[1]]).sum() 
    return output

def apply_gaussian_filter(image, ksize=5, sigma=1):
    """
    Apply Gaussian filter to an image.
    
    Parameters:
    image (numpy.ndarray): Input image.
    ksize (int): Kernel size.
    sigma (float): Standard deviation of the Gaussian kernel.
    
    Returns:
    numpy.ndarray: Image with Gaussian filter applied.
    """
    ax = np.linspace(-(ksize - 1) / 2., (ksize - 1) / 2., ksize)
    gauss = np.exp(-0.5 * np.square(ax) / np.square(sigma))
    kernel = np.outer(gauss, gauss)
    kernel /= np.sum(kernel)
    return convolve2d(image, kernel)

def apply_median_filter(image, ksize=5):
    """
    Apply Median filter to an image.
    
    Parameters:
    image (numpy.ndarray): Input image.
    ksize (int): Kernel size.
    
    Returns:
    numpy.ndarray: Image with Median filter applied.
    """
    output = np.zeros_like(image)
    image_padded = np.pad(image, ksize // 2, mode='constant')
    
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            output[y, x] = np.median(image_padded[y: y + ksize, x: x + ksize])  
    return output

def apply_averaging_filter(image, ksize=5):
    """
    Apply Averaging filter to an image.
    
    Parameters:
    image (numpy.ndarray): Input image.
    ksize (int): Kernel size.
    
    Returns:
    numpy.ndarray: Image with Averaging filter applied.
    """
    kernel = np.ones((ksize, ksize), np.float32) / (ksize * ksize)
    return convolve2d(image, kernel)
