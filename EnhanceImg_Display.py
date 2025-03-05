import cv2
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt

def calculate_histogram(image, mode):
    """
    Calculate the histogram of an image manually without using OpenCV's calcHist.

    Args:
        image: The input image. It can be either a grayscale or RGB image.
        mode (str): The mode of the image. It can be 'rgb' or 'gray'.

    Returns:
        list: A list containing the histogram(s) of the image.
              - For 'rgb' mode, it returns a list with three histograms (R, G, B).
              - For 'gray' mode, it returns a list with a single histogram.

    Raises:
        ValueError: If the mode is neither 'rgb' nor 'gray'.
    """
    if mode not in ('rgb', 'gray'):
        raise ValueError("Invalid mode. Use 'rgb' or 'gray'.")

    # Initialize the histogram with 256 bins (0-255)
    histogram = [0] * 256

    if mode == 'rgb':
        # Split the image into its R, G, B channels
        r_channel = image[:, :, 0]
        g_channel = image[:, :, 1]
        b_channel = image[:, :, 2]

        # Calculate histogram for each channel
        histograms = []
        for channel in [r_channel, g_channel, b_channel]:
            hist = [0] * 256
            for row in channel:
                for pixel in row:
                    hist[pixel] += 1
            histograms.append(hist)
        return histograms
    else:  # mode == 'gray'
        # Iterate through each pixel in the grayscale image
        for row in image:
            for pixel in row:
                histogram[pixel] += 1
        return [histogram]


def plot_histograms_as_array(hist, mode, title="Histogram"):
    if mode == "rgb":
        colors = ['blue', 'green', 'red']
        # labels = ['Blue Channel', 'Green Channel', 'Red Channel']
    else:
        colors = ['black']
        # labels = ['Grayscale Channel']

    fig, axs = plt.subplots(len(hist), 1, figsize=(5, 10))

    if len(hist) == 1:
        axs = [axs]  # Handle case for grayscale where axs is not a list.

    for i, color in enumerate(colors):
        axs[i].bar(np.arange(256), hist[i], color=color, width=1)
        # axs[i].set_title(f'{labels[i]}', fontsize=10, color=color)

        axs[i].set_xlim([0, 255])
        axs[i].set_facecolor('#F5F5F5')
        axs[i].spines['top'].set_visible(False)
        axs[i].spines['right'].set_visible(False)

    plt.suptitle(title, fontsize=12)
    plt.tight_layout()

    fig.canvas.draw()
    img = np.frombuffer(fig.canvas.buffer_rgba(), dtype=np.uint8)
    img = img.reshape(fig.canvas.get_width_height()[::-1] + (4,))  # RGBA

    img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)  # Convert to RGB (optional if you want to match before)

    plt.close(fig)
    return img

def plot_cdf_as_array(hist, mode, title="Cumulative Distribution Function (CDF)"):
    """
    Calculate and plot the Cumulative Distribution Function (CDF) of an image histogram manually.
    
    Args:
        hist: The histogram of the image. For 'rgb' mode, it's a list of three histograms (R, G, B).
             For 'gray' mode, it's a single histogram.
        mode (str): The mode of the image. It can be 'rgb' or 'gray'.
        title (str): The title for the plot.

    Returns:
        img: The plot of the CDF as an image array.
    """
    if mode not in ('rgb', 'gray'):
        raise ValueError("Invalid mode. Use 'rgb' or 'gray'.")

    if mode == "rgb":
        colors = ['blue', 'green', 'red']
        num_channels = 3
    else:
        colors = ['black']
        num_channels = 1

    # Create a figure with subplots for each channel
    fig, axs = plt.subplots(num_channels, 1, figsize=(5, 10))
    if num_channels == 1:
        axs = [axs]  # Handle grayscale case

    for i in range(num_channels):
        if num_channels == 1:
            channel_hist = hist[0]
        else:
            channel_hist = hist[i]

        # Initialize CDF
        cdf = [0] * 256
        running_total = 0

        # Calculate running sum manually
        for intensity in range(256):
            running_total += channel_hist[intensity]
            cdf[intensity] = running_total

        # Normalize CDF
        total_pixels = running_total
        if total_pixels != 0:
            cdf = [value / total_pixels for value in cdf]
        else:
            # Handle case where there are no pixels (shouldn't happen with valid histogram)
            cdf = [0.0 for _ in range(256)]

        # Plot the CDF
        axs[i].plot(cdf, color=colors[i], linewidth=1.5)
        axs[i].set_xlim([0, 255])
        axs[i].set_ylim([0, 1])
        axs[i].set_facecolor('#F5F5F5')
        axs[i].spines['top'].set_visible(False)
        axs[i].spines['right'].set_visible(False)

    plt.suptitle(title, fontsize=12)
    plt.tight_layout()

    # Convert plot to image array
    fig.canvas.draw()
    img = np.frombuffer(fig.canvas.buffer_rgba(), dtype=np.uint8)
    img = img.reshape(fig.canvas.get_width_height()[::-1] + (4,))  # RGBA

    img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)  # Convert to RGB

    plt.close(fig)
    return img

