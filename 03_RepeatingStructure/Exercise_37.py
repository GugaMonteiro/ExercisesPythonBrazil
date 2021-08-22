cod = 1
height = 0
weight = 0

big_h = 0
h_minor = 0
big_w = 0
w_minor = 0

c_big_h = 0
c_h_minor = 0
c_big_w = 0
c_w_minor = 0


while cod != 0:
    if cod > 0:
        cod = int(input("Type your code: "))
        if cod != 0:
            y = float(input("Type your height: "))
            if y > height:
                height = y
                big_h = height
                c_big_h = cod
            elif y < height:
                height = y
                h_minor = height
                c_h_minor = cod
            z = float(input("Type your weight: "))
            if z > weight:
                weight = z
                big_w = weight
                c_big_w = cod
            elif z < weight:
                weight = z
                w_minor = weight
                c_w_minor = cod

print(f"\nBiggest height:\nCode: {c_big_h}\nHeight: {big_h}")
print(f"\nBiggest weight:\nCode: {c_big_w}\nWeight: {big_w}")
print(f"\nSmallest height:\nCode: {c_h_minor}\nHeight: {h_minor}")
print(f"\nSmallest weight:\nCode: {c_w_minor}\nWeight: {w_minor}")
