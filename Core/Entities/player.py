from .creature import Creature, Limb
from Game.Core.skill_system import Skills
from Game.Utils.directions import Orientation


class Character(Creature):
    def __init__(self, name, size, pos, skin_desc, msg_func):
        head = Limb("Head", 100, 95, Orientation.UP, skin_desc)
        neck = Limb("Neck", 100, 100, Orientation.UP, skin_desc)

        left_arm = Limb("Left Arm", 100, 50, Orientation.LEFT, skin_desc)
        left_elbow = Limb("Left Elbow", 100, 60, Orientation.LEFT, skin_desc)
        left_wrist = Limb("Left Wrist", 100, 60, Orientation.LEFT, skin_desc)

        left_leg = Limb("Left Leg", 100, 40, Orientation.LEFT, skin_desc)
        left_knee = Limb("Left Knee", 100, 60, Orientation.LEFT, skin_desc)
        left_ankle = Limb("Left Ankle", 100, 60, Orientation.LEFT, skin_desc)

        right_arm = Limb("Right Arm", 100, 50, Orientation.RIGHT, skin_desc)
        right_elbow = Limb("Right Elbow", 100, 60, Orientation.RIGHT, skin_desc)
        right_wrist = Limb("Right Wrist", 100, 60, Orientation.RIGHT, skin_desc)

        right_leg = Limb("Right Leg", 100, 40, Orientation.RIGHT, skin_desc)
        right_knee = Limb("Right Knee", 100, 60, Orientation.RIGHT, skin_desc)
        right_ankle = Limb("Right Ankle", 100, 60, Orientation.RIGHT, skin_desc)

        chest = Limb("Chest", 100, 80, Orientation.MIDDLE, skin_desc)
        stomach = Limb("Stomach", 100, 80, Orientation.MIDDLE, skin_desc)

        limbs = [head, neck, left_arm, left_elbow, left_wrist, left_leg, left_knee, left_ankle, right_ankle, right_arm,
                 right_elbow, right_wrist, right_leg, right_knee, chest, stomach]

        self.skills = Skills()
        self.send = msg_func
        super().__init__(name, size, pos, limbs)

    def describe(self):
        text = ""
        for limb in self.limbs:
            text += limb.describe() + ", "
        return text

    def add_xp(self, skill: str, amount: int):
        self.skills.add_xp(skill, amount)
