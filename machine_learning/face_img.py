
from scapy import misc
import matplotlib.pyplot as plt

f=misc.face()
misc.imsave("face.png",f)
plt.imshow(f)
plt.show()


