class AttributeHolder:
    def __init__(self):
        self.level = 0
        self.xp = 0
        self.xp_needed = lambda lvl: lvl * 150

    def __str__(self):
        return "Your level is " + str(self.level) + ", your current xp: " + str(self.xp) + " Xp to next level " + (
        str(self.xp_needed(self.level + 1) - self.xp)) + "\n"


class Skills:
    def __init__(self):
        self.all_skills = {}

    def __str__(self):
        whole_info = ""
        for k, v in self.all_skills.items():
            whole_info += k + str(v)
        return whole_info

    def set_skill(self, skill, level, xp):
        if skill not in self.all_skills:
            self.all_skills[skill] = AttributeHolder()
        a = self.all_skills[skill]
        a.level = level
        a.xp = xp

    def add_xp(self, skill, xp):
        if skill not in self.all_skills:
            self.all_skills[skill] = AttributeHolder()
        a = self.all_skills[skill]
        a.xp += xp

        while a.xp_needed(a.level + 1) < a.xp:
            a.xp = a.xp - a.xp_needed(a.level)
            a.level += 1
        while a.xp < 0:
            a.level -= 1
            a.xp += a.xp_needed(a.level+1)


a = Skills()

"""a.set_skill("Woodcutting", 1, 0)
a.set_skill("Firemaking", 0, 0)

print(a)

a.add_xp("Woodcutting", 100)
a.add_xp("Firemaking", 100)

print(a)

a.add_xp("Woodcutting", 400)
a.add_xp("Firemaking", 5000)

print(a)

a.add_xp("Firemaking", -5000)
print(a)"""
