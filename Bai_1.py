import tkinter as tk

# Hàm khi bấm nút "Bắt đầu"
def start():
    status_label.config(text="Đang ghi...")

# Hàm khi bấm nút "Tạm dừng"
def pause():
    status_label.config(text="Đã tạm dừng.")

# Hàm khi bấm nút "Kết thúc"
def stop():
    status_label.config(text="Đã kết thúc ghi.")

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Ứng dụng Ghi Video")
root.geometry("600x300")  # Kích thước cửa sổ

# Thiết lập màu nền
root.configure(bg='pink')

# Nhãn tiêu đề
title_label = tk.Label(root, text="Ứng dụng Ghi Video", font=("Arial", 20), bg='pink')
title_label.pack(pady=10)

# Frame cho đầu vào FPS
fps_frame = tk.Frame(root, bg='pink')
fps_frame.pack(pady=10)

# Nhãn và trường nhập FPS
fps_label = tk.Label(fps_frame, text="FPS:", bg='pink')
fps_label.pack(side=tk.LEFT, padx=10)
fps_entry = tk.Entry(fps_frame)
fps_entry.pack(side=tk.LEFT, padx=10)

# Frame cho các nút
button_frame = tk.Frame(root, bg='pink')
button_frame.pack()

# Nút bắt đầu
start_button = tk.Button(button_frame, text="Bắt đầu", width=10, command=start)
start_button.pack(side=tk.LEFT, padx=10, pady=10)

# Nút tạm dừng
pause_button = tk.Button(button_frame, text="Tạm dừng", width=10, command=pause)
pause_button.pack(side=tk.LEFT, padx=10, pady=10)

# Nút kết thúc
stop_button = tk.Button(button_frame, text="Kết thúc", width=10, command=stop)
stop_button.pack(side=tk.LEFT, padx=10, pady=10)

# Nhãn trạng thái
status_label = tk.Label(root, text="Sẵn sàng để bắt đầu ghi.", bg='pink', bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_label.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

# Chạy vòng lặp chính của cửa sổ
root.mainloop()