def process_image(file_path, mode="rgb"):
    """
    Process an image and return the image with the histogram and CDF.

    Args:
        file_path (str): The path to the image.
        mode (str): The mode to process the image. Default is 'rgb'.

    Returns:
        numpy.ndarray: The processed image.
    """
    

    if mode not in ["rgb", "gray"]:
        raise ValueError("Mode must be 'rgb' or 'gray'.")

    image = cv2.imread(file_path)

    if mode == "rgb":
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    else:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    height, width = image.shape[:2]

    # Calculate histogram
    hist = calculate_histogram(image, mode)

    # Generate images (histogram & CDF)
    hist_bars_img = plot_histograms_as_array(hist, mode, title=f"{mode.upper()} Histogram")
    cdf_img = plot_cdf_as_array(hist, mode, title=f"{mode.upper()} CDF")

    # Resize both to match original image size
    hist_bars_img = cv2.resize(hist_bars_img, (width, height))
    cdf_img = cv2.resize(cdf_img, (width, height))

    return hist_bars_img, cdf_img, hist




def process_image(image, mode="rgb"):
    """
    Args:
        image (numpy.ndarray): Image to process.
        mode (str, optional): Mode to process image. Defaults to "rgb".

    Returns:
        numpy.ndarray: Histogram image.
        numpy.ndarray: CDF image.
    """
    

    height, width = image.shape[:2]

    # Calculate histogram
    hist = calculate_histogram(image, mode)

    # Generate images (histogram & CDF)
    hist_bars_img = plot_histograms_as_array(hist, mode, title=f"{mode.upper()} Histogram")
    cdf_img = plot_cdf_as_array(hist, mode, title=f"{mode.upper()} CDF")

    # Resize both to match original image size
    hist_bars_img = cv2.resize(hist_bars_img, (width, height))
    cdf_img = cv2.resize(cdf_img, (width, height))

    return hist_bars_img, cdf_img



def equalize_image(image):
    """
    Equalize the image 
    Args:
        image (numpy.ndarray): Image to equalize.

    Returns:
        numpy.ndarray: Equalized image.
    """
    
    # Step 1: Calculate the histogram of the image
    hist = np.zeros(256, dtype=int)
    for pixel in image.flatten():
        hist[pixel] += 1



    # Step 2: Compute the cumulative distribution function (CDF)
    cdf = np.zeros(256, dtype=int)
    cdf[0] = hist[0]
    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + hist[i]

    # Step 3: Normalize the CDF
    cdf_min = cdf.min()
    cdf_max = cdf.max()
    cdf_normalized = ((cdf - cdf_min) * 255 / (cdf_max - cdf_min)).astype(np.uint8)

    # Step 4: Map the original pixel values to the equalized values using the normalized CDF
    equalized_image = np.zeros_like(image, dtype=np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            equalized_image[i, j] = cdf_normalized[image[i, j]]

    return equalized_image

def normalize_image(image):
    min_val = np.min(image)
    max_val = np.max(image)
    normalized_image = ((image - min_val) /
                        (max_val - min_val)) * 255

    # Convert to uint8 data type (required for image display)
    normalized_image = normalized_image.astype(np.uint8)
    return normalized_image



def manual_global_threshold(image):
    global_thresh_value = 128
    max_value = 255

    # Initialize the output image with zeros (all black)
    thresh_image = np.zeros_like(image)

    # Get the dimensions of the image
    rows, cols = image.shape[:2]

    # Loop over each pixel in the image
    for i in range(rows):
        for j in range(cols):
            # Apply the threshold
            if image[i, j] >= global_thresh_value:
                thresh_image[i, j] = max_value
            else:
                thresh_image[i, j] = 0

    return thresh_image

def manual_local_threshold(image):
    block_size = 11
    c = 2
    max_value = 255
    # Create an image to store the thresholded result
    thresh_image = np.zeros_like(image)

    # Ensure block_size is odd
    if block_size % 2 == 0:
        block_size += 1

    # Pad the image to handle the border pixels
    pad_size = block_size // 2
    padded_image = cv2.copyMakeBorder(
        image, pad_size, pad_size, pad_size, pad_size, cv2.BORDER_REPLICATE)

    # Iterate over each pixel in the image
    for y in range(image.shape[0]):
            for x in range(image.shape[1]):
                block = padded_image[y:y+block_size, x:x+block_size]
                mean = np.mean(block)
                if image[y, x] > mean - c:
                    thresh_image[y, x] = max_value
                else:
                    thresh_image[y, x] = 0

    return thresh_image

