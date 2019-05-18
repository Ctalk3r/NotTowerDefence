from pygame.surface import Surface
import math

def is_inside(pos, top_left, bottom_right):
    if top_left[0] <= pos[0] <= bottom_right[0] and top_left[1] <= pos[1] <= bottom_right[1]:
        return True
    return False


def is_intersected(x, y):
    if x.pos[0] > y.pos[0] + y.width or x.pos[0] + x.width < y.pos[0] or \
            x.pos[1] > y.pos[1] + y.height or x.pos[1] + x.height < y.pos[1]:
        return False
    return True


def dist(unit1, unit2):
    def ro(v1, v2):
        return math.sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2)

    def add_v(unit):
        def middle(v1, v2):
            return (v1[0] + v2[0]) / 2, (v1[1] + v2[1]) / 2

        v = list()
        v.append((unit.pos[0], unit.pos[1]))
        v.append((unit.pos[0] + unit.width, unit.pos[1]))
        v.append((unit.pos[0], unit.pos[1] + unit.height))
        v.append((unit.pos[0] + unit.width, unit.pos[1] + unit.height))
        v.append(middle(v[0], v[1]))
        v.append(middle(v[1], v[3]))
        v.append(middle(v[3], v[2]))
        v.append(middle(v[2], v[0]))

        v.append(middle(v[0], v[4]))
        v.append(middle(v[4], v[1]))
        v.append(middle(v[1], v[5]))
        v.append(middle(v[5], v[3]))
        v.append(middle(v[3], v[6]))
        v.append(middle(v[6], v[2]))
        v.append(middle(v[2], v[7]))
        v.append(middle(v[7], v[0]))
        return v

    v1 = add_v(unit1)
    v2 = add_v(unit2)

    min_dist = math.inf
    for i in range(len(v1)):
        for j in range(len(v2)):
            min_dist = min(ro(v1[i], v2[j]), min_dist)

    return min_dist
