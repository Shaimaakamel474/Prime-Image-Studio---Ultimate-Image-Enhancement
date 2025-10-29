# Prime Image Studio 📸

<div align="center">
  <img src="./screenshots/logo.png" alt="Prime Image Studio Logo" width="200"/>
  
  ### 🎯 A Comprehensive Desktop Application for Real-Time Image Processing
  
  [![Python](https://img.shields.io/badge/Python-3.8+-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
  [![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-41CD52.svg?style=flat&logo=qt&logoColor=white)](https://pypi.org/project/PyQt5/)
  [![NumPy](https://img.shields.io/badge/NumPy-Manual_Algorithms-013243.svg?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
  [![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat)](LICENSE)
  
  <p align="center">
    <a href="#-features">Features</a> •
    <a href="#-project-structure">Structure</a> •
    <a href="#-getting-started">Getting Started</a> •
    <a href="#-gallery">Gallery</a>
  </p>
</div>

---

## 💡 Overview

Prime Image Studio is an **educational desktop application** built with Python and PyQt5, designed to help users understand image processing algorithms by implementing them **from scratch**. 

### 🌟 What Makes It Special?

> **Most core image processing algorithms**—from Sobel filters to histogram equalization—are **manually implemented using NumPy**, providing deep insight into how these operations work "under the hood."

<div align="center">
  <img src="./screenshots/main-interface.png" alt="Main Interface" width="850"/>
  <p><em>✨ Main application interface with real-time image processing capabilities</em></p>
</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🎨 Spatial Domain Analysis

<img src="./screenshots/histogram-feature.png" alt="Histogram Analysis" width="100%"/>

**Visualization Tools**
- 📊 Real-time histograms & CDFs
- 🎨 RGB & Grayscale mode toggle

**Enhancement Techniques**
- ⚡ Histogram Equalization *(Manual)*
- 📈 Min-max Normalization *(Manual)*

**Thresholding Operations**
- 🎯 Global Thresholding
- 🔍 Local Adaptive Thresholding

</td>
<td width="50%">

### 🔍 Edge Detection

<img src="./screenshots/edge-detection.png" alt="Edge Detection" width="100%"/>

**Classic Operators** *(All Manual)*
- ⚡ **Sobel Filter**
- 🔷 **Prewitt Filter**
- ✖️ **Robert's Cross**

**Advanced Detection**
- 🌟 **Canny Edge** *(OpenCV)*

*Real-time x-gradient & y-gradient visualization*

</td>
</tr>

<tr>
<td width="50%">

### 🔊 Noise & Spatial Filtering

<img src="./screenshots/noise-filtering.png" alt="Noise and Filtering" width="100%"/>

**Add Noise** - Test filter robustness
- 🎲 Gaussian Noise
- 📏 Uniform Noise
- 🧂 Salt & Pepper Noise

**Apply Filters** - Clean images *(Manual)*
- 📦 Average Filter
- 🌫️ Gaussian Filter
- 📊 Median Filter

</td>
<td width="50%">

### 🌊 Frequency Domain

<img src="./screenshots/frequency-domain.png" alt="Frequency Domain" width="100%"/>

**FFT-Based Filters**
- 🔽 **Low-Pass Filter**
  - Circular filter for blurring
  - Adjustable radius control

- 🔼 **High-Pass Filter**
  - Edge enhancement & sharpening
  - Variable frequency cutoff

- 🎭 **Hybrid Images**
  - Merge low & high frequencies
  - Create fascinating visual illusions

</td>
</tr>
</table>

---

## 📂 Project Structure

<div align="center">

```
Prime-Image-Studio/
│
├── 🎮 Main_Window.py              # Main application (Controller)
├── 🎨 Main_Window_UI_2color.ui    # Qt Designer UI file (View)
├── 🖼️  Imag_Widget.py              # Custom QWidget for image display
│
├── 📊 EnhanceImg_Display.py       # Histogram, CDF, Enhancement (Model)
├── 🔍 EdgeDetection.py            # Edge detection filters (Model)
├── 🔊 Noise_and_filter.py         # Noise & Spatial filters (Model)
└── 🌊 frequncy_domain.py          # Frequency domain filters (Model)
```

</div>

<div align="center">
<table>
<tr>
<td align="center"><b>🧠 Model</b><br/>Processing Logic</td>
<td align="center"><b>👁️ View</b><br/>User Interface</td>
<td align="center"><b>🎮 Controller</b><br/>Event Handling</td>
</tr>
<tr>
<td>Core algorithms<br/>decoupled from UI</td>
<td>Qt Designer +<br/>Custom Widgets</td>
<td>Main Window<br/>orchestration</td>
</tr>
</table>
</div>

---

## 🚀 Getting Started

### 📋 Prerequisites

<table>
<tr>
<td align="center">🐍<br/><b>Python 3.8+</b></td>
<td align="center">📦<br/><b>pip</b></td>
<td align="center">💻<br/><b>Windows/Mac/Linux</b></td>
</tr>
</table>

### 🔧 Installation

**1️⃣ Clone the repository**
```bash
git clone https://github.com/your-username/Prime-Image-Studio.git
cd Prime-Image-Studio
```

**2️⃣ Create a virtual environment** *(recommended)*
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

**3️⃣ Install dependencies**
```bash
pip install -r requirements.txt
```

Or manually install:
```bash
pip install PyQt5 numpy opencv-python matplotlib
```

**4️⃣ Run the application**
```bash
python Main_Window.py
```

---

### 🎯 Usage Guide

<div align="center">
  <img src="./screenshots/usage-demo.gif" alt="Usage Demo" width="800"/>
</div>

<table>
<tr>
<td align="center">1️⃣</td>
<td><b>Load Image</b><br/>Double-click any image panel to select your source image</td>
</tr>
<tr>
<td align="center">2️⃣</td>
<td><b>Select Mode</b><br/>Choose an operation from the radio buttons on the left</td>
</tr>
<tr>
<td align="center">3️⃣</td>
<td><b>Adjust Parameters</b><br/>Use sliders and dropdowns to fine-tune effects</td>
</tr>
<tr>
<td align="center">4️⃣</td>
<td><b>Real-time Results</b><br/>Watch processed images update instantly!</td>
</tr>
</table>

---

## 📸 Gallery

<div align="center">
  
### 🎨 See Prime Image Studio in Action

<table>
<tr>
<td align="center">
<img src="./screenshots/example-1.png" alt="Sobel Edge Detection" width="280"/>
<br/>
<sub><b>🔍 Sobel Edge Detection</b></sub>
<br/>
<sub>Manual implementation with gradient visualization</sub>
</td>
<td align="center">
<img src="./screenshots/example-2.png" alt="Histogram Equalization" width="280"/>
<br/>
<sub><b>📊 Histogram Equalization</b></sub>
<br/>
<sub>Enhanced contrast using custom algorithm</sub>
</td>
<td align="center">
<img src="./screenshots/example-3.png" alt="Hybrid Image" width="280"/>
<br/>
<sub><b>🎭 Hybrid Image</b></sub>
<br/>
<sub>Frequency domain manipulation magic</sub>
</td>
</tr>
</table>

</div>

---

## 📄 License

<div align="center">

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License - Free to use, modify, and distribute
```

</div>

---

