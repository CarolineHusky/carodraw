canvas = None

def init_pygame():
    global canvas
    from .pygame import Canvas as PygameCanvas

    canvas = PygameCanvas()