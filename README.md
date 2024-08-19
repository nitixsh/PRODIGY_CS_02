# PRODIGY_CS_02
This repository contains a Python-based tool developed for image encryption and decryption using pixel manipulation techniques. The primary objective of this project is to demonstrate how simple operations on pixel values can be used to encrypt and decrypt images.

# Pixel Manipulation for Image Encryption

This repository contains a Python-based GUI tool for image encryption and decryption using pixel manipulation techniques. Users can apply various operations such as pixel swapping, inversion, and mathematical adjustments to encrypt and decrypt images.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project provides a simple yet effective tool for image encryption and decryption using pixel manipulation. The tool is built using Python and Tkinter, offering a graphical interface that allows users to upload an image, apply encryption, and then decrypt the image to retrieve the original.

## Features
- **Image Upload:** Upload any image file (PNG, JPEG) to start the encryption process.
- **Encrypt Image:** 
  - **Pixel Swap:** Swap adjacent pixels to alter the image.
  - **Invert Colors:** Invert the colors of the image.
  - **Add 50 to Pixel Values:** Increase the pixel values by 50.
  - **Subtract 50 from Pixel Values:** Decrease the pixel values by 50.
- **Decrypt Image:** Revert the encrypted image back to its original state using the same operation used for encryption.
- **Save Image:** Save the encrypted or decrypted image to your system.

## Prerequisites
To run this program, you will need:
- Python 3.x installed on your system.
- Required Python libraries, which can be installed via pip:
  ```bash
  pip install pillow numpy
  ```
## Installation
1. **Clone the Repository:**
   ```bash
   https://github.com/nitixsh/PRODIGY_CS_02.git
   ```
2. **Install Dependencies:**
   ```bash
   pip install pillow numpy
   ```
   
## Usage
1. Run the Python script to start the GUI:
    ```bash
    python main.py
    ```
2. Use the "Upload Your Image" button to select an image file.
3. Apply encryption by selecting an operation (Swap, Invert, Add 50, Subtract 50) and clicking "Encrypt Image".
4. To decrypt the image, click on "Decrypt Image".
5. Save the processed image using the "Save Image" button.

## Examples
### Encrypting an Image
- Upload an image using the "Upload Your Image" button.
- Choose an operation, e.g., "Swap".
- The image is displayed alongside its encrypted version.

### Decrypting an Image
- After encryption, click "Decrypt Image" to revert the changes.
- The decrypted image is displayed next to the encrypted version.

## Contributing
Contributions are welcome! If you have ideas for improvements or additional features, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
