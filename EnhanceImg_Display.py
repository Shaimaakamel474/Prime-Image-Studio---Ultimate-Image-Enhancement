import cv2
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt

def calculate_histogram(image, mode):
    if mode == "rgb":
        hist = [cv2.calcHist([image], [i], None, [256], [0, 256]).flatten() for i in range(3)]
    elif mode == "gray":
        hist = [cv2.calcHist([image], [0], None, [256], [0, 256]).flatten()]
    else:
        raise ValueError("Invalid mode. Use 'rgb' or 'gray'.")
    return hist

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
    if mode == "rgb":
        colors = ['blue', 'green', 'red']
        # labels = ['Blue Channel', 'Green Channel', 'Red Channel']
    else:
        colors = ['black']
        # labels = ['Grayscale Channel']

    fig, axs = plt.subplots(len(hist), 1, figsize=(5, 10))

    if len(hist) == 1:
        axs = [axs]  # Handle grayscale case.

    for i, color in enumerate(colors):
        cdf = np.cumsum(hist[i])
        cdf = cdf / cdf[-1]

        axs[i].plot(cdf, color=color, linewidth=1.5)
        # axs[i].set_title(f'{labels[i]} (CDF)', fontsize=10, color=color)

        axs[i].set_xlim([0, 255])
        axs[i].set_ylim([0, 1])
        axs[i].set_facecolor('#F5F5F5')
        axs[i].spines['top'].set_visible(False)
        axs[i].spines['right'].set_visible(False)

    plt.suptitle(title, fontsize=12)
    plt.tight_layout()

    fig.canvas.draw()
    img = np.frombuffer(fig.canvas.buffer_rgba(), dtype=np.uint8)
    img = img.reshape(fig.canvas.get_width_height()[::-1] + (4,))  # RGBA

    img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)  # Convert to RGB (optional)

    plt.close(fig)
    return img

def process_image(file_path, mode="rgb"):
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
    # get the histogram of the image
    hist, bins = np.histogram(image.flatten(), 256, [0, 256])

    # get the Cumulative Distribution Function
    cdf = hist.cumsum()

    # normalization
    cdf_normalized = cdf * (255 / cdf.max())

    # mapping form original image to the cdf
    equalized_image = np.interp(
        image.flatten(), bins[:-1], cdf_normalized).reshape(image.shape)
    equalized_image = equalized_image.astype(np.uint8)

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