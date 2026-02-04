from PIL import Image, ImageOps
from pyzbar.pyzbar import decode
import cv2
import zxingcpp
import base64



# You need to download these 4 model files from the OpenCV GitHub repo
# or let a script handle it.
# QRdetector = cv2.wechat_qrcode_WeChatQRCode(
#     "detect.prototxt", "detect.caffemodel", 
#     "sr.prototxt", "sr.caffemodel"
# )

inception_qr = Image.open("inception.png")

'''
qrs = [] 
qrs.append(inception_qr.crop((1325,1325,1375,1375,)))
qrs[0] = ImageOps.invert(qrs[0])
qrs[0].show()
qrs[0].save("cropped.png")

# decoded_objects = decode(Image.open("cropped.png"))
decoded_objects = decode(qrs[0])
if decoded_objects:
    decoded_data = ""
    for obj in decoded_objects:
        decoded_data += obj.data.decode('utf-8')
    print("scanned data found")
    print("data in qr: ",decoded_data)

# img = cv2.imread("cropped.png")
# res, points = QRdetector.detectAndDecode(img)
# print("QR code detected by CV wechat", res)

results = zxingcpp.read_barcodes(qrs[0])
for result in results:
    print("qr found by zxingcpp")
    print(f"Text: {result.text}")
    print(f"Format: {result.format}")

quit()
'''
# (left, upper, right, lower)``
left = 0
upper = 0
right = 100
lower = 100
flag = ""
i=-1
while upper<8700:
    i+=1
    qr = inception_qr.crop((left+25,upper+25,right-25,lower-25))
    # qr.save(f"QRs/qr{i}.png")
    decoded_objects = zxingcpp.read_barcodes(qr)
    if decoded_objects:
        # print(f"({left},{upper},{right},{lower}")
        decoded_data = ""
        for obj in decoded_objects:
            decoded_data += obj.text
        flag += decoded_data
    left += 100
    right += 100
    if left == 8700:
        left = 0
        right = 100
        upper += 100
        lower += 100
        if upper == 8700:
            break
print("decodedCode: \n", flag)

flag = flag.split('...')[-1].strip()
png_data = base64.b64decode(flag)
open("qr2Qr.png", 'wb').write(png_data)
qr = Image.open("qr2Qr.png")
res = zxingcpp.read_barcodes(qr)
for r in res:
    print("\nFlag: ", r.text)
print()
print()
# qrs[0].save("cropped.png")