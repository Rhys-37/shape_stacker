'''
File: main.py
'''

from background import Background


# Function to create the background
def background():
    background = Background()
    background.create() 

if __name__ == '__main__':
    background()
