# A complete BMI (Body Mass Index) calculator application with a graphical user interface (GUI).
# This script is built using Python's built-in Tkinter library.# A complete BMI (Body Mass Index) calculator application with a graphical user interface (GUI).
# This script is built using Python's built-in Tkinter library.

import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    """
    Calculates the BMI based on user input for weight and height, and displays the result.
    """
    try:
        # Get weight and height from the entry fields
        weight_str = weight_entry.get()
        height_str = height_entry.get()
        
        # Check for empty input
        if not weight_str or not height_str:
            messagebox.showwarning("Warning", "Please enter both weight and height.")
            return

        # Convert input to float and handle potential conversion errors
        weight_kg = float(weight_str)
        height_cm = float(height_str)

        # Check for non-positive values
        if weight_kg <= 0 or height_cm <= 0:
            messagebox.showwarning("Warning", "Weight and height must be positive numbers.")
            return

        # Convert height from centimeters to meters for the BMI formula
        height_m = height_cm / 100
        
        # Calculate BMI
        bmi = weight_kg / (height_m ** 2)

        # Determine the BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        
        # Update the result labels with the calculated values
        result_label.config(text=f"Your BMI is: {bmi:.2f}")
        category_label.config(text=f"Category: {category}")

    except ValueError:
        # Handle cases where the input is not a valid number
        messagebox.showerror("Error", "Invalid input. Please enter numerical values for weight and height.")
    except Exception as e:
        # Catch any other unexpected errors
        messagebox.showerror("An Error Occurred", f"An unexpected error occurred: {e}")

def clear_fields():
    """
    Clears the input fields and result labels.
    """
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")
    category_label.config(text="")

# ----------------- GUI Setup -----------------

# Create the main application window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x300")
root.resizable(False, False)
root.config(bg="#F0F0F0")

# Create a main frame for padding and layout
main_frame = tk.Frame(root, padx=20, pady=20, bg="#F0F0F0")
main_frame.pack(expand=True, fill=tk.BOTH)

# Create and place widgets for input
title_label = tk.Label(main_frame, text="BMI Calculator", font=("Helvetica", 18, "bold"), bg="#F0F0F0")
title_label.pack(pady=(0, 10))

# Weight input
weight_frame = tk.Frame(main_frame, bg="#F0F0F0")
weight_frame.pack(pady=5, fill=tk.X)
weight_label = tk.Label(weight_frame, text="Weight (kg):", font=("Helvetica", 12), bg="#F0F0F0")
weight_label.pack(side=tk.LEFT, padx=(0, 10))
weight_entry = tk.Entry(weight_frame, width=15, font=("Helvetica", 12))
weight_entry.pack(side=tk.RIGHT, expand=True, fill=tk.X)

# Height input
height_frame = tk.Frame(main_frame, bg="#F0F0F0")
height_frame.pack(pady=5, fill=tk.X)
height_label = tk.Label(height_frame, text="Height (cm):", font=("Helvetica", 12), bg="#F0F0F0")
height_label.pack(side=tk.LEFT, padx=(0, 10))
height_entry = tk.Entry(height_frame, width=15, font=("Helvetica", 12))
height_entry.pack(side=tk.RIGHT, expand=True, fill=tk.X)

# Create and place buttons
button_frame = tk.Frame(main_frame, bg="#F0F0F0")
button_frame.pack(pady=15)
calculate_button = tk.Button(button_frame, text="Calculate", font=("Helvetica", 12, "bold"), command=calculate_bmi)
calculate_button.pack(side=tk.LEFT, padx=5)
clear_button = tk.Button(button_frame, text="Clear", font=("Helvetica", 12), command=clear_fields)
clear_button.pack(side=tk.LEFT, padx=5)

# Create and place labels for results
result_label = tk.Label(main_frame, text="", font=("Helvetica", 14, "bold"), bg="#F0F0F0")
result_label.pack(pady=(10, 5))
category_label = tk.Label(main_frame, text="", font=("Helvetica", 14), bg="#F0F0F0")
category_label.pack(pady=5)

# Start the main GUI loop
if __name__ == "__main__":
    root.mainloop()

