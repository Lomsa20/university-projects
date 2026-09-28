class Point3D:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def __str__(self):
        return f'({self._x}, {self._y}, {self._z})'


class Cube:
    def __init__(self, corner, side):
        self._corner = corner      # Point3D
        self._side = side          # number

    def volume(self):
        return self._side ** 3

    def __add__(self, other):
        min_x = min(self._corner._x, other._corner._x)
        min_y = min(self._corner._y, other._corner._y)
        min_z = min(self._corner._z, other._corner._z)

        max_x = max(self._corner._x + self._side,
                    other._corner._x + other._side)
        max_y = max(self._corner._y + self._side,
                    other._corner._y + other._side)
        max_z = max(self._corner._z + self._side,
                    other._corner._z + other._side)

        new_side = max(
            max_x - min_x,
            max_y - min_y,
            max_z - min_z
        )

        return Cube(Point3D(min_x, min_y, min_z), new_side)

    def __str__(self):
        return f'Cube at {self._corner} with side {self._side}'
c1 = Cube(Point3D(0, 0, 0), 2)
c2 = Cube(Point3D(1, 1, 1), 3)

c3 = c1 + c2

print(c1)
print(c2)
print(c3)
print("Volume:", c3.volume())
