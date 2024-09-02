meme_dict = {
   "LOL": "Komik bir şeye verilen cevap",
   "CRINGE": "Garip ya da utandırıcı bir şey",
   "ROFL": "Bir şakaya karşılık verilen cevap",
   "SHEESH": "Onaylamamak",
   "CREEPY": "Korkunç",
   "AGGRO": "Agresifleşmek/sinirlenmek",
   "YOWAIMO": "Gojo Satoru'nun kullandığı kelime"
}

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict:
    print(word + " kelimesinin anlamı: " + meme_dict[word])
else:
    print("Bu kelime sözlükte bulunamadı.")
