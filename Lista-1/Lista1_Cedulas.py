N = int(input())
cedula100 = N // 100
cedula50 = (N % 100) // 50
cedula20 = ((N % 100) % 50) // 20
cedula10 = (((N % 100) % 50) % 20) // 10
cedula5 = ((((N % 100) % 50) % 20) % 10) // 5
cedula2 = (((((N % 100) % 50) % 20) % 10) % 5) // 2
cedula1 = ((((((N % 100) % 50) % 20) % 10) % 5) % 2) // 1
print(N)
print(cedula100, "nota(s) de R$ 100,00")
print(cedula50, "nota(s) de R$ 50,00")
print(cedula20, "nota(s) de R$ 20,00")
print(cedula10, "nota(s) de R$ 10,00")
print(cedula5, "nota(s) de R$ 5,00")
print(cedula2, "nota(s) de R$ 2,00")
print(cedula1, "nota(s) de R$ 1,00")