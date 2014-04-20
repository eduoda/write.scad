include <atoi.scad>;
module _write(font,s,h,p,i) {
	if(i<len(s)){
		if(s[i]==" "){
			translate([dxf_dim(file = font, name = str(atoi("-"),"_width")),0,0])
				_write(font,s,h,p,i+1);
		}else{
			linear_extrude(height=h) import(font,layer=atoi(s[i]));		
			translate([p+dxf_dim(file = font, name = str(atoi(s[i]),"_width")),0,0])
				_write(font,s,h,p,i+1);
		}
	}
}
module write(s,h,p){
	_write("GaroaHackerClubeBold.dxf",s,h,1,0);
}
module write_custom(font,s,h,p){
	_write(font,s,h,p,0);
}
