import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QVBoxLayout
from PyQt5.QtCore import Qt, QTime, QTimer

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 500, 150)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-family: Arial;"
                                      "font-size: 150px;"
                                      "color: cyan;")
        self.setStyleSheet("background-color: black")

        self.timer.timeout.connect(self.UpdateTime)
        self.timer.start(1000)
        self.UpdateTime()


    def UpdateTime(self):
        current_time = QTime.currentTime().toString("hh:mm:ss ap")
        self.time_label.setText(current_time)


def main():
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
