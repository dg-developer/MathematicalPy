import unittest

from mathematical.vec3 import Vec3


class TestVec3(unittest.TestCase):
    def setUp(self):
        pass

    # --------------------------------------------------------------------------
    # Builders
    # --------------------------------------------------------------------------
    def test_construction(self):
        vec = Vec3(1, 2, 3)
        assert vec.x == 1
        assert vec.y == 2
        assert vec.z == 3

        vec = Vec3.new([4, 5, 6])
        assert vec.x == 4
        assert vec.y == 5
        assert vec.z == 6

        vec = Vec3.new(iter([7, 8, 9]))
        assert vec.x == 7
        assert vec.y == 8
        assert vec.z == 9


    # --------------------------------------------------------------------------
    # Casting and conversions
    # --------------------------------------------------------------------------


    def test_array_access(self):
        a_data = a.as_array()
        assert a_data == [1, 2, 3]



    # --------------------------------------------------------------------------
    # Data access
    # --------------------------------------------------------------------------


    # --------------------------------------------------------------------------
    # Operators
    # --------------------------------------------------------------------------

    def test_cross_product(self):
        a = Vec3(3, -3, 1)
        b = Vec3(4, 9, 2)
        c = Vec3.cross(a, b)
        assert c.get_data() == [-15, -2, 39]


