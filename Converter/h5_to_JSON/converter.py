from keras.models import load_model
model = load_model("F:\\MAJOR 2\\Drowsiness_detection\\models\\cnncat2.h5")

# get the architecture as a json string


arch = model.to_json()
# save the architecture string to a file somehow, the below will work
with open('F:\\MAJOR 2\\Drowsiness_detection\\models\\cnnCat2.json', 'w') as arch_file:
    arch_file.write(arch)
# now save the weights as an HDF5 file
model.save_weights('F:\\MAJOR 2\\Drowsiness_detection\\models\\cnnCat2.h5')
