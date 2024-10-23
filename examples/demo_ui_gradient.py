from skia_gradient_array import GradientCanvas
from skia_gradient_array.ui_gradient import UiGradient
from skia_gradient_array.set_patch_background import set_patch_background


# from gradient_canvas import Point
import matplotlib.pyplot as plt

ui_gradient = UiGradient()
stops = ui_gradient.get_stops("Pinot Noir")

canvas = GradientCanvas(256, 256)
grad = canvas.makeLinear((0, 0), (256, 256), stops).get_array()


plt.style.use('dark_background')
fig, ax = plt.subplots(num=1, clear=True)

set_patch_background(fig.patch, grad)

set_patch_background(ax.patch, grad)

plt.show()


