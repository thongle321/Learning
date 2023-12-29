import math
def snt(n):
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

n = int(input("Nhap mot so: "))
if snt(n):
    print(n, "La so snt")
else:
    print(n, "Ko la snt")
