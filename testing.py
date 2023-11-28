import keras
loaded = keras.models.load_model(r"C:\Users\Administrator\Desktop\sign\my_model.h5")

img_original = r'C:\Users\Administrator\Desktop\sign\01_049.png'
img_forged = r'C:\Users\Administrator\Desktop\sign\01_049.png'

x = image.load_img(img_original, target_size=(100, 100))    
x = image.img_to_array(x)
x = tf.image.rgb_to_grayscale(x)
x = np.expand_dims(x, axis=0)
x = x/255.0

y = image.load_img(img_forged, target_size=(100, 100))    
y = image.img_to_array(y)
y = tf.image.rgb_to_grayscale(y)
y = np.expand_dims(y, axis=0)
y = y/255.0
y_pred = loaded.predict([x,y])
print(y_pred)
y_pred = np.argmax(y_pred)

if y_pred==1:
  print('Forged')
else:
  print('Real')