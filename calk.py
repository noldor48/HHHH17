class Calculator:
    def __init__(self, a, b):#, darbiba
        self.a = a
        self.b = b
    def saskaitisana(self):
        sum = self.a + self.b
        print(sum)
        return sum
    def atnemsana(self):
        sum = self.a - self.b
        print(sum)
        return sum
    def reizinasana(self):
        sum = self.a * self.b
        print(sum)
        return sum
    def dalisana(self):
        try:
            sum = self.a / self.b
            print(sum)
            return sum
        except ZeroDivisionError:
            print("Nijuhai bebru ZeroDivisionError")
def get_valid_number(Calculator):
    while True:
        try:
            return float(input(Calculator))
        except ValueError:
            print("Kļūda :ievadiet derigu skaitli ") 
        #self.darbiba = darbiba
    #if darbiba == "+":
    #    print()
def main():
    a = get_valid_number("Enter first number:")
    b = get_valid_number("Enter second number:")
    #darbiba = input("Enter action(+,-,*,/):")
    calck1 = Calculator(int(a),int(b))#,darbiba
    calck1.saskaitisana()
    calck1.atnemsana()
    calck1.reizinasana()
    calck1.dalisana()

main()