class MFunction:
    def __init__(self, logic):
        self.logic = logic

    def execute(self, param):
        return self.logic(param)
