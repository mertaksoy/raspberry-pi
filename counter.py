from gpiozero import LED
from time import sleep

class Number:
    def __init__(self, code, mappings):
        self.code = code
        self.mappings = mappings
        
    def turnOn(self):
        for led in self.mappings:
            led.on()
            
    def turnOff(self):
        for led in self.mappings:
            led.off()

class Display:
    numbers = []

    def __init__(self, a, b, c, d, e, f, g):
        self.a = LED(a)
        self.b = LED(b)
        self.c = LED(c)
        self.d = LED(d)
        self.e = LED(e)
        self.f = LED(f)
        self.g = LED(g)
        self.numbers.append(Number(0, [self.a, self.b, self.c, self.d, self.e, self.f]))
        self.numbers.append(Number(1, [self.b, self.c]))
        self.numbers.append(Number(2, [self.a, self.b, self.g, self.e, self.d]))
        self.numbers.append(Number(3, [self.a, self.b, self.c, self.d, self.g]))
        self.numbers.append(Number(4, [self.f, self.g, self. b, self.c]))
        self.numbers.append(Number(5, [self.a, self.f, self.g, self.c, self.d]))
        self.numbers.append(Number(6, [self.a, self.f, self.e, self.d, self.c, self.g]))
        self.numbers.append(Number(7, [self.a, self.b, self.c]))
        self.numbers.append(Number(8, [self.a, self.b, self.c, self.d, self.e, self.f, self.g]))
        self.numbers.append(Number(9, [self.a, self.b, self.c, self.d, self.f, self.g]))
        
    
    def turnAllOff(self):        
        for number in self.numbers:
            number.turnOff()
        
    def display(self, code):
        self.turnAllOff()
        for number in self.numbers:
            if number.code == code:
                number.turnOn()
                
        
display = Display(14,15,18,17,27,22,23);

while True:
    for number in display.numbers:
        number.turnOn()
        sleep(1)
        number.turnOff()
