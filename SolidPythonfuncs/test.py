from solid import *
from solid.utils import *

from utils import *
from patterns import *

from libFunc.mathfuncs import *

a = circle(1)
b = circle(10)

def circularPattern(object, count, startAngle=0.0, endAngle=360.0, origin=None):
    if origin is None:
        origin = Vector3()
    # translate(-origin)
    output = []
    for i in range(count):
        angle = lerp(i, 0, count, startAngle, endAngle)
        print angle
        output.append(rotate(angle)(object))
    return union()(output)

pat = circularPattern(right(5)(circle(1)),4)

# b-=a
# a=b

output = b - pat

output = right(4)(output)

renderSCAD(output, "test.scad")
