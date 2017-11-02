from __future__ import division
import os
import sys
import re

from solid import *
from solid.utils import *

def renderSCAD(obj,fileName,segments = 50):
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
    file_out = os.path.join(out_dir, 'basic_geometry.scad')
    print("saved: %(fileName)s" % vars())
    # Adding the file_header argument as shown allows you to change
    # the detail of arcs by changing the SEGMENTS variable.  This can
    # be expensive when making lots of small curves, but is otherwise
    # useful.
    scad_render_to_file(obj, fileName, file_header='$fn = %s;' % segments)

if __name__ == '__main__':
    a = circle(5)
    renderSCAD(a,"test.scad")


