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
 
ó
Â|űYc           @   s   d  d l  m Z d  d l Z d  d l Z d  d l Z d  d l Td  d l Td d  Z e d k r| e	 d  Z
 e e
 d  n  d S(	   i˙˙˙˙(   t   divisionN(   t   *i2   c         C   sm   t  t j  d k r" t j d n t j } t j j | d  } d t   GHt |  | d d | d t	 d  S(   Ni   s   basic_geometry.scads   saved: %(fileName)st   file_headers	   $fn = %s;t   include_orig_code(
   t   lent   syst   argvt   ost   curdirt   patht   joint   varst   scad_render_to_filet   True(   t   objt   fileNamet   segmentst   out_dirt   file_out(    (    sC   D:\Dropbox\src\Python\SolidPython\libFunc\SolidPythonfuncs\utils.pyt
   renderSCAD	   s    +t   __main__i   s	   test.scad(   t
   __future__R    R   R   t   ret   solidt   solid.utilsR   t   __name__t   circlet   a(    (    (    sC   D:\Dropbox\src\Python\SolidPython\libFunc\SolidPythonfuncs\utils.pyt   <module>   s   


 
 
************************************************/
