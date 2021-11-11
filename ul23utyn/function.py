import numpy as np
# from ipywidgets import interact, fixed
from PIL import Image

def imshow(X,resize=None):
    if type(X).__module__ == np.__name__:
        im=Image.fromarray(X)
    else:
        im=X
    resized_im=im.resize(resize)
    resized_im.show()
    return resized_im