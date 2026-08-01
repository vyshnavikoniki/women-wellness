import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load model
model = load_model("model.h5")

# Read Image
img = cv2.imread("test.png", cv2.IMREAD_GRAYSCALE)

# Resize
img = cv2.resize(img, (28,28))

# Invert Image
img = 255 - img

# Normalize
img = img / 255.0

# Reshape
img = img.reshape(1,28,28,1)

# Predict
prediction = model.predict(img)

digit = np.argmax(prediction)

print("Predicted Digit:", digit)