class Agent:
    def __init__(self, id, value, src, dest, speed, pos):
        self.id = id
        self.value = value
        self.src = src
        self.dest = dest
        self.speed = speed
        self.pos = pos

    def get_id(self):
        return self.id

    def set_id(self, i):
        self.id = i

    def get_value(self):
        return self.value

    def set_value(self, v):
        self.value = v

    def get_src(self):
        return self.src

    def set_src(self, s):
        self.src = s

    def get_dest(self):
        return self.dest

    def set_dest(self, d):
        self.dest = d

    def get_speed(self):
        return self.speed

    def set_speed(self, s):
        self.speed = s

    def get_pos(self):
        return self.pos

    def set_pos(self, p):
        self.pos = p