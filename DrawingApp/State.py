# StateMachine/State.py
# A State has an operation, and can be moved
# into the next State given an Input:

class State:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name
    def run(self):
        assert 0, "run not implemented"
    def next(self, input):
        assert 0, "next not implemented"
