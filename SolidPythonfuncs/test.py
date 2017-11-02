from solid import *
from solid.utils import *

from utils import *
from patterns import *

from libFunc.mathfuncs import *

a = right(7)( circle(1))
b = circle(10)

pat = circularPattern(a,4)

output = b - pat

output = circularPattern(right(40)(output),4)

renderSCAD(output, "test.scad")
