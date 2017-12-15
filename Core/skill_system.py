import cmath


class AttributeHolder:
    def __init__(self):
        self.xp = 0

    def __str__(self):
        b = self.get_level()
        return " level: " + str(b) + " xp: "+str(self.xp)

    def get_level(self):
        return int(cmath.log(self.xp).real)


class Skills:
    def __init__(self):
        self.all_skills = {}

    def __str__(self):
        whole_text = ""
        for k, v in self.all_skills.items():
            whole_text += k + str(v)
        return whole_text

    def set_skill(self, skill, xp):
        if skill not in self.all_skills:
            self.all_skills[skill] = AttributeHolder()
        skill_attributes = self.all_skills[skill]
        skill_attributes.xp = xp

    def add_xp(self, skill, xp):
        if skill not in self.all_skills:
            self.all_skills[skill] = AttributeHolder()
        skill_attributes = self.all_skills[skill]
        skill_attributes.xp += xp

    def get_lvl(self,skill):
        return self.all_skills[skill].get_level()





