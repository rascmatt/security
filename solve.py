from PIL import Image
import numpy as np
import random

password = '123456'

img = Image.open('scrambled.png')
data = np.array(img)

y_size = img.size[1]
x_size = img.size[0]

# Flatten the pixel matrix into an array
i_flat = np.full((y_size * x_size), 0, dtype=int)
for y in range(y_size):
    for x in range(x_size):
        i_flat[y*x_size + x] = data[y][x][0]

# Unshuffle:
# Initialize the 'key' array with the positions
key = np.full((y_size * x_size), 0, dtype=int)
for i in range(x_size * y_size):
    key[i] = i

# Shuffle the 'key' to find out, where the pixels
# ended up after scrambling. 
random.seed(password)
random.shuffle(key)

# Use the key to determin where to put the pixel
# at the current position
ordered = np.full((y_size * x_size, 3), (0, 0, 0), dtype=np.uint8)
for i in range(x_size * y_size):
    ordered[key[i]] = i_flat[i]

# Rebuild the pixel matrix
final = np.full((y_size, x_size, 3), (0, 0, 0), dtype=np.uint8)
for y in range(y_size):
    for x in range(x_size):
        final[y][x] = ordered[y*x_size + x]

#Image._show(Image.fromarray(final))
Image.fromarray(final).save('solved.png')