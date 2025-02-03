def tambah(x, y):
    return x + y

hasil = list(map(lambda x: tambah(x, 3), [1,2,3]))
print(hasil)