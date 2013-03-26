set PAINTINGS;
set COLORS;

var quantity_produced{j in PAINTINGS}, >=0, integer;

param selling_price{j in PAINTINGS};
param paint_available{i in COLORS};
param paint_needed{i in COLORS, j in PAINTINGS};

maximize revenue: sum{j in PAINTINGS} selling_price[j]*quantity_produced[j];

s.t. enough_paint{i in COLORS}: sum{j in PAINTINGS}
paint_needed[i,j]*quantity_produced[j] <= paint_available[i];

data;

set PAINTINGS := p1 p2;
set COLORS := blue green red;

param selling_price := p1 3 p2 2;
param paint_available := blue 15 green 8 red 5;

param paint_needed :
       p1   p2 :=
blue    4    2
green   1    2
red     1    1;

end;