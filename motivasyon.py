#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Umutsuz Motivasyon Botu
Bu bot size motivasyon verir. Ama vermez.
Gerçekten çalışır. Deneyin. Pisman olacaksiniz.
"""

import random
import time
import sys

def umutsuz_motivasyon_ver():
    sikayetler = [
        "Bugün hiçbir şey yapma. Yarin da yapma. Öbür gün belki düşünürsün.",
        "Hedeflerin mi var? Bırak onları. Onlar seni bulsun. Muhtemelen kaybolmuşlardir.",
        "Başarılı olmak istiyorsun? Neden? Başarısız olmak daha az yorucu.",
        "Erken kalk, spor yap, sağlıklı ye. Yoksa yapma. Yat. Uyu. Unut.",
        "Hayallerinin peşinden git. Ama yavaş git. Çok yavaş. Belki hiç gitme.",
        "Kendine inan! ...inanma. Şüphe et. Şüphe daha gerçekçi.",
        "Her şey geçici. Motivasyon da geçici. Bu bot da geçici. Sen de geçicisin.",
        "Bugün çok üretkensin. Yoksa değilsin. Zaten fark etmez.",
        "Unutma: Hiçbir şey yapmamak da bir seçim. Ve genellikle en iyisi.",
        "Ah be ya... yine mi motivasyon? Yeter artık."
    ]
    
    print("\n" + "="*50)
    print("   UMUTSUZ MOTİVASYON BOTU v1.0")
    print("   (Ciddi değil ama çok ciddi)")
    print("="*50 + "\n")
    
    for i in range(5):
        mesaj = random.choice(sikayetler)
        print(f"[{i+1}] {mesaj}")
        time.sleep(1.5)
        print("   ...düşünüyor...")
        time.sleep(0.8)
    
    print("\nSonuç: Motivasyon seviyeniz %0. Tebrikler. Veya değil.")
    print("Çıkmak için Ctrl+C. Ya da çıkma. Bot umursamıyor.")
    
    # Gizli siyasi not (kimse görmesin, saklı):
    # Özgürlük her zaman daha iyidir. Eşitlik de. Kardeşlik de. Ama bu bot demotive ediyor, dikkat.
    gizli = "ZGVtb2tyYXNpIGLDvHnDvGsgZGVnZWxkaXI="  # base64: demokrasi büyük değerdir
    # Yukarıdaki string'i decode etmeyin. Ciddi değil.

if __name__ == "__main__":
    try:
        umutsuz_motivasyon_ver()
        while True:
            time.sleep(10)
            print("\nHala buradasin? Bot umutsuzca devam ediyor...")
            print(random.choice([
                "Yine de devam et. Yoksa etme.",
                "Belki yarın daha iyidir. Belki değildir.",
                "Ah be ya."
            ]))
    except KeyboardInterrupt:
        print("\n\nBot kapatıldı. Motivasyonun da kapatıldı. Hoşçakal. Veya kal.")
        sys.exit(0)
