from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
with tf.device("/cpu:0"):
    model = ResNet50(weight='imagenet')

    img_path = 'ima.png'
    img = image.load_img(img_path, target_size=(130,130))

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    print(decode_predictions(preds,top=3)[0])
