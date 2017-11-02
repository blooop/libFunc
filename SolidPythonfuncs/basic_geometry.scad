$fn = 50;

union() {
	rotate(a = 0.0000000000) {
		translate(v = [40, 0, 0]) {
			difference() {
				circle(r = 10);
				union() {
					rotate(a = 0.0000000000) {
						translate(v = [7, 0, 0]) {
							circle(r = 1);
						}
					}
					rotate(a = 90.0000000000) {
						translate(v = [7, 0, 0]) {
							circle(r = 1);
						}
					}
					rotate(a = 180.0000000000) {
						translate(v = [7, 0, 0]) {
							circle(r = 1);
						}
					}
					rotate(a = 270.0000000000) {
						translate(v = [7, 0, 0]) {
							circle(r = 1);
						}
					}
				}
			}
		}
	}
	rotate(a = 90.0000000000) {
		translate(v = [40, 0, 0]) {
			difference() {
				circle(r = 10);
				union() {
					rotate(a = 0.0000000000) {
						translate(v = [7, 0, 0]) {
							circle(r = 1);
						}
					}
					rotate(a = 90.0000000000) {
						translate(v = [7, 0, 0]) {
							circle(r = 1);
						}
					}
					rotate(a = 180.0000000000) {
						translate(v = [7, 0, 0]) {
							circle(r = 1);
						}
					}
					rotate(a = 270.0000000000) {
						translate(v = [7, 0, 0]) {
							circle(r = 1);
						}
					}
				}
			}
		}
	}
	rotate(a = 180.0000000000) {
		translate(v = [40, 0, 0]) {
			difference() {
				circle(r = 10);
				union() {
					rotate(a = 0.0000000000) {
						translate(v = [7, 0, 0]) {
							circle(r = 1);
						}
					}
					rotate(a = 90.0000000000) {
						translate(v = [7, 0, 0]) {
							circle(r = 1);
						}
					}
					rotate(a = 180.0000000000) {
						translate(v = [7, 0, 0]) {
							circle(r = 1);
						}
					}
					rotate(a = 270.0000000000) {
						translate(v = [7, 0, 0]) {
							circle(r = 1);
						}
					}
				}
			}
		}
	}
	rotate(a = 270.0000000000) {
		translate(v = [40, 0, 0]) {
			difference() {
				circle(r = 10);
				union() {
					rotate(a = 0.0000000000) {
						translate(v = [7, 0, 0]) {
							circle(r = 1);
						}
					}
					rotate(a = 90.0000000000) {
						translate(v = [7, 0, 0]) {
							circle(r = 1);
						}
					}
					rotate(a = 180.0000000000) {
						translate(v = [7, 0, 0]) {
							circle(r = 1);
						}
					}
					rotate(a = 270.0000000000) {
						translate(v = [7, 0, 0]) {
							circle(r = 1);
						}
					}
				}
			}
		}
	}
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
from __future__ import division
import os
import sys
import re

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


out_dir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
file_out = os.path.join(out_dir, 'basic_geometry.scad')


print("%(__file__)s: SCAD file written to: \n%(file_out)s" % vars())

# Adding the file_header argument as shown allows you to change
# the detail of arcs by changing the SEGMENTS variable.  This can
# be expensive when making lots of small curves, but is otherwise
# useful.
scad_render_to_file(output, file_out, file_header='$fn = %s;' % 50)
 
 
************************************************/
