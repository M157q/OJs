# http://www.checkio.org/mission/three-points-circle/

import math

def checkio(data):
    x1, y1, x2, y2, x3, y3 = map(int, filter(str.isdigit, data))

    # central point of circle (p, q)
    p = ((y1 - y3)*(y1**2 - y2**2 + x1**2 - x2**2) - (y1 - y2)*(y1**2 - y3**2 + x1**2 - x3**2)) / (2*((y1 - y3)*(x1 - x2) - (y1 - y2)*(x1 - x3)))
    q = ((x1 - x3)*(x1**2 - x2**2 + y1**2 - y2**2) - (x1 - x2)*(x1**2 - x3**2 + y1**2 - y3**2)) / (2*((x1 - x3)*(y1 - y2) - (x1 - x2)*(y1 - y3)))
    r = math.sqrt((p-x1)**2 + (q-y1)**2)

    return "(x-{p:.3g})^2+(y-{q:.3g})^2={r:.3g}^2".format(p=round(p, 2), q=round(q, 2), r=round(r, 2))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
