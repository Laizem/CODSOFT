import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.num1_label = QLabel("Number 1:")
        self.num1_input = QLineEdit()
        self.num2_label = QLabel("Number 2:")
        self.num2_input = QLineEdit()
        self.result_label = QLabel("Result:")
        self.result_output = QLabel()
        self.add_button = QPushButton("Add")

        # Create layouts
        main_layout = QVBoxLayout()
        input_layout = QHBoxLayout()
        output_layout = QHBoxLayout()

        # Add widgets to layouts
        input_layout.addWidget(self.num1_label)
        input_layout.addWidget(self.num1_input)
        input_layout.addWidget(self.num2_label)
        input_layout.addWidget(self.num2_input)
        output_layout.addWidget(self.result_label)
        output_layout.addWidget(self.result_output)

        main_layout.addLayout(input_layout)
        main_layout.addLayout(output_layout)
        main_layout.addWidget(self.add_button)

        self.setLayout(main_layout)

        # Connect button to function
        self.add_button.clicked.connect(self.calculate_sum)

    def calculate_sum(self):
        try:
            num1 = float(self.num1_input.text())
            num2 = float(self.num2_input.text())
            result = num1 + num2
            self.result_output.setText(str(result))
        except ValueError:
            self.result_output.setText("Invalid input")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.setWindowTitle("Simple Calculator")
    window.show()
    sys.exit(app.exec())