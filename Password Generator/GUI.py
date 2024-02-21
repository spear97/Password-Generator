# Import necessary modules for GUI and messagebox
from tkinter import messagebox
import tkinter as tk

# Import the Generator class from Generator.py
from Generator import Generator

class GUI(object):
    
    def __init__(self):

        # Create and Initialize an instance of the Generator class
        self.gen = Generator()

        # Create the main window of the application
        self.window = tk.Tk()

        # Set the window title
        self.window.title("Password Generator App")

        # Set the size, shape, and location of the application window
        self.set_geometry()

        # Create a label for the password length field
        self.name_label = tk.Label(self.window, text="Password Length:")
        self.name_label.pack()

        # Create an entry field for the user to enter the password length
        self.user_entry = tk.Entry(self.window)
        self.user_entry.pack()

        # Create an advisory label for password length requirements
        self.advisory_label = tk.Label(self.window, text="Passwords must be between 8 to 16 characters long!")
        self.advisory_label.pack()

        # Create a button to generate the password
        self.gen_button = tk.Button(self.window, text="Generate Password", command=self.generate_password)
        self.gen_button.pack()

        # Create a label for the password result
        self.result_label = tk.Label(self.window, text="Generated Password:")
        self.result_label.pack()

        # Create an entry field to display the generated password
        self.pass_result = tk.Entry(self.window)
        self.pass_result.pack()

        # Run the application
        self.window.mainloop()

    def set_geometry(self):
        '''
        Set the size, shape, and location of the application window.
        '''
        # Set the minimum size that the application window is allowed to be
        size = 500

        # Get the screen resolution of the device window
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Calculate the center X and Y position for the application window
        x = (screen_width - size) // 2
        y = (screen_height - size) // 2

        # Set the size and location of the application window
        self.window.geometry(f"{size}x{size}+{x}+{y}")

        # Set the minimum size that the application window is allowed to be
        self.window.minsize(size, size)

    def generate_password(self):
        '''
        Generate a password based on user input and display it.
        '''
        # Attempt to generate a password
        try:
            # Get the user input for password length and convert it to an integer
            password_length = int(self.user_entry.get())

            # Ensure that the input is not less than 8 characters in length
            if password_length < 8:
                messagebox.showerror(title='Error!', message='Please enter a minimum of 8 characters!')

            # Ensure that the input is not greater than 16 characters in length
            elif password_length > 16:
                messagebox.showerror(title='Error!', message='Password cannot exceed a maximum of 16 characters!')

            else:
                # Generate a new password using the Generator class
                new_password = self.gen.generate_password(password_length)

                # Clear any previous content in the password result field
                self.pass_result.delete(0, tk.END)

                # Insert the new password into the password result field
                self.pass_result.insert(0, new_password)

        # Handle exceptions for invalid inputs
        except ValueError:
            messagebox.showerror(title='Error!', message='You entered an invalid input! Please enter an integer.')

# Create an instance of the GUI class to run the application
if __name__ == "__main__":
    gui = GUI()
