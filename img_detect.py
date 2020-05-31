from keras.applications.resnet50 import ResNet50
from keras.applications.xception import Xception
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import os
from PIL import Image, ImageEnhance
from skimage.color import rgb2gray
from skimage import io

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
model = ResNet50(weights='imagenet')

def detectall():
    s = ['a','b','c','d','e','f','g','h','i']
    for i in range(9):
        img_path = 'im'+s[i]+'.png'
        pil_img = Image.open(img_path)
        enhancer = ImageEnhance.Sharpness(pil_img)
        enhanced_im = enhancer.enhance(10.0)

        img = image.load_img(img_path, interpolation="nearest", target_size=(224,224))


        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = model.predict(x)
        predn = decode_predictions(preds,top=3)[0]

        for j in range(3):
            print(str(i)+". "+str(predn[j][1]))

detectall()
