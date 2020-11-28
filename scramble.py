from PIL import Image
import numpy as np
import random

password = '123456'

img = Image.open('./img/name.png')
data = np.array(img)

y_size = img.size[1]
x_size = img.size[0]

i_flat = np.full((y_size * x_size), 0, dtype=int)
for y in range(y_size):
    for x in range(x_size):
        i_flat[y*x_size + x] = data[y][x][0]

random.seed(password)
random.shuffle(i_flat)

out = np.full((y_size, x_size, 3), (0, 0, 0), dtype=np.uint8)
for y in range(y_size):
    for x in range(x_size):
        out[y][x] = i_flat[y*x_size + x]

Image.fromarray(out).save('scrambled.png')