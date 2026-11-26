import sys
sys.path.insert(0, 'scripts')
from fig_geo import *
from shapely.geometry import LineString

body = ell(54, 66, 40, 14.5, -6)
chest = ell(88, 62, 15, 16)
head = circle(100, 36, 9.5)
neck = ell(94, 49, 11.5, 14, rot=12)
beak = poly([(106, 32), (124, 35), (126, 38), (107, 43)])
tail = ell(20, 63, 17, 8, rot=-16)
g = comb(body, chest, head, neck, beak, tail)
g = g.buffer(2.2).buffer(-2.2)
d, _ = to_path(g)

leg1 = LineString([(45, 80), (45, 98)]).buffer(1.2)
leg2 = LineString([(58, 80), (58, 98)]).buffer(1.2)
foot = poly([(36, 98), (45, 104), (54, 98), (45, 100)]).buffer(0.6)

parts = []
parts.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 190" width="640" height="380">')
parts.append('<rect width="320" height="190" fill="#F7F4EE"/>')
parts.append('<g transform="translate(12,6) scale(1.75)">')
parts.append('<path d="{}" fill="#F7F4EE" stroke="#1F1B17" stroke-width="0.5"/>'.format(d))
parts.append('<path d="{}" fill="#F7F4EE" stroke="#5C544A" stroke-width="0.4"/>'.format(to_path(leg1)[0]))
parts.append('<path d="{}" fill="#F7F4EE" stroke="#5C544A" stroke-width="0.4"/>'.format(to_path(leg2)[0]))
parts.append('<path d="{}" fill="#5C544A" stroke="none" opacity="0.55"/>'.format(to_path(foot)[0]))
parts.append('<circle cx="99" cy="34" r="1.2" fill="#1F1B17"/>')
parts.append('<path d="M62,70 C52,76 36,76 26,70" fill="none" stroke="#5C544A" stroke-width="0.3"/>')
parts.append('<path d="M56,74 C48,77 38,77 30,73" fill="none" stroke="#9A9186" stroke-width="0.25"/>')
parts.append('</g></svg>')
open('/tmp/bird_test.svg', 'w').write("\n".join(parts))
import cairosvg
cairosvg.svg2png(url='/tmp/bird_test.svg', write_to='/tmp/bird_test.png', output_width=600)
print("ok")
