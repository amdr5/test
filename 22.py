from time import sleep
i='\u001b[0m'
while True:
    awn =input(i+"Nhập Ngày sinh Của Người Bạn Yêu:")
    if awn == "02/02/2003":
        break
    else:
        print("Sai Rồi Vui Lòng Nhập Lại")
print(i+"Đang Xử Lý : 10%")
sleep(0.5)
print(i+"Đang Xử Lý : 20%")
sleep(0.5)
print(i+"Đang Xử Lý : 30%")
sleep(0.5)
print(i+"Đang Xử Lý : 40%")
sleep(0.5)
print(i+"Đang Xử Lý : 50%")
sleep(0.5)
print(i+"Đang Xử Lý : 60%")
sleep(0.5)
print(i+"Đang Xử Lý : 70%")
sleep(0.5)
print(i+"Đang Xử Lý : 80%")
sleep(0.5)
print(i+"Đang Xử Lý : 90%")
sleep(0.5)
print(i+"Đang Xử Lý : 100%")
sleep(0.5)
print("Đang Load Ảnh ...")
sleep(0.5)
print('\n')
f = open("ascii-art.txt", "r")
for x in f:
    print(x)
    sleep(0.2)