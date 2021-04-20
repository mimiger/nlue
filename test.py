
# ファイルをリテラルで読んでqrコードに変換するやつ

#
import qrcode,os
from PIL import Image

#################################


#################################

# テスト用変数
f_path = ""
f_name = "make_gui.py"

# literalize
def literalize(f):
    try:
        print()
    except a:
        print() 

with open(f_name,"r",encoding="utf-8") as f:
    lt = f.read()

print(os.path.getsize("qr3.py"),"a")
print(len(lt))

qr = qrcode.QRCode(
    version          = 40,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size         = 16,
    border           = 4 ,
)

qr.add_data(lt)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.show()
