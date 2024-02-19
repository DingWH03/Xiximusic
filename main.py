from widget import *
import threading
import chardet

class xiximusic:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.widget = Widget()

    def run(self):
        self.widget.show()
        sys.exit(self.app.exec())

if __name__ == "__main__":
    my_app = xiximusic()
    my_app.run()
