from os import listdir
from PIL import Image
    
for filename in listdir('./kitti/trainB'):
  if filename.endswith('.png'):
    try:
      img = Image.open('./'+filename) # open the image file
      img.verify() # verify that it is, in fact an image
    except (IOError, SyntaxError) as e:
      print('Bad file:', filename) # print out the names of corrupt files
