import sys
import csv
from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView, QMessageBox
from PyQt6.QtCore import Qt

class PeriodicTableWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Таблица Химических элементов Менделеева')
        self.setGeometry(100, 100, 800, 400)

        layout = QVBoxLayout()

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(12)
        self.tableWidget.setColumnCount(14)

        with open('periodic_table.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 5:
                    symbol = row[0]
                    full_name = row[1]
                    group = row[2]
                    period = row[3]
                    mass = row[4]

                    item = QTableWidgetItem(symbol)
                    item.setData(Qt.ItemDataRole.ToolTipRole, f"Название: {full_name}.\nМасса элемента: {mass}")
                    self.tableWidget.setItem(int(period) - 1, int(group) - 1, item)

        self.tableWidget.setHorizontalHeaderLabels(["1", "2", "3", "4", "5", "6", "7", "8"])
        self.tableWidget.setVerticalHeaderLabels(["1", "2", "3", "4.1", "4.2", "5.1", "5.2","6.1","6.2" ,"7","Лантаноиды","Актиноиды"])

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.tableWidget.cellClicked.connect(self.showElementDetails)

    def showElementDetails(self, row, col):
        item = self.tableWidget.item(row, col)
        element_info = item.data(Qt.ItemDataRole.ToolTipRole)
        QMessageBox.information(self, "Элемент", element_info)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PeriodicTableWidget()
    window.show()
    sys.exit(app.exec())