# Image Optimizer & File Zipper

A lightweight Python utility toolkit for optimizing images and creating ZIP archives.

This project provides two simple utilities:

- 🖼️ Resize and reduce the quality of multiple images
- 📦 Create ZIP archives from files or directories

---

## ✨ Features

### 🖼️ Image Optimizer

- Resize images using a configurable resize factor
- Reduce image quality
- Process multiple images in a folder
- Automatically create the output directory
- Support common image formats:
  - JPG
  - JPEG
  - PNG
  - BMP
  - GIF

### 📦 File Zipper

- Create ZIP archives using Python's built-in `shutil` module
- Compress directories into ZIP files
- Automatically create the destination directory when needed

---

## 📁 Project Structure

```text
image-optimizer-file-zipper/
│
├── image_optimizer.py
├── file_zipper.py
├── requirements.txt
├── README.md
└── .gitignore
🛠️ Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/image-optimizer-file-zipper.git
2. Navigate to the project directory
cd image-optimizer-file-zipper
3. Install the required dependencies
pip install -r requirements.txt
🚀 Usage
🖼️ Image Optimizer

Open image_optimizer.py and configure the input and output directories:

input_folder_path = "input"
output_folder_path = "output"

You can also customize the image quality and resize factor:

process_images_in_folder(
    input_folder_path=input_folder_path,
    output_folder_path=output_folder_path,
    quality=50,
    resize_factor=0.8,
)

Then run:

python image_optimizer.py
Example

Before processing:

input/
├── photo1.jpg
├── photo2.jpg
└── photo3.png

After processing:

output/
├── photo1.jpg
├── photo2.jpg
└── photo3.png
⚙️ Configuration
Image Quality

The quality parameter controls the output image quality:

quality=50

The value is generally between 1 and 100.

Lower value → smaller file size
Higher value → better image quality

For example:

quality=30

produces a smaller file with lower quality, while:

quality=90

produces a higher-quality image with a potentially larger file size.

Resize Factor

The resize_factor parameter determines how much the image dimensions are reduced:

resize_factor=0.8

For example, an image with dimensions:

1920 × 1080

will be resized to approximately:

1536 × 864

Other examples:

resize_factor=0.5

Reduces the dimensions to 50%.

resize_factor=1.0

Keeps the original dimensions.

📦 File Zipper

Open file_zipper.py and configure the input path and output ZIP file:

input_path = "output"
output_zip = "optimized_images.zip"

Then run:

python file_zipper.py

The ZIP archive will be created at the specified location.

💡 Use Cases

This toolkit can be useful for:

Reducing image file sizes
Preparing images for websites
Processing large collections of images
Creating compressed backups
Packaging folders into ZIP archives
Automating simple file-processing tasks
Preparing images before uploading them to a website or cloud service
🧰 Technologies

This project is built with:

Python
Pillow
pathlib
shutil
📋 Requirements

Python 3.9 or newer is recommended.

Install the required Python package with:

pip install -r requirements.txt
