import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Monkey-patch matplotlib_pyodide for stability
try:
    import matplotlib_pyodide.browser_backend as bb
    # Patch TimerWasm
    if hasattr(bb, "TimerWasm"):
        _old_TimerWasm_init = bb.TimerWasm.__init__

        def _new_TimerWasm_init(self, *args, **kwargs):
            self._timer = None
            _old_TimerWasm_init(self, *args, **kwargs)

        bb.TimerWasm.__init__ = _new_TimerWasm_init
    
    # Patch FigureCanvasWasm/FigureManagerWebAgg to prevent 'NoneType' object has no attribute 'parentNode'
    # This happens when plt.close() is called on a figure that was never shown or whose DOM was removed.
    if hasattr(bb, "FigureCanvasWasm"):
        _old_canvas_destroy = bb.FigureCanvasWasm.destroy
        def _new_canvas_destroy(self, *args, **kwargs):
            try:
                _old_canvas_destroy(self, *args, **kwargs)
            except Exception:
                pass
        bb.FigureCanvasWasm.destroy = _new_canvas_destroy

except Exception:
    pass

class Plot:
    def image_show(self, data):
        plt.figure()
        # image_show often expects 0-1 values or 0-255.
        # Based on UTokyo docs, 0 is black, 1 is white.
        plt.imshow(data, cmap="gray" if np.array(data).ndim == 2 else None, vmin=0, vmax=1)
        plt.axis("off")
        plt.show()

    def animation_show(self, images):
        fig = plt.figure()
        ims = []
        for img in images:
            im = plt.imshow(
                img,
                animated=True,
                cmap="gray" if np.array(img).ndim == 2 else None,
                vmin=0,
                vmax=1,
            )
            plt.axis("off")
            ims.append([im])
        # blit=False is often more stable in browser environments
        ani = animation.ArtistAnimation(fig, ims, interval=100, blit=False, repeat_delay=1000)
        plt.show()

class Array:
    def make1d(self, n):
        return [0] * n
    def make2d(self, r, c):
        return [[0] * c for _ in range(r)]

plot = Plot()
array = Array()
