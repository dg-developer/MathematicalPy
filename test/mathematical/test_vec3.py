import unittest

from mathematical.vec3 import Vec3


class TestVec3(unittest.TestCase):
    def setUp(self):
        pass

    def test_construction(self):
        a = Vec3(1, 2, 3)
        a_data = a.as_array()
        assert a_data == [1, 2, 3]

    def test_cross_product(self):
        a = Vec3(3, -3, 1)
        b = Vec3(4, 9, 2)
        c = Vec3.cross(a, b)
        assert c.get_data() == [-15, -2, 39]


