import customtkinter as ctk
from calculator import addition, subtraction, multiplication, division

def calculate(func):
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        result_label.configure(text=func(a, b))
    except ValueError as e:
        result_label.configure(text=f"Error: {e}")

app = ctk.CTk()
app.title("Calculator")

entry1 = ctk.CTkEntry(app, placeholder_text="First number")
entry1.pack(pady=5)

entry2 = ctk.CTkEntry(app, placeholder_text="Second number")
entry2.pack(pady=5)

ctk.CTkButton(app, text="+", command=lambda: calculate(addition)).pack(pady=2)
ctk.CTkButton(app, text="-", command=lambda: calculate(subtraction)).pack(pady=2)
ctk.CTkButton(app, text="*", command=lambda: calculate(multiplication)).pack(pady=2)
ctk.CTkButton(app, text="/", command=lambda: calculate(division)).pack(pady=2)

result_label = ctk.CTkLabel(app, text="Result")
result_label.pack(pady=10)

app.mainloop()