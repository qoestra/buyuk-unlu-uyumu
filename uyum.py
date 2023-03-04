kelime = input("Bir kelime girin: ")

son_unlu_harf = None
onceki_unlu_harf = None

unlu_harfler = "aeıioöuü"

for harf in kelime:
    if harf in unlu_harfler:
        onceki_unlu_harf = son_unlu_harf
        son_unlu_harf = harf

if son_unlu_harf in "aeı":
    print("Büyük ünlü uyumu sağlanmıştır.")
elif son_unlu_harf == "o" and onceki_unlu_harf == "o":
    print("Büyük ünlü uyumu sağlanmıştır.")
elif son_unlu_harf == "u" and onceki_unlu_harf == "u":
    print("Büyük ünlü uyumu sağlanmıştır.")
else:
    print("Büyük ünlü uyumu sağlanmamıştır.")
