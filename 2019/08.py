from pathlib import Path
from time import time
from PIL import Image

t0 = time()

################ Data Processing #################

lines = (Path(__file__).parent / "in/08.in").open().read()
lines = [int(line) for line in lines]

w = 25 #image width
h = 6 # image height
d = int(len(lines) / (w * h)) #number of layers

################ Part 1 #################

image = []
image = [lines[(i*w*h):(i*w*h)+(w*h)] for i in range(d)]
layer_index = min(layer.count(0) for layer in image)

print('ans1:',image[layer_index].count(1) * image[layer_index].count(2))

################ Part 2 #################

out = []
for i in range(w*h):
    for j in range(len(image)):
        if image[j][i] == 0:
            out.append(' ')
            break
        elif image[j][i] == 1:
            out.append('#')
            break

print('ans2:')
for i in range(0, len(out), w):
    print(*out[i:i + w], sep='')

im = Image.new('RGB', (w+2,h+2))
for i in range(h):
    for j in range(w):
        val = out[i*w + j]
        if val == '#':
            im.putpixel((j+1, i+1), (255, 255, 255, 255))

im.show()

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))