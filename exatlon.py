code = [1152, 1344, 1056, 1968, 1728, 816, 1648, 784, 1584, 816, 1728, 1520, 1840, 1664, 784, 1632, 1856, 1520, 1728, 816, 1632, 1856, 1520, 784, 1760, 1840, 1824, 816, 1584, 1856, 784, 1776, 1760, 528, 528, 2000]
alphabet = {"a": "1552",
"b": "1568",
"c": "1584",
"d": "1600",
"e": "1616",
"f": "1632",
"g": "1648",
"h": "1664",
"i" :"1680",
"j" :"1696",
"k" :"1712",
"l" :"1728",
"m" :"1744",
"n" :"1760",
"o" :"1776",
"p" :"1792",
"q" :"1808",
"r" :"1824",
"s" :"1840",
"t" :"1856",
"u" :"1872",
"v" :"1888",
"w" :"1904",
"x" :"1920",
"y" :"1936",
"z" :"1952",
"A": "1040",
"B": "1056",
"C": "1072",
"D": "1088",
"E": "1104",
"F": "1120",
"G": "1136",
"H": "1152",
"I": "1168",
"J": "1184",
"K": "1200",
"L": "1216",
"M": "1232",
"N": "1248",
"O": "1264",
"P": "1280",
"Q": "1296",
"R": "1312",
"S": "1328",
"T": "1344",
"U": "1360",
"V": "1376",
"W": "1392",
"X": "1408",
"Y": "1424",
"Z":"1440",
"{": "1968", 
"}":"2000",
"!" :"528",
"@" :"1024", 
"#" :"560",
"$" :"576",
"%" :"592",
"^":"1504",
"&" :"608",
"*":"672",
"(":"640",
")" :"656",
"-" :"720",
"_" :"1520",
"=" :"976",
"0" :"768",
"1" :"784",
"2" :"800",
"3" :"816",
"4" :"832" ,
"5" :"848",
"6" :"864",
"7" :"880",
"8" :"896",
"9" :"912"}
newcode = []

"""for char in code:
    char = 1152
    decodedChar = 0
    for i in alphabet:
        if alphabet[i] == str(char):
            decodedChar = i
            print(decodedChar)
    if decodedChar == 0:
        print("_")

"""

for char in code:
    found=False
    for item in alphabet:
        if alphabet[item] == str(char):
            found = True
            print(item, end = "")
    if found == False:
            print("#",end="")