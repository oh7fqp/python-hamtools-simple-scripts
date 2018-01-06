#! python
import shapefile, math
output_grid_2 = r"E:\scripts\ham\maidenhead2"
output_grid_4 = r"E:\scripts\ham\maidenhead4"
dicty = {
    -90: 'A',
    -80: 'B',
    -70: 'C',
    -60: 'D',
    -50: 'E',
    -40: 'F',
    -30: 'G',
    -20: 'H',
    -10: 'I',
    0: 'J',
    10: 'K',
    20: 'L',
    30: 'M',
    40: 'N',
    50: 'O',
    60: 'P',
    70: 'Q',
    80: 'R'
    }
mh2 = shapefile.Writer(shapefile.POLYGON)
mh2.field('Locator','C',12)
mh4 = shapefile.Writer(shapefile.POLYGON)
mh4.field('Locator','C',12)
stepy = 10
stepx = 20
for y in range(0,180,stepy):
    for x in range(0,360,stepx):
        px = -180+x
        py = -90+y
        locator = dicty[px/2]+dicty[py]
        mh2.poly(parts=[[[px,py],[px,py+stepy],[px+stepx,py+stepy],[px+stepx,py],[px,py]]])
        mh2.record(locator)

mh2.save(output_grid_2)
stepy = 1
stepx = 2
for y in range(0,180,stepy):
    for x in range(0,360,stepx):
        px = -180+x
        py = -90+y
        locator = dicty[int(px/20)*10]+dicty[int(py/10)*10]+str(x/2)[-1:]+str(y)[-1:]
        mh4.poly(parts=[[[px,py],[px,py+stepy],[px+stepx,py+stepy],[px+stepx,py],[px,py]]])
        mh4.record(locator)
        print(px)

mh4.save(output_grid_4)
