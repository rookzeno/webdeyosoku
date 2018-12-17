import numpy as np
from keras.preprocessing import image
from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from keras.models import load_model

class imagenet():
    def __init__(self,img):
        img = image.load_img(img, target_size=(224, 224))
        img = image.img_to_array(img).reshape(1,224,224,3)
        self.img = img
    def load_image(filename):
        img = image.load_img(filename, target_size=(224, 224))
        return image.img_to_array(img)
    def deep(self):
        print("")
        model = load_model("./model/kerasresnet50.h5")
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
