# Prime Image Studio 📸

<div align="center">
  <img src="./screenshots/logo.png" alt="Prime Image Studio Logo" width="200"/>
  
  **A comprehensive desktop application for real-time image processing and analysis**
  
  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
  [![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)](https://pypi.org/project/PyQt5/)
  [![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
</div>

---

## 📖 Overview

Prime Image Studio is an educational desktop application built with Python and PyQt5, designed to help users understand image processing algorithms by implementing them from scratch. What makes this project unique is that **most core image processing algorithms**—from Sobel filters to histogram equalization—are manually implemented using NumPy, providing insight into how these operations work "under the hood."

<div align="center">
  <img src="./screenshots/main-interface.png" alt="Main Interface" width="800"/>
  <p><em>Main application interface with real-time image processing</em></p>
</div>

---

## ✨ Features

### 🎨 Spatial Domain Analysis & Enhancement

<img src="./screenshots/histogram-feature.png" alt="Histogram Analysis" align="right" width="400"/>

- **Histogram & CDF Visualization**
  - Real-time, auto-updating histograms
  - Cumulative Distribution Functions (CDFs)
  
- **RGB & Grayscale Modes**
  - Toggle between full RGB (channel-separated) and grayscale analysis
  
- **Enhancement Techniques**
  - **Histogram Equalization**: Manual implementation for contrast enhancement
  - **Normalization**: Min-max normalization to stretch pixel intensity values
  
- **Thresholding Operations**
  - **Global Thresholding**: Fixed-value manual threshold
  - **Local (Adaptive) Thresholding**: Adaptive mean threshold for varying lighting

<br clear="right"/>

### 🔍 Edge Detection

<img src="./screenshots/edge-detection.png" alt="Edge Detection" align="right" width="400"/>

Apply classic edge detection operators with instant x-gradient and y-gradient visualization:

- **Sobel Filter** (Manual Implementation)
- **Prewitt Filter** (Manual Implementation)
- **Robert's Cross** (Manual Implementation)
- **Canny Edge Detector** (OpenCV Implementation)

<br clear="right"/>

### 🔊 Noise & Spatial Filtering

<img src="./screenshots/noise-filtering.png" alt="Noise and Filtering" align="right" width="400"/>

**Add Noise:** Test filter robustness with various noise types
- Gaussian Noise
- Uniform Noise
- Salt & Pepper Noise

**Apply Filters:** Clean up noisy images with adjustable kernel sizes
- Average Filter
- Gaussian Filter
- Median Filter

<br clear="right"/>

### 🌊 Frequency Domain Processing

<img src="./screenshots/frequency-domain.png" alt="Frequency Domain" align="right" width="400"/>

- **Low-Pass Filter**: Circular filter with adjustable radius for image blurring
- **High-Pass Filter**: Circular filter for sharpening and edge enhancement
- **Hybrid Images**: Combine low-frequency components from one image with high-frequency components from another

<br clear="right"/>



---
## 📂 Project Structure

```
Prime-Image-Studio/
│
├── 📜 Main_Window.py              # Main application (Controller)
├── 📜 Main_Window_UI_2color.ui    # Qt Designer UI file (View)
├── 📜 Imag_Widget.py              # Custom QWidget for image display
│
├── 📜 EnhanceImg_Display.py       # Histogram, CDF, Enhancement (Model)
├── 📜 EdgeDetection.py            # Edge detection filters (Model)
├── 📜 Noise_and_filter.py         # Noise & Spatial filters (Model)
└── 📜 frequncy_domain.py          # Frequency domain filters (Model)

```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Prime-Image-Studio.git
   cd Prime-Image-Studio
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or manually install:
   ```bash
   pip install PyQt5 numpy opencv-python matplotlib
   ```

4. **Run the application**
   ```bash
   python Main_Window.py
   ```

### Usage Guide

<img src="./screenshots/usage-demo.gif" alt="Usage Demo" width="800"/>

1. **Load Image**: Double-click any image panel to load your source image
2. **Select Mode**: Choose an operation mode from the radio buttons on the left
3. **Adjust Parameters**: Use sliders and options to fine-tune the effect
4. **Real-time Results**: See processed images update instantly!




## 📸 Gallery

<div align="center">
  <table>
    <tr>
      <td><img src="./screenshots/example-1.png" alt="Example 1" width="300"/></td>
      <td><img src="./screenshots/example-2.png" alt="Example 2" width="300"/></td>
      <td><img src="./screenshots/example-3.png" alt="Example 3" width="300"/></td>
    </tr>
    <tr>
      <td align="center"><em>Sobel Edge Detection</em></td>
      <td align="center"><em>Histogram Equalization</em></td>
      <td align="center"><em>Hybrid Image</em></td>
    </tr>
  </table>
</div>


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to the PyQt5 and OpenCV communities for excellent documentation
- Inspired by classical image processing textbooks and courses
- Built as an educational tool for understanding computer vision fundamentals

---
