'''
Bai 1:

order_price = int(input("Nhap don gia: "))
order_amount = int(input("Nhap so luong: "))

total_order = order_amount * order_price

if total_order >= 1000000:
    total_order = total_order - (total_order*0.1)

print(f"tong so tien cuoi cung: {total_order}")

Bai 2:

right_password = "123456"
lock_count = 0
while True:
    if lock_count >= 3:
        print("Tài khoản đã bị khóa!")
        break

    p_password = input("Nhap mat khau: ")

    if right_password == p_password:
        print("Đăng nhập thành công!")
        break
    
    else:
        lock_count += 1
        print("Mật khẩu sai, vui lòng nhập lại!")

Bai 3:
'''
total_amount = 0
box_amount = 0

while True:
    p_amount = int(input("Nhập số lượng sản phẩm trong thùng: "))
    if p_amount < 0:
        print("Số lượng không hợp lệ, bỏ qua thùng này!")
    elif p_amount == 0:
        break
    else:
        total_amount += p_amount  
        box_amount += 1     

print(f"Tổng số thùng hàng hợp lệ đã đếm: {box_amount}")
print(f"Tổng số lượng sản phẩm thu được: {total_amount}")