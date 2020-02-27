# Soal 1

# def Find_short(text):
#     list_text = text.split(' ')
#     list_jumlah_huruf = []
#     for item in list_text:
#         if item !='':
#             angka = item.count('')-1
#             list_jumlah_huruf.append(angka)
#     list_jumlah_huruf.sort()
#     print(list_jumlah_huruf[0])
# Find_short("Many people get up early in the morning ")
# Find_short("Every office would getting newest monitor ")
# Find_short("Create new file after this morning")

# Soal 2

# def persistence(n):
#     string_n = str(n)
#     check = False
#     total =0
#     while check == False:
#         hasil=1
#         for item in string_n:
#             hasil*=int(item)
#         total +=1
#         if hasil < 10:
#             check = True
#         else:
#             string_n = str(hasil)
#             check = False
#     if n < 10:
#         total =0
#     print(total)
# persistence(39)
# persistence(999)
# persistence(4)

# Soal 3

# def findUniqChar(text):
#     list_huruf=[]
#     list_huruf_banyak = []
#     for item in text:
#         if item in list_huruf:
#             list_huruf_banyak.append(item)
#             ind = list_huruf.index(item)
#             list_huruf.pop(ind)
#         else:
#             if item not in list_huruf_banyak:
#                 if item != ' ':
#                     list_huruf.append(item)
#     print(''.join(list_huruf))
# findUniqChar('hello world')
# findUniqChar('budi pergi ke pasar')
# findUniqChar('fikri')

# Soal 4

# import string
# def alphabet_position(text):
#     text =text.lower()
#     list_alpha = list(string.ascii_lowercase)
#     kamus = {}
#     angka = 1
#     for item in list_alpha:
#         kamus[item] = angka
#         angka+=1
#     out = ''
#     for huruf in text:
#         if huruf.isalpha() == True:
#             out += f'{kamus[huruf]} '
#         else:
#             out+=''
#     print(out)
# alphabet_position("The sunset sets at twelve o' clock.")
# alphabet_position("it’s never too late to try")
# alphabet_position("Have you done your homework?")