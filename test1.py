
class complex():
    """ Complex number classs"""

    """ init method """
    def __init__(self, real, imag):
        self.real = int(real)
        self.imag = int(imag)
        
    @classmethod
    def __add__(self, other):
        return complex(self.real + other.real,
                       self.imag + other.imag)
    @classmethod
    def __sub__(self, other):
        return complex(self.real - other.real,
                       self.imag - other.imag)
    @classmethod
    def __mul__(self, other):
        return complex(self.real * other.real -
                       self.imag * other.imag,
                       self.real * other.imag +
                       self.imag * other.real)
    @classmethod
    def __div__(self, other):
        try: 
            return self.__mul__(complex(other.real, -1*other.imag)).__mul__(complex(1.0/(other.mod().real)**2, 0))
        except ZeroDivisionError as e:
            print (e)
            return None
    @classmethod
    def mod(self):
        return complex(pow(self.real**2+self.imag**2, 0.5), 0)

    def __str__(self, precision=2):
        return str(("%."+"%df"%precision)%float(self.real))+('+' if self.imag>=0 else '-')+str(("%."+"%df"%precision)%float(abs(self.imag)))+'i'

    
