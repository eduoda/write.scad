write.scad
==========
A simple way to use strings in openscad


howto
=====
Put the files atoi.scad, write.scad and GaroaHackerClubeBold.dxf in the same directory of your openscad project. Use like in the example:
include <write.scad>
translate([-38,-38,0]) rotate([20,0,45])
	write("i'm a fucking genius",10);

blablabla
=========
The script svggen.py generates a svg with all printable latin1 chars.

The generate svg needs to be converted to a dxf file. It's done with Inkscape and a modified version of the Inkscape-OpenSCAD-DXF-Export exension (https://github.com/brad/Inkscape-OpenSCAD-DXF-Export). At this point yout need the GaroaHackerClubeBold.otf to be installed on your system. If you want to use another font, just edit the svggen.py and create a new dfx file.

The script atoigen.py generates the function atoi that converts a string to its ascii number.
