class Fraction():
    def __init__(self, top, bottom=1):
        if type(top) != int or type(bottom)!= int:
            raise TypeError
        if bottom == 0:
            raise ValueError
        sign = 1
        if (top < 0):
            top, sign = -top, -sign
        if (bottom < 0):
            bottom, sign = -bottom, -sign
        g = self._gcd(top, bottom)
        self.num = sign * (top // g)
        self.den = bottom // g

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        else:
            return str(self.num) +'/'+ str(self.den)

    __repr__ = __str__
    
    def __add__(self, otherFraction):
        bottom = self.den * otherFraction.den
        top = self.num * otherFraction.den + self.den * otherFraction.num

        return Fraction(top, bottom)
    
    def __radd__(self, otherFraction):
        return self + otherFraction

    def __sub__(self, other):
        bottom = self.den * other.den
        top = self.num * other.den - self.den * other.num

        return Fraction(top, bottom)

    def __mul__(self, other):
        bottom = self.den * other.den
        top = self.num * other.num
       
        return Fraction(top, bottom)

    def __truediv__(self, other):
        return Fraction(self.num, self.den) * Fraction(other.den, other.num)

    def __iadd__(self, other):
        return self + other

    def _gcd(self, m, n):
        if m % n == 0:
            return n
        else:
            return self._gcd(n, m%n)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __le__(self, other):
        top = self.num * other.den - self.den * other.num
        return top <= 0
    
    def __ge__(self, other):
        top = self.num * other.den - self.den * other.num
        return top >= 0

    def __lt__(self, other):
        top = self.num * other.den - self.den * other.num
        return top < 0

    def __gt__(self, other):
        top = self.num * other.den - self.den * other.num
        return top > 0
    def __eq__(self, other):
        top = self.num * other.den - self.den * other.num
        return top == 0

    def __ne__(self, other):
        top = self.num * other.den - self.den * other.num
        return top != 0




if __name__ == '__main__':
    f1 = Fraction(-1,2)
    f2 = Fraction(1,2)

    print(f2 - f1)



    