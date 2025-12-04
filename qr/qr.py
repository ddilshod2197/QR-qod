import qrcode
from pathlib import Path

print("QR.uz - Tezkor QR kod yaratuvchi")
print("=" * 40)

matn = input("Nima yozilsin QR kodga? (havola, matn, wifi, tel...) → ").strip()

if not matn:
    print("Hech nima kiritmadingiz!")
    exit()


rang = input("Rang tanlang (qora, ko'k, yashil, qizil, oq fonda) [standart: qora] → ").lower().strip()

if "ko'k" in rang or "blue" in rang:
    fill = "#0066ff"
elif "yashil" in rang or "green" in rang:
    fill = "#00ff00"
elif "qizil" in rang or "red" in rang:
    fill = "#ff0000"
else:
    fill = "black"


qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(matn)
qr.make(fit=True)

rasm = qr.make_image(fill_color=fill, back_color="white")


fayl_nomi = "mening_qr.png"
rasm.save(fayl_nomi)

print(f"\nTayyor! QR kod saqlandi → {fayl_nomi}")
print("Faylni ochib ko'ring yoki do'stlaringizga yuboring!")


import os
try:
    if os.name == 'nt':  # Windows
        os.startfile(fayl_nomi)
    elif os.name == 'posix':  # Mac yoki Linux
        os.system(f"xdg-open {fayl_nomi}" if "linux" in os.uname().sysname.lower() else f"open {fayl_nomi}")
except:
    pass
