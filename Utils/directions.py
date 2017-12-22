from enum import IntFlag


def rev(dic):
    ndic = {}
    for k, v in dic.items():
        for item in v:
            ndic[item] = k
    return ndic


class Orientation(IntFlag):
    NONE = 0
    UP = 1
    DOWN = 2
    MIDDLE = 4
    RIGHT = 8
    LEFT = 16
    BACK = 32


orientation_modifiers = {
    Orientation.UP: ["up", "upward", "to the top of"],
    Orientation.DOWN: ["down", "downward", "downhill"],
    Orientation.MIDDLE: ["to the middle"],
    Orientation.RIGHT: ["to the right", "rightward"],
    Orientation.LEFT: ["to the left", "leftward"],
    Orientation.BACK: ["back", "behind", "to the rear of"]
}
side_modifiers = {
    Orientation.UP: ["on top of", "at the top of"],
    Orientation.DOWN: ["at the bottom"],
    Orientation.MIDDLE: ["in the middle", "in the center"],
    Orientation.RIGHT: ["on the right of", "on the right by"],
    Orientation.LEFT: ["on the left of", "on the left by"],
    Orientation.BACK: ["in the back", "behind", "to the rear of"]
}

orientation_modifiers_rev = rev(orientation_modifiers)
side_modifiers_rev = rev(side_modifiers)


class RelativePos(IntFlag):
    NONE = 0
    ON = 1
    UNDER = 2
    BEHIND = 4
    NEAR = 8  # next to, in front of..
    ABOVE = 16  # flying tho
    IN = 32  # embroidered but not really inside right? Use grids for things inside things


relative_modifiers = {
    RelativePos.ON: ["on", "on top of", "situated on", "placed on", "upon"],
    RelativePos.UNDER: ["under", "beneath", "on the underside of"],
    RelativePos.BEHIND: ["behind", "after"],
    RelativePos.NEAR: ["near", "near by", "close to", "close by", "next to", "by", "in front of", "in vicinity of",
                       "in the vicinity of"],
    RelativePos.ABOVE: ["above"],
    RelativePos.IN: ["in", "inside", "inward"]
}

relative_modifiers_rev = rev(relative_modifiers)
