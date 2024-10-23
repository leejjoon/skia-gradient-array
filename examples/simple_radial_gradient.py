from skia_gradient_array import Stops, GradientCanvas
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1, num=2, clear=True)


stops = Stops.from_offsets_colors([0, 1],
                                  [(0.50, 1.0, 0.54), (0.39, 0.59, 0.37)])

canvas = GradientCanvas(128, 128)
arr = canvas.makeRadial((64, 64), 0,
                        (64, 64), 63*1.414,
                        stops).get_array()

ax.imshow(arr)
plt.show()
