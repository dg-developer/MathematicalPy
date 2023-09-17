from mathematical.vec3 import *


def main():
    a = Vec3(3, -3, 1)
    b = Vec3(4, 9, 2)
    c = a. cross(b)

    print(f"a: {a}")
    print(f"b: {b}")
    print(f"a x b: {c}")
