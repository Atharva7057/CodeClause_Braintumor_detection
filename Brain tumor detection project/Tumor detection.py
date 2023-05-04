import cv2
from keras.models import load_model
from PIL import Image
import numpy as np

model=load_model('BrainTumor10Epochs.h5')

image=cv2.imread('E:\Brain tumor detection project\pred\pred5.jpg')

img=Image.fromarray(image)

img=img.resize((64,64))

img=np.array(img)
input_img=np.expand_dims(img, axis=0)



result=model.predict(input_img)
# print(result)
if result==[0.]:
    print("No tumor found")
else:
    print("Tumor found")
