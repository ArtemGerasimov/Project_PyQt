import sqlite3
import sys
from docx import Document
from datetime import date

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTextBrowser, QGridLayout


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('progect.ui', self)
        self.setFixedSize(800, 600)

        self.criteria.addItem('Выберите критерий')
        self.criteria.addItem('Код переработки')
        self.criteria.addItem('Материал')
        self.criteria.addItem('Название')

        self.comboBox.hide()

        self.comboBox.addItem('Выберите материал')

        self.search.clicked.connect(self.run)
        self.calendarWidget.selectionChanged.connect(self.calen)
        self.record.clicked.connect(self.mean)
        self.statistic.clicked.connect(self.stat)
        self.help_2.clicked.connect(self.help)

    def run(self):
        self.comboBox.hide()
        self.error.setText('')
        self.name_2.setText('')
        self.code_2.setText('')
        self.metod_2.setText('')
        con = sqlite3.connect('new_life_2.db')
        cur = con.cursor()
        if self.criteria.currentText() == 'Выберите критерий':
            self.error.setText('Критерий не выбран')
        elif self.criteria.currentText() == 'Материал':
            result = cur.execute(f"""SELECT code FROM materials
                                        WHERE material == '{self.criteria_2.text().capitalize()}'""").fetchone()
            if result:
                self.name_2.setText(self.criteria_2.text())
                self.code_2.setText(result[0])
                result_2 = cur.execute(f"""SELECT method FROM materials 
                                            WHERE code == '{result[0]}'""").fetchall()
                self.metod_2.setText(result_2[0][0])
            else:
                self.error.setText('Такой материал не перерабатывается.')
        elif self.criteria.currentText() == 'Код переработки':
            result = cur.execute(f"""SELECT material FROM materials
                                        WHERE code LIKE '%{self.criteria_2.text()} %'""").fetchall()
            if len(result) == 1:
                self.cod_1()
            elif len(result) > 1:
                self.comboBox.clear()
                self.comboBox.addItem('Выберите материал')
                for i in range(len(result)):
                    self.comboBox.addItem(result[i][0])
                self.comboBox.show()
                self.comboBox.activated.connect(self.cod_2)
        elif self.criteria.currentText() == 'Название':
            self.title()

    def cod_2(self):
        con = sqlite3.connect('new_life_2.db')
        cur = con.cursor()
        result = cur.execute(f"""SELECT code FROM materials
                                    WHERE material == '{self.comboBox.currentText()}'""").fetchall()
        result_2 = cur.execute(f"""SELECT method FROM materials
                                    WHERE code == '{result[0][0]}'""").fetchall()
        self.name_2.setText(self.comboBox.currentText())
        self.code_2.setText(result[0][0])
        self.metod_2.setText(result_2[0][0])

    def cod_1(self):
        con = sqlite3.connect('new_life_2.db')
        cur = con.cursor()
        result = cur.execute(f"""SELECT * FROM materials
                                    WHERE code LIKE '%{self.criteria_2.text()} %'""").fetchall()
        self.name_2.setText(result[0][1])
        self.code_2.setText(result[0][2])
        self.metod_2.setText(result[0][3])

    def title(self):
        con = sqlite3.connect('new_life_2.db')
        cur = con.cursor()
        result = cur.execute(f"""SELECT material FROM artem
                                    WHERE name LIKE '%{self.criteria_2.text()}%'""").fetchone()
        if not result or result[0] == 20:
            self.error.setText('Такой материал не перерабатывается')
        else:
            result_2 = cur.execute(f"""SELECT * FROM materials
                                    WHERE id == '{result[0]}'""").fetchone()
            self.name_2.setText(f'{result_2[1]}')
            self.code_2.setText(f'{result_2[2]}')
            self.metod_2.setText(f'{result_2[3]}')

    def calendar(self):
        con = sqlite3.connect('calendar.db')
        cur = con.cursor()
        data = date(self.calendarWidget.selectedDate().getDate()[0],
                    self.calendarWidget.selectedDate().getDate()[1],
                    self.calendarWidget.selectedDate().getDate()[2])
        a = self.event.text()
        if len(cur.execute(f"""SELECT date FROM dairy
                                WHERE date == '{data}'""").fetchall()) > 0:
            cur.execute(f"""UPDATE dairy
                            SET text = '{a}'
                            WHERE date == '{data}'""")
        else:
            cur.execute(f"""INSERT INTO dairy(`date`, `text`) VALUES('{data}', '{a}')""")
        con.commit()
        con.close()

    def mean(self):
        con = sqlite3.connect('mean.db')
        cur = con.cursor()
        if len(cur.execute(f"""SELECT name FROM stat
                WHERE name == '{self.meaning.text().strip().lower()}'""").fetchall()) > 0:
            result = cur.execute(f"""SELECT quantity FROM stat
                        WHERE name == '{self.meaning.text().strip().lower()}'""").fetchone()[0]
            result += self.quantity.value()
            cur.execute(f"""UPDATE stat
                        SET quantity = '{result}'
                        WHERE name == '{self.meaning.text().strip().lower()}'""")
        else:
            cur.execute(f"""INSERT INTO stat
                        VALUES('{self.meaning.text().strip().lower()}', '{self.quantity.value()}')""")
            con.commit()
            con.close()

    def help(self):
        self.helper = SecondForm(self, 'Здравствуйте! Моя программа подскажет вам как правильно подготовить '
                                       'вещи к сдаче. Для начала вберите из перечня, в левом верхнем углу, критерий по '
                                       'которому вы хотите узнать как подготовить вещь к сдаче.После этого в строке '
                                       'введите значение согласно выбранному критерию и нажмите поиск. Также вы можете '
                                       'делать заметки в календаре, вести статистику сданных вещей.')
        self.helper.show()

    def calendar_2(self):
        con = sqlite3.connect('calendar.db')
        cur = con.cursor()
        data = date(self.calendarWidget.selectedDate().getDate()[0],
                    self.calendarWidget.selectedDate().getDate()[1],
                    self.calendarWidget.selectedDate().getDate()[2])
        a = self.event.text()
        if len(cur.execute(f"""SELECT date FROM dairy
                WHERE date == '{data}'""").fetchall()) > 0:
            cur.execute(f"""UPDATE dairy
                    SET text = '{a}'
                    WHERE date == '{data}'""")
        else:
            cur.execute(f"""INSERT INTO dairy(`date`, `text`) VALUES('{data}', '{a}')""")
        con.commit()
        con.close()

    def stat(self):
        con = sqlite3.connect('mean.db')
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM stat""").fetchall()
        doc = Document()
        for i in result:
            doc.add_paragraph(f'{i[0]}: {i[1]}')
        doc.save('Статистика.docx')

    def calen(self):
        self.event.setText('')
        con = sqlite3.connect('calendar.db')
        cur = con.cursor()
        data = date(self.calendarWidget.selectedDate().getDate()[0],
                    self.calendarWidget.selectedDate().getDate()[1],
                    self.calendarWidget.selectedDate().getDate()[2])
        result = cur.execute(f"""SELECT text FROM dairy
                                    WHERE date == '{data}'""").fetchone()
        if result:
            self.event.setText(result[0])
        self.event_record.clicked.connect(self.calendar)
        con.commit()
        con.close()


class SecondForm(QWidget):
    def __init__(self, *args):
            super().__init__()
            self.initUI(args)

    def initUI(self, args):
        self.setFixedSize(300, 300)
        self.setWindowTitle('Вторая форма')
        self.lbl = QTextBrowser(self)
        self.lbl.setText(args[-1])
        self.lbl.adjustSize()
        self.grid = QGridLayout(self)
        self.grid.addWidget(self.lbl)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
