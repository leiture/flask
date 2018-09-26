list =[]
def num(i):
    for x in i:
        def fibo(x):
            if x == 0:
                resp = 0
            elif x == 1:
                resp = 1
            else:
                return fibo(x-1) + fibo(x-2)

            return resp


print()
