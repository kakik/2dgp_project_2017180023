class Unit(object):
    def __init__(self):
        pass

    def get_events(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class PlayerUnit(Unit):
    def __init__(self):
        super(PlayerUnit, self).__init__()
        self.x = 400
        self.y = 300
        self.width_half = 0
        self.x_speed = 0
        self.y_speed = 0
        self.direction_angle = 0

    def get_events(self):
        super(PlayerUnit, self).get_events()

    def update(self):
        super(PlayerUnit, self).update()

    def draw(self):
        super(PlayerUnit, self).draw()


class Observer(Unit):
    def __init__(self):
        super(Observer, self).__init__()

    def get_events(self):
        super(Observer, self).get_events()

    def update(self):
        super(Observer, self).update()

    def draw(self):
        super(Observer, self).draw()


class Wraith(Unit):
    def __init__(self):
        super(Wraith, self).__init__()

    def get_events(self):
        super(Wraith, self).get_events()

    def update(self):
        super(Wraith, self).update()

    def draw(self):
        super(Wraith, self).draw()


class Scourge(Unit):
    def __init__(self):
        super(Scourge, self).__init__()

    def get_events(self):
        super(Scourge, self).get_events()

    def update(self):
        super(Scourge, self).update()

    def draw(self):
        super(Scourge, self).draw()