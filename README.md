# Handwritten Digit Recognition

A real-time handwritten digit recognition application built with Python, Pygame, and Keras. Draw a number on the screen, and the AI will predict which digit (0-9) it is instantly.

## 🎥 Demo

Check out the sample output video: [sample.mp4](sample.mp4)

## 🚀 Features

- **Interactive Canvas**: Draw digits freely using your mouse.
- **Real-time Prediction**: Uses a pre-trained Deep Learning model (CNN) to recognize digits immediately upon releasing the mouse.
- **Smart Preprocessing**: The application automatically crops, resizes, and centers your drawing to match the MNIST dataset format, ensuring high accuracy.
- **Visual Feedback**: Draws a bounding box around your input and displays the prediction on screen.

## 🛠️ Prerequisites

You need Python installed along with the following libraries:

- `pygame` (for the user interface)
- `numpy` (for matrix operations)
- `opencv-python` (for image processing)
- `tensorflow` / `keras` (for loading the AI model)

You can install them via pip:

```bash
pip install pygame numpy opencv-python tensorflow
```

## 📂 Project Structure

- `app.py`: The main application script.
- `Model.h5`: The pre-trained Keras model file (must be in the same directory).
- `sample.mp4`: A video demonstration of the application.

## 🎮 How to Run

1. Ensure `Model.h5` is present in the project folder.
2. Run the script:

```bash
python app.py
```

## 🕹️ Controls

| Action | Key / Mouse |
| :--- | :--- |
| **Draw** | Hold **Left Mouse Button** and move |
| **Clear Screen** | Press **'n'** on the keyboard |
| **Quit** | Close the window |

## 🧠 How It Works

To ensure the AI understands your drawing, the application performs several preprocessing steps similar to how the MNIST dataset was created:

1. **Capture**: Captures the drawing from the Pygame surface.
2. **Crop**: Calculates the bounding box of the digit to remove excess empty space.
3. **Grayscale**: Converts the image to grayscale.
4. **Resize**: Resizes the digit to fit inside a 20x20 pixel box while **preserving the aspect ratio**. This prevents the number from looking squashed or stretched.
5. **Pad**: Adds padding to center the 20x20 image inside a 28x28 black canvas.
6. **Normalize**: Scales pixel values to a range of 0.0 to 1.0.
7. **Predict**: Feeds the processed image into the Neural Network to get the result.

## 📝 Notes

- For best results, draw the number clearly in the center.
- If the prediction is wrong, press 'n' to clear the canvas completely before drawing again.