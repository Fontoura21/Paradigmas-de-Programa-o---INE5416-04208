x,y,z = (int(i) for i in input().split())
quantidadex = x//2
quantidadey = y//3
quantidadez = z//5

if quantidadex <= quantidadey and quantidadex <= quantidadez:
    print(quantidadex)
elif quantidadey <= quantidadex and quantidadey <= quantidadez:
    print(quantidadey)
else:
    print(quantidadez)