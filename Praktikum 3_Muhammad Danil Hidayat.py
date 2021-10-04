# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 14:52:32 2021
Spyder Editor
@nama : Muhammad Danil Hidayat
@NIM :065002100032
@hari?tanggal : 20211004
This is a temporary script file.
"""

a = print('progam menentukan jenis segitiga')

x = float(input('Masukan sisi A :  '))
y = float(input('Masukan sisi B :  '))
z = float(input('Masukan sisi C :  '))

if(x == y == z):
    print('ini adalah segitiga sama sisi')
elif((x == y) or (y == z) or (z == x)):
     print('ini adalah segitiga sama kaki')
elif((x + y <=z) or (x + z <= y) or (y + z <= x)):
    print('ini bukan termasuk segitiga')
else:
    print('ini adalah segitiga sembarang')

