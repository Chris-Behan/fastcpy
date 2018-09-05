import io
import sys
import os
import wx

def uiSetup():
    # Create application object.
    app = wx.App()

    # Create ui frame.
    frame = wx.Frame(None, title="FastCpy")

    # Display frame.
    frame.Show()

    # Start the event loop.
    app.MainLoop()

def main():
    uiSetup()
    target_folder = input("Enter the name and path of the file you wish to copy.")
    destination_folder = input("Enter the destination path you wish to copy the files too.")
    os.system('rsync -ru %s/ %s' % (target_folder, destination_folder))

if __name__ == '__main__':
    main()

