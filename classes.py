def gcd(m,n):
        while m % n != 0:
            old_m = m
            old_n = n
            m = old_n
            n = old_m % old_n
        return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    
    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def __add__(self,other_fraction):
        new_den = self.den * other_fraction.den
        new_num = self.num * other_fraction.den + other_fraction.num * self.den
        common = gcd(new_num,new_den)
        return Fraction(new_num//common,new_den//common)

    def __eq__(self, other_fraction):
        firstNum = self.num * other_fraction.den
        secondNum = self.den * other_fraction.num
        return firstNum == secondNum

    

    



