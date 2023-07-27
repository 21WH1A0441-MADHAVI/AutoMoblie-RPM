
import tkinter as tk
import math
from tkinter import *
from playsound import playsound
from PIL import Image, ImageTk

class GUI:
    def __init__(self, master):
        self.master = master
        master.minsize(height=700, width=1530)
        master.title("Automobile RPM")

        self.button1 = tk.Button(master, text="Calculate time between Mileposts", command=lambda:self.open_window(1), font=("Cambria",18), pady=20, bg="#6b5b95", fg="white")
        self.button1.pack()
        self.button1.place(x=900, y=50)
        
        self.sound = 'C:/Users/Madhavi/Downloads/sound-1.wav'
        self.button1.bind('<Button-1>', lambda event: playsound(self.sound))

        

        
        self.button2 = tk.Button(master, text="Calculate number of revolutions per mile", command=lambda:self.open_window(2), font=("Cambria",18), pady=20, bg="#feb236", fg="white")
        self.button2.pack()
        self.button2.place(x=900, y=180)
        self.button2.bind('<Button-1>', lambda event: playsound('sound1.mp3'))

        self.button3 = tk.Button(master, text="Calculate revolutions per second at speed & diameter", command=lambda:self.open_window(3), font=("Cambria",18), pady=20, bg="#d64161", fg="white")
        self.button3.pack()
        self.button3.place(x=900, y=310)
        self.button3.bind('<Button-1>', lambda event: playsound('sound1.mp3'))

        self.button4 = tk.Button(master, text="Calculate actual speed with tire diameter errors", command=lambda:self.open_window(4), font=("Cambria",18), pady=20, bg="#ff7b25", fg="white")
        self.button4.pack()
        self.button4.place(x=900, y=440)
        self.button4.bind('<Button-1>', lambda event: playsound('sound1.mp3'))


    def open_window(self, option):
        new_window = tk.Toplevel(self.master)
        new_window.title("Calculate")
        new_window.minsize(height=1000, width=1530)

        if option == 1:
            label = tk.Label(new_window, text="Calculate time between Mileposts", font=("Cambria",25))
            label.pack()

            def per_milepost(speed):
                return round(3600/speed)

            def calculate_time():
                speeds = [int(speed) for speed in entry.get().split(',')]
                output = ""
                for speed in speeds:
                    time = per_milepost(speed)
                    caution = ""
                    if speed > 70 :
                        caution = " Caution: High speed ⚠️! Be sure to stay alert and maintain a safe distance from other vehicles."
                    elif speed <= 70:
                        caution = " Moderate speed Great job 👍."
                    output += f"Time between mileposts at {speed} mph: {time} seconds. {caution}\n"
                result_label.config(text=output)

            input_label = tk.Label(new_window, text="Enter comma-separated speeds:", font=("Cambria",25))
            input_label.pack()

            entry = tk.Entry(new_window)
            entry.pack()

            calculate_button = tk.Button(new_window, text="Calculate", font=("Cambria",25), command=calculate_time)
            calculate_button.pack()

            result_label = tk.Label(new_window, text="")
            result_label.pack()

        elif option == 2:
            label = tk.Label(new_window, text="Calculate number of revolutions per mile", font=("Cambria",25))
            label.pack()

            # Add code for this calculation here
            def number_of_revs(d):
                circumference = d * math.pi
                return round(5280 / circumference)

            def Numberofrevs():
                diameters = [int(diameter) for diameter in entry.get().split(',')]
                output = ""
                for diameter in diameters:
                    revolutions = number_of_revs(diameter)
                    output += f"Revolutions per mile for {diameter} inch tire: {revolutions}\n"
                result_label.config(text=output)

            input_label = tk.Label(new_window, text="Enter comma-separated diameters:", font=("Cambria",25))
            input_label.pack()

            entry = tk.Entry(new_window)
            entry.pack()

            calculate_button1 = tk.Button(new_window, text="Calculate", font=("Cambria",25), command=Numberofrevs)
            calculate_button1.pack()

            result_label = tk.Label(new_window, text="")
            result_label.pack()

        elif option == 3:
            label = tk.Label(new_window, text="Calculate revolutions per second at given speed and diameter", font=("Cambria",25))
            label.pack()

            # Add code for this calculation here
            def revolutions_per_second(d, s):
                circumference = d * math.pi
                speed_in_fps = s * 5280 / 3600
                revs_per_second = speed_in_fps / circumference
                return revs_per_second

            def Numberofrevs_persecond():
                diameters = [int(diameter) for diameter in diameter_entry.get().split(',')]
                speeds = [int(speed) for speed in speed_entry.get().split(',')]
                output = ""
                for diameter in diameters:
                    for speed in speeds:
                        revs_per_second = revolutions_per_second(diameter, int(speed))
                        output += f"Diameter: {diameter} inches, Speed: {speed} mph, Revolutions per second: {revs_per_second}\n"
                result_label.config(text=output)

            diameter_label = tk.Label(new_window, text="Enter comma-separated diameters:", font=("Cambria",25))
            diameter_label.pack()

            diameter_entry = tk.Entry(new_window, width=50)
            diameter_entry.pack()

            speed_label = tk.Label(new_window, text="Enter comma-separated speeds:", font=("Cambria",25))
            speed_label.pack()

            speed_entry = tk.Entry(new_window)
            speed_entry.pack()

            calculate_button2 = tk.Button(new_window, text="Calculate", font=("Cambria",25), command=Numberofrevs_persecond)
            calculate_button2.pack()

            result_label = tk.Label(new_window, text="")
            result_label.pack()

        elif option == 4:
            label = tk.Label(new_window, text="Calculate actual speed with tire diameter errors", font=("Cambria",25))
            label.pack()

            def actual_speed(speed, error, diameter):
                actual_diameter = diameter * (1 + error / 100)
                actual_speed = speed * (actual_diameter / diameter)
                return actual_speed

            def calculate_actual_speed():
                speed = int(speed_entry.get())
                error = float(error_entry.get())
                diameter = int(diameter_entry.get())
                actual_speed_value = actual_speed(speed, error, diameter)
                if actual_speed_value < 60 :
                    caution = "Caution: Moderate speed 🚸"
                elif actual_speed_value > 70:
                    caution = f"Caution: Well done👍!"
                else:
                    caution = ""
                output = f"Actual speed: {round(actual_speed_value, 2)} mph"
                result_label.config(text=output)

            diameter_label = tk.Label(new_window, text="Enter tire diameter (in inches):", font=("Cambria",25))
            diameter_label.pack()

            diameter_entry = tk.Entry(new_window)
            diameter_entry.pack()

            speed_label = tk.Label(new_window, text="Enter current speed (in mph):", font=("Cambria",25))
            speed_label.pack()

            speed_entry = tk.Entry(new_window)
            speed_entry.pack()

            error_label = tk.Label(new_window, text="Enter tire diameter error (in percentage):", font=("Cambria",25))
            error_label.pack()

            error_entry = tk.Entry(new_window)
            error_entry.pack()

            calculate_button = tk.Button(new_window, text="Calculate", font=("Cambria",25), command=calculate_actual_speed)
            calculate_button.pack()

            result_label = tk.Label(new_window, text="",font=("Cambria",25))
            result_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()