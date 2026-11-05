from typing import Any


class Rhombus:
    def __init__(self, side_a_param: int, angle_a_param: int):
        self.side_a = side_a_param
        self.angle_a = angle_a_param

    def __setattr__(self, name: str, value: Any) -> None :
        if name == "side_a":
            if value < 0 or value == 0:
                raise ValueError("Side couldn't be equal or less than 0")
        if name == "angle_a":
            if value <= 0 or value >= 180:
                raise ValueError("Angle must be greater than 0 and less than 180")
            else:
                super().__setattr__("angle_b", 180 - value)
        super().__setattr__(name, value)

r = Rhombus(5, 60)
r.angle_a = 100
print(r.side_a)
print(r.angle_a)
print(r.angle_b)