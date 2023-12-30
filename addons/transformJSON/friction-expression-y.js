// Bindings:

cur = $frame;
def = $value;

// Calculate:

var dat = '{}'; // paste JSON here

var offset = 0; // optional offset

var cords = JSON.parse(dat);
if (offset > 0 && cur < offset) { return def; }
if (offset > 0) { cur = cur - offset; }
if (cur <= cords.length) {
    return cords[cur].y2 + cords[cur].y2 - cords[cur].y1
}
return def;
