filas=5

for i in range(1,filas*2):
    if i<=filas:
        print("* "*i)
    else:
        print("* "*(2*filas-i))
