class vehicle:
    def __init__(self,speed):
        self.speed=speed

    def drive(self,distance):
        print 'need %f hour(s)' % (distance / self.speed)

class bike(vehicle):
    pass

class car(vehicle):
    def __init__(self,speed,fuel):
        vehicle.__init__(self,speed)
        self.fuel=fuel

    def drive(self,distance):
        vehicle.drive(self,distance)
        print 'need %f fuels' %(distance *self.fuel)

b=bike(50.0)
c=car(100,0.06)
False and b.drive(1000)or c.drive(1000)
