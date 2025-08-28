from PIL import Image


color_image = Image.open("color_img.png")
print(color_image.mode)
print(color_image.size)

pixel_column_list = []

for i in range(color_image.size[1]):
    temp_row = []
    for j in range(color_image.size[0]):
        temp_row.append(color_image.getpixel((j,i)))
        # print(color_image.getpixel((j,i)), end=' ')
    pixel_column_list.append(temp_row)


# print(pixel_column_list[0])

# for i in range(len(pixel_column_list)):
#     if pixel_column_list[i] != pixel_column_list[0]:
#         print(f" pixel column {i} not equal to column 0")

unique_pixels = [pixel_column_list[0][0]]

for t in pixel_column_list[0]:
    if unique_pixels[-1] != t:
        unique_pixels.append(t)

print(unique_pixels)
message = ""
for t in unique_pixels:
    x, y, z = t
    message += chr(x) + chr(y) + chr(z)
print(message)
print(f"flag: {message}")

# cipher = "C4 7E 6D 75 08 45 2B 22 C9 13 00 00 00 00 49 45 4E 44 AE 42 60 82"
# cipher = cipher.replace("   ", ' ').replace('  ', ' ')
# cipher = cipher.strip().split(' ')

# message = ''
# for c in cipher:
#     message += chr(int(c, 16))

# print(message.encode())