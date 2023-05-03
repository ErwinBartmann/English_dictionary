wor = input("Merhaba ingilizce kelime/kısaltma sözlüğüme hoş geldin!")
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap",
            "SHEESH": "onaylamamak",
            "CREEPY": "korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek",
            
            "BTW": "by the way, bu arada",
            "Get it easy" :"Sakin ol",
            "GG": "Good Game,İyi oyundu",
            }
word = input("Bazı kısaltma yada İngilizce kelimelerle sorunmu yaşıyorsun?,elimden geldiğince yardım etmek isterim.Anlamadığın bir kelime yaz(büyük harfle): ")
if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(word,"bu kelime/kısaltmanın anlamı",meme_dict[word])
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("üzgünümki bu kelimenin anlamını bizde bilmiyoruz")
