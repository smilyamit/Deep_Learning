# Note learning capacity of model is in that file which has been created during actual training, here it is saved
# in model.h5 so while running this file make sure model.h5 is also in same directory 
# To save the model

#classifier.save("model.h5")  , here u can use any name eg catdog_model.h5
#print("Saved model to disk")


from keras.models import load_model
new_model = load_model('model.h5')
import numpy as np
from keras.preprocessing import image

test_image = image.load_img('/Users/koro/Desktop/Ml Practise /DL/CNN/first_cnn trial/rocky.jpeg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = new_model.predict(test_image)
#training_set.class_indices
if result[0][0] == 1:
    prediction = 'dog'
    print(f"Your image is probably 🐩  {prediction}")
else:
    prediction = 'cat'
    print(f"Your image is probably 🐈  {prediction}")

