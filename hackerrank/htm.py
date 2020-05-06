import PIL
import numpy as np
from PIL import Image

im = np.array(PIL.Image.open('Gull_portrait_ca_usa.jpg').convert('L').resize((256, 256)))
print(type(im))
