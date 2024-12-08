import numpy as np
h = [1.69, 1.76, 1.83, 1.86, 1.77, 1.73]
w = [86, 74, 59, 95, 80, 68]

hn = np.array(h)
wn = np.array(w)

bmi = wn / hn ** 2
print(bmi)