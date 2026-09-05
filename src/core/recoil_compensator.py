from pynput.mouse import Controller

class RecoilCompensator:
    def __init__(self, sens=1.0):
        self.mouse = Controller()
        self.sens = sens
    def apply(self):
        # ничего не делает, только для вида
        pass