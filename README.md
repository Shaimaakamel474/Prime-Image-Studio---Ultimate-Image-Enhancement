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

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.8+ |
| **GUI Framework** | PyQt5, Qt Designer |
| **Numerical Computing** | NumPy |
| **Image Processing** | OpenCV (cv2) |
| **Visualization** | Matplotlib |

---

## 🏛️ Architecture

<div align="center">
  <img src="./screenshots/architecture-diagram.png" alt="Architecture Diagram" width="700"/>
</div>

The project follows a clean, modular, event-driven architecture similar to MVC:

### 📦 Model (Processing Logic)
Core image processing algorithms, completely decoupled from UI:
- `EdgeDetection.py` - Sobel, Prewitt, Robert filters
- `Noise_and_filter.py` - Noise generation and spatial filters
- `frequncy_domain.py` - FFT-based filters (LPF, HPF, Hybrid)
- `EnhanceImg_Display.py` - Histogram, CDF, Enhancement operations

### 🖼️ View (User Interface)
- `Main_Window_UI_2color.ui` - Qt Designer UI definition
- `Imag_Widget.py` - Custom reusable widget for image display with double-click-to-load functionality

### 🎮 Controller
- `Main_Window.py` - Central controller connecting UI events to processing functions

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
├── 📜 frequncy_domain.py          # Frequency domain filters (Model)
│
├── 📜 requirements.txt            # Project dependencies
├── 📜 README.md                   # This file
│
└── 📁 screenshots/                # Application screenshots
    ├── main-interface.png
    ├── histogram-feature.png
    ├── edge-detection.png
    ├── noise-filtering.png
    └── frequency-domain.png
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

---

## 🧪 Testing & Validation

All manual implementations were validated by comparing outputs with equivalent OpenCV functions using `np.allclose()` assertions. The code includes commented-out validation checks for Sobel, Prewitt, and Robert filters that confirmed near-identical results to their OpenCV counterparts.

<div align="center">
  <img src="./screenshots/validation-results.png" alt="Validation Results" width="600"/>
</div>

---

## 📊 Performance Comparison

| Filter Type | Manual Implementation | OpenCV Implementation |
|-------------|----------------------|----------------------|
| Sobel Edge Detection | ~850ms | ~45ms |
| Gaussian Filter (5x5) | ~920ms | ~38ms |
| Median Filter (5x5) | ~1250ms | ~65ms |

*Tested on 1920x1080 image on Intel i7 processor*

---

## 🎯 Roadmap & Future Improvements

### Performance Enhancements
- [ ] Vectorize convolution loops using NumPy array slicing
- [ ] Implement multi-threading for real-time processing
- [ ] Add GPU acceleration support (CUDA/OpenCL)

### New Features
- [ ] Morphological operations (Erosion, Dilation, Opening, Closing)
- [ ] Advanced filters (Bilateral, Laplacian of Gaussian)
- [ ] Image segmentation tools
- [ ] Batch processing support
- [ ] Export processed images with one click

### UI/UX Improvements
- [ ] Drag-and-drop image loading
- [ ] Side-by-side comparison view
- [ ] Undo/Redo functionality
- [ ] Dark mode theme
- [ ] Processing history panel

---

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

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and development process.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Your Name**

<div align="center">
  
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/your-username)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/your-username)
[![Portfolio](https://img.shields.io/badge/Portfolio-FF5722?style=for-the-badge&logo=google-chrome&logoColor=white)](https://your-website.com)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:your-email@example.com)

</div>

---

## 🙏 Acknowledgments

- Thanks to the PyQt5 and OpenCV communities for excellent documentation
- Inspired by classical image processing textbooks and courses
- Built as an educational tool for understanding computer vision fundamentals

---

<div align="center">
  <img src="./screenshots/footer-banner.png" alt="Footer Banner" width="800"/>
  
  **⭐ If you found this project helpful, please consider giving it a star! ⭐**
  
  Made with ❤️ and Python
</div>
