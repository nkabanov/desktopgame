import sys
import random

from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QGraphicsDropShadowEffect, QLabel, QListWidgetItem
from gui import Ui_MainWindow
from regimes import spisok, Znachenie, Synonyms, Usage, Poisk_po_bukvam, Dictionary
from spisok_sokratscheniy import spisok_sokratschenij
import sqlite3

conn = sqlite3.connect("../data/feedback.db", check_same_thread=False)
cursor = conn.cursor()
conn.commit()
class TranslatorGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.user_data = {
            'rounds': 0,
            'lives': 3,
            'current_answer': '',
            'options': [],
            'correct_answers': 0,
            'used_words': [],
            'synonyms': []
        }

        self.setup_connections()
        self.update_game_status()

        self.add_shadows_to_main_menu()

    def setup_connections(self):
        self.ui.btn_gamemodes_2.clicked.connect(self.gamemodes)
        self.ui.btn_dictionary_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dictionary))
        self.ui.btn_feedback_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.feedback_page))
        self.ui.btn_stats.clicked.connect(self.statistics)

        for attr_name in dir(self.ui):
            if attr_name.startswith('back_'):
                back_button = getattr(self.ui, attr_name)
                if back_button:
                    back_button.clicked.connect(
                        lambda _, page=self.ui.main_menu: self.ui.stackedWidget.setCurrentWidget(page)
                    )
        for attr_name in dir(self.ui):
            if attr_name.startswith('letter_'):
                letter_button = getattr(self.ui, attr_name)
                if isinstance(letter_button, QPushButton):
                    letter = letter_button.text().strip()
                    letter_button.clicked.connect(lambda _, l=letter: self.show_words_for_letter(l))

        self.ui.btn_easymode.clicked.connect(self.start_easy_game)
        self.ui.btn_hardmode.clicked.connect(self.start_hard_game)

        self.ui.btn_user_search.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.user_search))
        self.ui.another_search.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.user_search))
        self.ui.btn_po_bukvam.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.letter_search))
        self.ui.btn_sokr_list.clicked.connect(self.show_abbreviation_list)

        self.ui.easy_answer1.clicked.connect(lambda: self.check_easy_answer(0))
        self.ui.easy_answer2.clicked.connect(lambda: self.check_easy_answer(1))
        self.ui.easy_answer3.clicked.connect(lambda: self.check_easy_answer(2))

        self.ui.lineEdit.returnPressed.connect(self.check_hard_answer)
        self.ui.lineEdit_2.returnPressed.connect(self.user_dictionary_input)
        self.ui.lineEdit_3.returnPressed.connect(self.feedback_input)

        self.ui.list_words.itemClicked.connect(self.show_word_info)
        self.ui.another_search_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.letter_search))
        self.ui.reset_stats.clicked.connect(self.reset_stats)

        self.ui.lineEdit_2.textChanged.connect(self.update_search_results)
        self.ui.listWidget.itemClicked.connect(self.user_search_info)

    def gamemodes(self):
        self.user_data = {
            'rounds': 0,
            'lives': 3,
            'current_answer': '',
            'options': [],
            'correct_answers': 0,
            'used_words': [],
            'synonyms': []
        }
        self.ui.stackedWidget.setCurrentWidget(self.ui.game_modes)

    def update_game_status(self):
        self.ui.label_18.setText(f'Раунд: {self.user_data["rounds"]}')
        self.ui.label_17.setText(f'❤️ Жизни: {self.user_data["lives"]}')
        self.ui.label_19.setText(f'Раунд: {self.user_data["rounds"]}')
        self.ui.label_20.setText(f'❤️ Жизни: {self.user_data["lives"]}')

    def start_easy_game(self):
        available_words = [word for word in spisok if word not in self.user_data['used_words']]
        self.user_data['rounds'] += 1
        self.update_game_status()
        self.user_data['current_answer'] = random.choice(available_words)
        self.user_data['used_words'].append(self.user_data['current_answer'])
        self.user_data['options'] = [
            Znachenie(self.user_data['current_answer'])
        ] + random.sample(
            [Znachenie(w) for w in spisok if w != self.user_data['current_answer']], 2)
        random.shuffle(self.user_data['options'])

        self.ui.label_6.setText(f"Выберите определение для слова: {self.user_data['current_answer']}")
        self.set_wrapped_text(self.ui.easy_answer1, self.user_data['options'][0])
        self.set_wrapped_text(self.ui.easy_answer2, self.user_data['options'][1])
        self.set_wrapped_text(self.ui.easy_answer3, self.user_data['options'][2])

        self.ui.stackedWidget.setCurrentWidget(self.ui.easy_game)

    def check_easy_answer(self, choice_index):
        correct_answer = Znachenie(self.user_data['current_answer'])
        if self.user_data['options'][choice_index] == correct_answer:
            self.user_data['correct_answers'] += 1
            self.msgbox_correct()
        else:
            self.user_data['lives'] -= 1
            self.update_game_status()
            self.msgbox_wrong(correct_answer)
            if self.user_data['lives'] == 0:
                self.end_game()
                return
        if self.user_data['rounds'] > 9:
            self.end_game()
            return
        self.start_easy_game()

    def start_hard_game(self):
        words_with_synonyms = [word for word in spisok if Synonyms(word) and word not in self.user_data['used_words']]

        self.user_data['rounds'] += 1
        self.update_game_status()

        self.user_data['current_answer'] = random.choice(words_with_synonyms)
        self.user_data['used_words'].append(self.user_data['current_answer'])
        synonyms = Synonyms(self.user_data['current_answer'])
        self.user_data['synonyms'] = synonyms.split(', ')

        usage = Usage(self.user_data['current_answer'])
        self.ui.label_6.setText(
            f"""Определите синоним для слова: {self.user_data['current_answer']}\nПример: {usage}"""
        )
        self.ui.label_2.setText(
            f"Введите синоним для слова: {self.user_data['current_answer']}"
        )
        self.ui.lineEdit.clear()
        self.ui.stackedWidget.setCurrentWidget(self.ui.hard_game)

    def check_hard_answer(self):
        user_input = self.ui.lineEdit.text().strip().lower()
        if user_input in [syn.lower() for syn in self.user_data['synonyms']]:
            self.user_data['correct_answers'] += 1
            self.msgbox_correct()
            if self.user_data['rounds'] > 9:
                self.end_game()
                return
        else:
            self.user_data['lives'] -= 1
            self.update_game_status()
            self.msgbox_wrong(', '.join(self.user_data['synonyms']))
            if self.user_data['lives'] == 0:
                self.end_game()
                return
            if self.user_data['rounds'] > 9:
                self.end_game()
                return
        self.start_hard_game()

    def end_game(self):
        self.ui.label_66.setText(
            f"Игра закончена!\nВы правильно ответили на {self.user_data['correct_answers']} из {self.user_data['rounds']} вопросов.")
        self.ui.stackedWidget.setCurrentWidget(self.ui.game_result)
        if self.user_data['lives'] > 0:
            cursor.execute("UPDATE stats SET games_won = games_won + 1")
        cursor.execute("UPDATE stats SET games_played = games_played + 1")
        cursor.execute("UPDATE stats SET correct_answers = correct_answers + ?",
                       (self.user_data['correct_answers'],))
        conn.commit()
        self.user_data['rounds'] = 0
        self.user_data['lives'] = 3
        self.user_data['used_words'] = []
        self.update_game_status()

    def feedback_input(self):
        feedback = str(self.ui.lineEdit_3.text())
        cursor.execute("INSERT INTO feedbacks (feedback) VALUES (?)", (feedback,))
        conn.commit()
        self.ui.lineEdit_3.clear()
        self.ui.stackedWidget.setCurrentWidget(self.ui.feedback_ty)

    def user_dictionary_input(self):
        word = self.ui.lineEdit_2.text().strip().upper()
        result = Znachenie(word)
        self.ui.label_68.setText(f"Информация о слове {word}\n\n\n\n{result}")
        self.ui.lineEdit_2.clear()
        self.ui.label_68.setWordWrap(True)
        self.ui.stackedWidget.setCurrentWidget(self.ui.user_search_result)

    def update_search_results(self):
        search_term = self.ui.lineEdit_2.text().strip().lower()
        if search_term:
            filtered_words = [word for word in spisok if word.lower().startswith(search_term)]
        else:
            filtered_words = ""

        self.update_word_list(filtered_words)

    def update_word_list(self, filtered_words):
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(filtered_words)

    def user_search_info(self, item):
        word = item.text()
        info = Dictionary(word)
        self.ui.lineEdit_2.clear()
        self.ui.label_68.setText(info)
        self.ui.stackedWidget.setCurrentWidget(self.ui.user_search_result)


    def show_abbreviation_list(self):
        self.ui.label_16.setText(f"Список сокращений\n\n{spisok_sokratschenij}")
        self.ui.label_68.setWordWrap(True)
        self.ui.stackedWidget.setCurrentWidget(self.ui.sokr_list)

    def statistics(self):
        cursor.execute("SELECT games_played, games_won, correct_answers FROM stats")
        result = cursor.fetchone()
        if result:
            games_played, games_won, correct_answers = result
            self.ui.label_9.setText(
                f"Сыграно игр: {games_played}\n\n"
                f"Выиграно игр: {games_won}\n\n"
                f"Правильных ответов: {correct_answers}"
            )
        self.ui.stackedWidget.setCurrentWidget(self.ui.stats)

    def reset_stats(self):
        cursor.execute("UPDATE stats SET games_won = 0")
        cursor.execute("UPDATE stats SET games_played = 0")
        cursor.execute("UPDATE stats SET correct_answers = 0")
        cursor.execute("SELECT games_played, games_won, correct_answers FROM stats")
        result = cursor.fetchone()
        if result:
            games_played, games_won, correct_answers = result
            self.ui.label_9.setText(
                f"Сыграно игр: {games_played}\n\n"
                f"Выиграно игр: {games_won}\n\n"
                f"Правильных ответов: {correct_answers}"
            )
        conn.commit()
    def show_word_info(self, item):
        word = item.text()
        info = Dictionary(word)

        self.ui.label_76.setText(info)

        self.ui.stackedWidget.setCurrentWidget(self.ui.letter_search_result)

    def show_words_for_letter(self, letter):
        words = Poisk_po_bukvam(letter)
        self.ui.list_words.clear()
        if words:
            for word in words:
                self.ui.list_words.addItem(QListWidgetItem(word))
        else:
            self.ui.list_words.addItem(QListWidgetItem("Нет слов на эту букву"))

        self.ui.stackedWidget.setCurrentWidget(self.ui.letter_search_words)

    def add_shadows_to_main_menu(self):
        for button in self.ui.main_menu.findChildren(QPushButton):
            shadow = QGraphicsDropShadowEffect(self)
            shadow.setBlurRadius(3)
            shadow.setXOffset(5)
            shadow.setYOffset(6)
            shadow.setColor(QColor(0, 0, 0, 150))
            button.setGraphicsEffect(shadow)

        for label in self.ui.main_menu.findChildren(QLabel):
            shadow = QGraphicsDropShadowEffect(self)
            shadow.setBlurRadius(3)
            shadow.setXOffset(5)
            shadow.setYOffset(6)
            shadow.setColor(QColor(0, 0, 0, 150))
            label.setGraphicsEffect(shadow)

    def set_wrapped_text(self, button: QPushButton, text: str):
        words = text.split()
        wrapped_text = ''
        line = ''
        for word in words:
            if len(line + word) <= 30:
                line += word + ' '
            else:
                wrapped_text += line.rstrip() + '\n'
                line = word + ' '
        wrapped_text += line.rstrip()
        button.setText(wrapped_text)

    def msgbox_correct(self):
        messagebox = QMessageBox()
        messagebox.setWindowTitle("Результат")
        messagebox.setText("Правильно!")
        messagebox.addButton('Следующий раунд', QMessageBox.AcceptRole)
        messagebox.setStyleSheet(
            """
            QMessageBox {
                background-color: rgb(208, 233, 244);
                border: 2px solid black;
                border-radius: 0px;
                color: black;
                font-size: 20px;
                font-weight: bold;
            }
            QLabel#qt_msgbox_label {
                qproperty-alignment: AlignCenter;
                min-width: 250px;
            }
            QPushButton {
                min-width: 50px;
                padding: 5px;
                justify-content: center; 
            }
            """
        )
        messagebox.exec()

    def msgbox_wrong(self, otvet):
        messagebox = QMessageBox()
        messagebox.setWindowTitle("Результат")
        messagebox.setText(f"Неправильно! Правильный ответ: {otvet}")
        messagebox.addButton('Следующий раунд', QMessageBox.AcceptRole)
        messagebox.setStyleSheet(
            """
            QMessageBox {
                background-color: rgb(208, 233, 244);
                border: 2px solid black;
                border-radius: 0px;
                color: black;
                font-size: 20px;
                font-weight: bold;
            }
            QLabel {
                qproperty-alignment: AlignCenter;
            }
            QPushButton {
                min-width: 50px;
                padding: 5px;
                justify-content: center; 
            }
            """
        )
        messagebox.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TranslatorGame()
    window.resize(1280, 720)
    window.show()
    sys.exit(app.exec())
