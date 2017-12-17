from .creature import Creature, Limb, Orientation


class Character(Creature):
    def __init__(self, name, size, pos):
        head = Limb("Head", 100, 95, Orientation.UP, None)
        neck = Limb("Neck", 100, 100, Orientation.UP, None)

        left_arm = Limb("Left Arm", 100, 50, Orientation.LEFT, None)
        left_elbow = Limb("Left Elbow", 100, 60, Orientation.LEFT, None)
        left_wrist = Limb("Left Wrist", 100, 60, Orientation.LEFT, None)

        left_leg = Limb("Left Leg", 100, 40, Orientation.LEFT, None)
        left_knee = Limb("Left Knee", 100, 60, Orientation.LEFT, None)
        left_ankle = Limb("Left Ankle", 100, 60, Orientation.LEFT, None)

        right_arm = Limb("Right Arm", 100, 50, Orientation.RIGHT, None)
        right_elbow = Limb("Right Elbow", 100, 60, Orientation.RIGHT, None)
        right_wrist = Limb("Right Wrist", 100, 60, Orientation.RIGHT, None)

        right_leg = Limb("Right Leg", 100, 40, Orientation.RIGHT, None)
        right_knee = Limb("Right Knee", 100, 60, Orientation.RIGHT, None)
        right_ankle = Limb("Right Ankle", 100, 60, Orientation.RIGHT, None)

        chest = Limb("Chest", 100, 80, Orientation.MIDDLE, None)
        stomach = Limb("Stomach", 100, 80, Orientation.MIDDLE, None)

        limbs = [head, neck, left_arm, left_elbow, left_wrist, left_leg, left_knee, left_ankle, right_ankle, right_arm,
                 right_elbow, right_wrist, right_leg, right_knee, chest, stomach]

        super().__init__(name, size, pos, limbs)


