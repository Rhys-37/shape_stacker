from tkinter import Tk, PhotoImage, Label

class Background:
    def __init__(self) -> None:
        self.background = None  # Initialize self.background for later use
    
    def create(self):
        self.background = Tk()  # Store the Tk instance in self.background
        self.background.geometry("1024x1024")
        self.background.title("Shape Stacker")
        
        # Set the icon
        self.imageIcon()

        # Set the background image
        self.setBackgroundImage('images/background.png')  # Specify your image path here

        self.background.mainloop()  # Start the main event loop
        print("Background successfully created")

    def imageIcon(self):
        # Set the icon for the Tk instance
        icon = PhotoImage(file='images/shape_stacker_logo.png')
        self.background.iconphoto(False, icon)  # Use self.background to set the icon

    def setBackgroundImage(self, image_path):
        # Load the image
        try:
            background_image = PhotoImage(file=image_path)
        except Exception as e:
            print(f"Error loading image: {e}")
            return
        
        # Create a Label to display the image
        label = Label(self.background, image=background_image)
        label.image = background_image  # Keep a reference to the image to prevent garbage collection
        label.place(x=0, y=0, relwidth=1, relheight=1)  # Place the label to cover the entire window

# Code only needed to create this object for testing purposes 
if __name__ == '__main__':
    background = Background()
    background.create()
