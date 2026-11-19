"""光栅化：Bresenham、裁剪与圆：待实现的核心模块。"""


def bresenham(x0, y0, x1, y1):
    """Bresenham 直线。"""
    raise NotImplementedError

def clip_line(x0, y0, x1, y1, rect):
    """线段裁剪。"""
    raise NotImplementedError

def midpoint_circle(cx, cy, r):
    """中点圆。"""
    raise NotImplementedError

def rect_contains(rect, point):
    """矩形包含。"""
    raise NotImplementedError

def fill_span(y, x0, x1):
    """水平填充。"""
    raise NotImplementedError
