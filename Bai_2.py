import tkinter as tk
from tkinter import messagebox

class AntivirusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AtarBals Modern Antivirus")
        self.root.geometry("800x500")
        self.root.configure(bg="white")

        # Tạo thanh bên
        self.sidebar = tk.Frame(root, bg="#3355FF", width=200, height=500)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        self.sidebar_label = tk.Label(self.sidebar, text="AtarBals AntiVirus", font=("Arial", 16), bg="#3355FF", fg="white")
        self.sidebar_label.pack(pady=10)

        self.menu_items = ["Status", "Updates", "Settings", "Share Feedback", "Buy Premium", "Help"]
        for item in self.menu_items:
            btn = tk.Button(self.sidebar, text=item, font=("Arial", 14), bg="#3355FF", fg="white", relief=tk.FLAT)
            btn.pack(pady=5, padx=10, fill=tk.X)

        self.scan_now_button = tk.Button(self.sidebar, text="Scan Now", font=("Arial", 14), bg="lime", fg="black")
        self.scan_now_button.pack(pady=20, padx=10, fill=tk.X)

        # Tạo khu vực nội dung chính
        self.main_content = tk.Frame(root, bg="white")
        self.main_content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.title_label = tk.Label(self.main_content, text="Scan", font=("Arial", 24), bg="white")
        self.title_label.pack(pady=20)

        self.subtitle_label = tk.Label(self.main_content, text="Premium will be free forever. You just need to click button.", font=("Arial", 14), bg="white")
        self.subtitle_label.pack(pady=10)

        self.buttons_frame = tk.Frame(self.main_content, bg="white")
        self.buttons_frame.pack(pady=20)

        self.buttons = [
            ("Quick Scan", self.quick_scan),
            ("Web Protection", self.web_protection),
            ("Quarantine", self.quarantine),
            ("Full Scan", self.full_scan),
            ("Simple Update", self.simple_update)
        ]

        for text, command in self.buttons:
            btn = tk.Button(self.buttons_frame, text=text, font=("Arial", 14), bg="magenta", fg="white", command=command, width=15, wraplength=120)
            btn.pack(side=tk.LEFT, padx=10, pady=10)

        self.status_label = tk.Label(self.main_content, text="Get Premium to Enable: {Web Protection}, {Full Scan}, {Simple Update}", font=("Arial", 12), bg="white", fg="magenta")
        self.status_label.pack(pady=10)

    def quick_scan(self):
        self.update_status("Quick Scan started")
    
    def web_protection(self):
        self.update_status("Web Protection is a premium feature")
    
    def quarantine(self):
        self.update_status("Quarantine opened")
    
    def full_scan(self):
        self.update_status("Full Scan is a premium feature")
    
    def simple_update(self):
        self.update_status("Simple Update is a premium feature")
    
    def update_status(self, message):
        self.status_label.config(text=message)
        messagebox.showinfo("Info", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = AntivirusApp(root)
    root.mainloop()
