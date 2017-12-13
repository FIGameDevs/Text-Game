class AtributeHolder:
    def __init__(self):
        self.level=0
        self.xp=0
        self.xp_needed = lambda lvl: lvl*150



class Skills:
    def __init__(self,all_skills):
        self.all_skills={}

    def set_skill(self,skill,level,xp):
        if skill not in self.all_skills:
            self.all_skills[skill]=AtributeHolder()
        a=self.all_skills[skill]
        a.level=level
        a.xp=xp




