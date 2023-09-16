from mathematical.Vec3 import Vec3


def main():
    a = Vec3(3, -3, 1)
    b = Vec3(4, 9, 2)
    c = Vec3.cross(a, b)

    print(f"a: {a}")
    print(f"b: {b}")
    print(f"a x b: {c}")
