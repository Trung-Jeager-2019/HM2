from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import os
from utils.helper import geocode_address, calculate_distance

app = Flask(__name__)
app.secret_key = 'HOMO_exe'  # Thay đổi 'your_secret_key_here' thành một chuỗi ngẫu nhiên và bí mật
#NYMGQFV3ZB7E25YQ4WU26WFW
# Đường dẫn đến tệp người dùng
USER_FILE = 'static/user.txt'

def save_user(email, password):
    with open(USER_FILE, 'a') as f:
        f.write(f"{email},{generate_password_hash(password)}\n")

def check_user(email, password):
    if not os.path.exists(USER_FILE):
        return False
    with open(USER_FILE, 'r') as f:
        for line in f:
            stored_email, stored_password = line.strip().split(',')
            if stored_email == email and check_password_hash(stored_password, password):
                return True
    return False

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None  # Biến để lưu thông báo lỗi

    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']

        # Kiểm tra xem email đã tồn tại chưa
        with open('static/user.txt', 'r', encoding='utf-8') as f:
            for line in f:
                user_email, user_password, username, user_phone = line.strip().split(',')
                if user_email == email:
                    error = "Email đã tồn tại. Vui lòng chọn email khác."
                    return render_template('register.html', error=error)

        # Lưu thông tin người dùng vào tệp
        with open('static/user.txt', 'a', encoding='utf-8') as f:
            f.write(f"{email},{password},{name},{phone}\n")

        session['username'] = name  # Lưu tên người dùng vào phiên
        return redirect(url_for('success'))  # Chuyển hướng đến trang chính

    return render_template('register.html', error=error)



@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Kiểm tra thông tin đăng nhập
        with open('static/user.txt', 'r', encoding = 'utf-8') as f:
            for line in f:
                user_email, user_password, username, user_phone = line.strip().split(',')
                if user_email == email and user_password == password:
                    session['username'] = username  # Lưu tên người dùng vào phiên
                    return redirect(url_for('index'))  # Chuyển hướng đến trang chính

        # Nếu thông tin không đúng, thiết lập thông báo lỗi
        error = "Sai thông tin đăng nhập"
    
    return render_template('login.html', error=error)



@app.route('/driver_register')
def driver_register():
    return render_template('driver_register.html')

# Xử lý đăng ký tài xế
@app.route('/submit_driver_registration', methods=['POST'])
def submit_driver_registration():
    # Lấy thông tin từ form
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    password = request.form.get('password')
    address = request.form.get('address')
    vehicle_type = request.form.get('vehicle_type')

    with open('static/driver.txt', 'a') as f:
        f.write(f"{name},{phone},{email},{password},{address},{vehicle_type}\n")

    flash('Đăng ký thành công! Bạn có thể đăng nhập ngay bây giờ.')
    return redirect(url_for('index'))

@app.route('/booking')
def booking_page():
    return render_template('booking.html')

@app.route('/booking2')
def booking_page2():
    return render_template('booking2.html')

@app.route('/booking3')
def booking_page3():
    return render_template('booking3.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  # Xóa thông tin tên người dùng khỏi phiên
    return redirect(url_for('index'))  # Chuyển hướng về trang chính

@app.route('/address_calculator')
def address_calculator():
    address1 = "1029 Trần Hưng Đạo, Đống Đa, Quy Nhơn, Bình Định, Việt Nam"
    address2 = "669 Trần Hưng Đạo, Lê Hồng Phong, Quy Nhơn, Bình Định, Việt Nam"
    coord1 = geocode_address(address1)
    coord2 = geocode_address(address2)
    print(f"coord1: {coord1}")
    print(f"coord2: {coord2}")

    distance, duration = calculate_distance(coord1, coord2)

    print(f"Distance: {distance / 1000:.2f} km")
    print(f"Estimated Travel Time: {duration / 60:.2f} minutes")

    return f"Distance: {distance / 1000:.2f} km\n" \
        f"Estimated Travel Time: {duration / 60:.2f} minutes"

if __name__ == '__main__':
    app.run(debug=True)
