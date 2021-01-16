from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

lines = (Path(__file__).parent / "in/08.in").open().read()
lines = [int(line) for line in lines]

w = 25
h = 6
image = []

################ Part 1 #################

while True:
    if len(lines) == 0:
        break
    image.append(lines[:(w*h)])
    lines = lines[(w*h):]

count = 1e10
for i, layer in enumerate(image):
    temp = layer.count(0)
    if temp < count:
        count = temp
        layer_index = i

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

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))