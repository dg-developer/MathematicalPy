import operator
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
        vec = Vec3(1, 2, 3)
        vec_data = vec.as_array()
        assert vec_data == [1, 2, 3]

    def test_zip(self):
        a = Vec3.new([1, 2, 3])
        b = Vec3.new([4, 5, 6])
        c = a.zip(b)
        assert c.as_array() == [(1, 4), (2, 5), (3, 6)]

    def test_zipo(self):
        a = Vec3.new([1, 2, 3])
        b = Vec3.new([4, 5, 6])

        # Default multiplication
        c = a.zipo(b)
        assert c.as_array() == [4, 10, 18]

        # Addition
        c = a.zipo(b, operator.add)
        assert c.as_array() == [5, 7, 9]

        # Custom operation
        c = a.zipo(b, lambda x1, x2: f"{x1}, {x2}")
        assert c.as_array() == ["1, 4", "2, 5", "3, 6"]

    def test_zipd(self):
        a = Vec3.new([1, 2, 3])
        b = Vec3.new([4, 5, 6])
        c = a.zipd(b)
        assert c == {
            1: 4,
            2: 5,
            3: 6
        }

    # --------------------------------------------------------------------------
    # Data access
    # --------------------------------------------------------------------------

    def test_indexing_get(self):
        a = Vec3.new([1, 2, 3])

        # Nominal access
        assert a[0] == 1
        assert a[1] == 2
        assert a[2] == 3

        # Invalid cases
        assert a[-1] == None
        assert a[-10] == None
        assert a[4] == None
        assert a[100] == None
        assert a["invalid"] == None
        assert a[None] == None

    def test_indexing_set(self):
        a = Vec3.new([1, 2, 3])

        # Nominal access
        a[0] = 4
        a[1] = 5
        a[2] = 6

        assert a[0] == 4
        assert a[1] == 5
        assert a[2] == 6

        # Reassignment
        a[1] = 7
        assert a[1] == 7

        # Invalid cases
        # Ensure doesn't throw exception
        a[-1] = 3
        a[-10] = 3
        a[4] = 3
        a[100] = 3
        a["invalid"] = 3
        a[None] = 3
        # Ensure value is not assigned for invalid index
        assert a[-1] == None
        assert a[-10] == None
        assert a[4] == None
        assert a[100] == None
        assert a["invalid"] == None
        assert a[None] == None

    # --------------------------------------------------------------------------
    # Operators
    # --------------------------------------------------------------------------

    def test_cross_product(self):
        a = Vec3(3, -3, 1)
        b = Vec3(4, 9, 2)
        c = Vec3.cross(a, b)
        assert c.as_array() == [-15, -2, 39]
