class Pokemon:

    def __init__(self, value, type, pos):
        self.value = value
        self.type = type
        self.pos = pos

    def get_value(self):
        return self.value

    def set_value(self, v):
        self.value = v

    def get_type(self):
        return self.type

    def set_type(self, t):
        self.type = t

    def get_pos(self):
        return self.pos

    def set_pos(self, p):
        self.pos = p
