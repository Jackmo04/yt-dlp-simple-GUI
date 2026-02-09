from gui import GUI
from controller import Controller

if __name__ == "__main__":
    gui = GUI()
    controller = Controller(gui)
    gui.set_controller(controller)
    gui.begin()
    