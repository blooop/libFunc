from solid import *
from solid.utils import *
from libFunc.mathfuncs import *

def circularPattern(object, count, startAngle=0.0, endAngle=360.0, origin=None):
    if origin is None:
        origin = Vector3()
    # translate(-origin)
    output = []
    for i in range(count):
        angle = lerp(i, 0, count, startAngle, endAngle)
        output.append(rotate(angle)(object))
    return union()(output)