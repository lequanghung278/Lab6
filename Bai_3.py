import tkinter as tk
from tkinter import messagebox

def submit_form():
    # Lấy dữ liệu từ các trường nhập
    name = name_entry.get()
    last_name = last_name_entry.get()
    title = title_entry.get()
    age = age_entry.get()
    nationality = nationality_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    gender = gender_var.get()

    # Lấy dữ liệu từ khung đăng ký
    is_registered = registered_checkbox.get()
    courses_completed = courses_completed_spinbox.get()
    semester = semester_combobox.get()

    # Kiểm tra xem người dùng đã đồng ý với Điều khoản và Điều kiện hay chưa
    if not terms_checkbox.get():
        messagebox.showerror("Lỗi", "Bạn cần đồng ý với Điều khoản và Điều kiện")
        return

    # Validate required fields
    if not (name and last_name and age and gender and email and phone):
        messagebox.showerror("Lỗi", "Vui lòng điền vào tất cả các trường bắt buộc")
        return

    # In thông báo ra bảng điều khiển
    print(f"""
        Thông tin người dùng:
            - Tên: {name} {last_name}
            - Chức danh: {title}
            - Tuổi: {age}
            - Quốc tịch: {nationality}
            - Email: {email}
            - Số điện thoại: {phone}
            - Giới tính: {gender}

        Thông tin đăng ký:
            - Trạng thái đăng ký: {"Đã đăng ký" if is_registered else "Chưa đăng ký"}
            - Số khóa học đã hoàn thành: {courses_completed}
            - Học kỳ: {semester}
    """)

def clear_form():
    name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    title_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    nationality_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    gender_var.set(None)
    registered_checkbox.set(False)
    courses_completed_spinbox.delete(0, tk.END)
    courses_completed_spinbox.insert(0, 0)
    semester_combobox.set("Học kỳ 1")
    terms_checkbox.set(False)

root = tk.Tk()
root.title("Đăng ký khóa học")
root.geometry("600x500")

# Khung thông tin người dùng
user_info_frame = tk.LabelFrame(root, text="Thông tin người dùng")
user_info_frame.pack(pady=20, fill="x", padx=10)

tk.Label(user_info_frame, text="Tên:").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(user_info_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(user_info_frame, text="Họ:").grid(row=0, column=2, padx=5, pady=5)
last_name_entry = tk.Entry(user_info_frame)
last_name_entry.grid(row=0, column=3, padx=5, pady=5)

tk.Label(user_info_frame, text="Chức danh:").grid(row=1, column=0, padx=5, pady=5)
title_entry = tk.Entry(user_info_frame)
title_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(user_info_frame, text="Tuổi:").grid(row=1, column=2, padx=5, pady=5)
age_entry = tk.Entry(user_info_frame)
age_entry.grid(row=1, column=3, padx=5, pady=5)

tk.Label(user_info_frame, text="Quốc tịch:").grid(row=2, column=0, padx=5, pady=5)
nationality_entry = tk.Entry(user_info_frame)
nationality_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(user_info_frame, text="Email:").grid(row=2, column=2, padx=5, pady=5)
email_entry = tk.Entry(user_info_frame)
email_entry.grid(row=2, column=3, padx=5, pady=5)

tk.Label(user_info_frame, text="Số điện thoại:").grid(row=3, column=0, padx=5, pady=5)
phone_entry = tk.Entry(user_info_frame)
phone_entry.grid(row=3, column=1, padx=5, pady=5)

# Gender selection
tk.Label(user_info_frame, text="Giới tính:").grid(row=3, column=2, padx=5, pady=5)
gender_var = tk.StringVar()
gender_frame = tk.Frame(user_info_frame)
gender_frame.grid(row=3, column=3, padx=5, pady=5)

tk.Radiobutton(gender_frame, text="Nam", variable=gender_var, value="Nam").pack(side=tk.LEFT)
tk.Radiobutton(gender_frame, text="Nữ", variable=gender_var, value="Nữ").pack(side=tk.LEFT)
tk.Radiobutton(gender_frame, text="Khác", variable=gender_var, value="Khác").pack(side=tk.LEFT)

# Khung đăng ký
registration_frame = tk.LabelFrame(root, text="Thông tin đăng ký")
registration_frame.pack(pady=20, fill="x", padx=10)

tk.Label(registration_frame, text="Đã đăng ký:").grid(row=0, column=0, padx=5, pady=5)
registered_checkbox = tk.BooleanVar()
registered_checkbox.set(False)  # Default value
tk.Checkbutton(registration_frame, variable=registered_checkbox).grid(row=0, column=1, padx=5, pady=5)
tk.Label(registration_frame, text="Số khóa học đã hoàn thành:").grid(row=1, column=0, padx=5, pady=5)
courses_completed_spinbox = tk.Spinbox(registration_frame, from_=0, to=10)
courses_completed_spinbox.grid(row=1, column=1, padx=5, pady=5)

tk.Label(registration_frame, text="Học kỳ:").grid(row=2, column=0, padx=5, pady=5)
semester_combobox = tk.StringVar()
semester_combobox.set("Học kỳ 1")
tk.OptionMenu(registration_frame, semester_combobox, "Học kỳ 1", "Học kỳ 2", "Học kỳ 3").grid(row=2, column=1, padx=5, pady=5)

terms_checkbox = tk.BooleanVar()
tk.Checkbutton(root, text="Tôi đồng ý với Điều khoản và Điều kiện", variable=terms_checkbox).pack(pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

submit_button = tk.Button(button_frame, text="Đăng ký", command=submit_form)
submit_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="Xóa", command=clear_form)
clear_button.pack(side=tk.LEFT, padx=10)

root.mainloop()