import numpy as np
from keras.preprocessing import image
import tensorflow as tf
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.utils import CustomObjectScope
from keras.applications.mobilenet import MobileNet, preprocess_input, decode_predictions
from keras.models import load_model

class imagenet():
    def __init__(self,img):
        img = image.load_img(img, target_size=(128, 128))
        img = image.img_to_array(img).reshape(1,128,128,3)
        self.img = img
    def load_image(filename):
        img = image.load_img(filename, target_size=(128, 128))
        return image.img_to_array(img)
    def deep(self):
        model = MobileNet(input_shape=(128,128,3), alpha=1.0, depth_multiplier=1, dropout=1e-3, include_top=True, weights=None, input_tensor=None, pooling=None, classes=1000)
        model.load_weights("./model/kerasmobilenet.h5")
        pred = model.predict(preprocess_input(self.img))
        top = decode_predictions(pred, top=5)
        name = []
        desc = []
        score = []
        for i in range(0, len(top)):
            for j in range(0, len(top[i])):
                name1, desc1, score1 = top[i][j]
                name.append(name1)
                desc.append(desc1)
                score.append(score1*100)
        return name, desc, score
