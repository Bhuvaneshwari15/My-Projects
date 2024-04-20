import tkinter as tk
from tkinter import messagebox

# Your prediction logic (replace with your actual logic)
def predict(url):
    return "Phishing" if "phishing" in url.lower() else "Legitimate"

# Event handler for the button click
def predict_button_click():
    url = entry.get()
    prediction = predict(url)
    messagebox.showinfo("Prediction Result", f"The URL is: {prediction}")

# Create the main window
app = tk.Tk()
app.title("URL Predictor")

# Create and place widgets (labels, entry, button)
label = tk.Label(app, text="Enter URL:")
label.pack()

entry = tk.Entry(app)
entry.pack()

predict_button = tk.Button(app, text="Predict", command=predict_button_click)
predict_button.pack()

# Start the main event loop
app.mainloop()
