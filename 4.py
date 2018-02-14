from collections import OrderedDict

def wlatin(n):
    latin = OrderedDict()
    latin[1000] = "M"
    latin[900] = "CM"
    latin[500] = "D"
    latin[400] = "CD"
    latin[100] = "C"
    latin[90] = "XC"
    latin[50] = "L"
    latin[40] = "XL"
    latin[10] = "X"
    latin[9] = "IX"
    latin[5] = "V"
    latin[4] = "IV"
    latin[1] = "I"

    def latinnum(n):
        for r in latin.keys():
            x, y = divmod(n, r)
            yield latin[r] * x
            n = n - (r * x)
            if n > 0:
                latinnum(n)
            else:
                break
    return "".join([z for z in latinnum(n)])

number=input(" WRITE A NUMBER: ")
print wlatin(number)	