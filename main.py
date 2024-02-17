import tkinter as tk

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight / (height ** 2)
    bmi_label.config(text=f"BMI: {bmi:.2f}")

def classify_bmi():
    bmi = float(bmi_label.cget("text").split(":")[1].strip())
    if bmi < 18.5:
        category_label.config(text="Category: Underweight")
    elif bmi < 24.9:
        category_label.config(text="Category: Normal Weight")
    elif bmi < 29.9:
        category_label.config(text="Category: Overweight")
    else:
        category_label.config(text="Category: Obesity")

root = tk.Tk()
root.title("BMI Calculator")

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack()

weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text="Height (m):")
height_label.pack()

height_entry = tk.Entry(root)
height_entry.pack()

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

bmi_label = tk.Label(root, text="BMI: ")
bmi_label.pack()

classify_button = tk.Button(root, text="Classify BMI", command=classify_bmi)
classify_button.pack()

category_label = tk.Label(root, text="Category: ")
category_label.pack()

root.mainloop()
