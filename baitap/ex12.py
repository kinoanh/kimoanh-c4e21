def is_inside(point, rectangle):
    [x1, y1] = point
    [x2, y2, w, h] =  rectangle
    test_1 = x2 <= x1 <= (x2 + w) 
    test_2 = y2 <= y1 <= (y2 +h)
    if test_1 and test_2:
        return True
    else:
        return False
test1 = is_inside([200, 120], [140, 60, 100, 200])
test2 = is_inside([100, 120], [140, 60, 100, 200])
if test1 and not test2:
    print("Your function is correct")
else:
    print("Ooops, bugs detected")