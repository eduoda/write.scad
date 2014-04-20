#!/usr/bin/python
chars=range(33,126+1)+[128]+range(130,140+1)+[142]+range(145,156+1)+range(158,159+1)+range(161,172+1)+range(174,255+1)
#chars=[97,105]

print '<?xml version="1.0" encoding="UTF-8" standalone="no"?><!-- Created with Inkscape (http://www.inkscape.org/) -->'
print '<svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" width="50" height="50" id="svg2" version="1.1" inkscape:version="0.48.4 r9939" sodipodi:docname="New document 1">'
print '<defs id="defs4" />'
print '<sodipodi:namedview id="base" pagecolor="#ffffff" bordercolor="#666666" borderopacity="1.0" inkscape:pageopacity="0.0" inkscape:pageshadow="2" inkscape:zoom="2" inkscape:cx="0" inkscape:cy="0" inkscape:document-units="px" inkscape:current-layer="a" showgrid="false" inkscape:window-width="1366" inkscape:window-height="721" inkscape:window-x="-3" inkscape:window-y="-3" inkscape:window-maximized="1" />'
print '<metadata id="metadata7"><rdf:RDF><cc:Work rdf:about=""><dc:format>image/svg+xml</dc:format><dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage" /><dc:title></dc:title></cc:Work></rdf:RDF></metadata>'

for n in chars:
  print '<g inkscape:label="'+str(n)+'" inkscape:groupmode="layer">'
  print '<text style="font-family:Garoa Hacker Clube;-inkscape-font-specification:Garoa Hacker Clube Bold;font-size:40px;" x="0" y="50">&#'+str(n)+';</text>'
  print '</g>'
print('</svg>')

#from PIL import ImageFont
#font = ImageFont.truetype("GaroaHackerClubeBold.otf", 40);
#print font.getsize('a')
#print font.getsize(chr(97))