from random import shuffle, randint
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from PyQt5.QtCore import Qt

class Question():
    def __init__(self, question_text, right_answer_text, wrong1_text, wrong2_text, wrong3_text):
        self.question = question_text
        self.right_answer = right_answer_text
        self.wrong1 = wrong1_text
        self.wrong2 = wrong2_text
        self.wrong3 = wrong3_text

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('MemoryCard')
main_win.resize(400, 300)

lb_question = QLabel('Вопрос')
RadioGroupBox = QGroupBox('Варианты ответа')

answer_bnt1 = QRadioButton('1')
answer_bnt2 = QRadioButton('2')
answer_bnt3 = QRadioButton('3')
answer_bnt4 = QRadioButton('4')

AnsGroupBox = QGroupBox('Результат')
is_correct = QLabel('Правильно/Неправильно')
correct_ans = QLabel('Правильный ответ')

correct_layout = QVBoxLayout()
correct_layout.addWidget(is_correct, alignment=(Qt.AlignLeft | Qt.AlignTop))
correct_layout.addWidget(correct_ans, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(correct_layout)

ans_layoutV1 = QVBoxLayout()
ans_layoutV1.addWidget(answer_bnt1)
ans_layoutV1.addWidget(answer_bnt2)

ans_layoutV2 = QVBoxLayout()
ans_layoutV2.addWidget(answer_bnt3)
ans_layoutV2.addWidget(answer_bnt4)

ans_layoutH = QHBoxLayout()
ans_layoutH.addLayout(ans_layoutV1)
ans_layoutH.addLayout(ans_layoutV2)
RadioGroupBox.setLayout(ans_layoutH)

layoutH1 = QHBoxLayout()
layoutH1.addWidget(lb_question, alignment=(Qt.AlignCenter | Qt.AlignCenter))

AnsGroupBox.hide()
RadioGroup = QButtonGroup()
RadioGroup.addButton(answer_bnt1)
RadioGroup.addButton(answer_bnt2)
RadioGroup.addButton(answer_bnt3)
RadioGroup.addButton(answer_bnt4)

bnt_restart = QPushButton("Начать заново")
bnt_restart.hide()

layoutH2 = QHBoxLayout()
RadioGroupBox.show()  
layoutH2.addWidget(RadioGroupBox)
layoutH2.addWidget(AnsGroupBox)
layoutH2.addWidget(bnt_restart)

bnt_answer = QPushButton('Ответить')
bnt_show = QPushButton('Показать ответ')  

layoutH3 = QHBoxLayout()
layoutH3.addStretch(1)
layoutH3.addWidget(bnt_answer, stretch=2)
layoutH3.addWidget(bnt_show, stretch=2) 
layoutH3.addStretch(1)

main_layout = QVBoxLayout()
main_layout.addLayout(layoutH1)
main_layout.addLayout(layoutH2)
main_layout.addLayout(layoutH3)
main_layout.setSpacing(25)

questions_list = [
    Question('Государственный язык Бразилии', 
        'Португальский', 
        'Русский', 
        'Бразильский', 
        'Испанский'),
    Question('Перевод слова "variable"', 
        'Переменная', 
        'Изменение', 
        'Вариация', 
        'Функция'),
    Question('ввв',
        '1лягушка',
        '6',
        '2лягушка',
        'да'), 
    Question('Торжыто',
            'Долр',
            'Одлолд',
            'Йцуццц',
            'Йумсйусйцсу'),
    Question('Тадатата',
            'Ллллллл',
            'Йцукен',
            'Чнт',
            'Опогшякови'),
    Question('La bkb ytn',
            'Rjytxyj la',
            'Rjytxyj ytn',
            'Xcortm',
            'Xnj'), 
    Question('Xфвы',
            'Черепаха',
            'Йдинозавр',
            'Лягушка',
            'Курица'),
    Question('Ааапафвыав',
            'Перепёлка',
            'Йцукен',
            'Воробушек',
            'Вьюрок'),
    Question('Йысаерьлщж',
            'Олнень',
            'Бобер',
            'Пес в парике',
            'Стекляная рука'),
    Question('Яыуамирглю',
            'Девон рекс',
            'Манчкин',
            'Ориинтал',
            'Шотландец'),
    Question('Уепкмавы',
            'Ан-пан',
            'Панеттоне',
            'Пикос',
            'Фугас'),
]   

def restart():
    main_win.total = 0
    main_win.score = 0
    bnt_answer.show()
    bnt_restart.hide()
    next_question()

bnt_restart.clicked.connect(restart)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    bnt_answer.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    bnt_answer.setText('Ответить')
    RadioGroup.setExclusive(False)
    answer_bnt1.setChecked(False)
    answer_bnt2.setChecked(False)
    answer_bnt3.setChecked(False)
    answer_bnt4.setChecked(False)
    RadioGroup.setExclusive(True)

answer = [answer_bnt1, answer_bnt2, answer_bnt3, answer_bnt4]

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_question.setText(q.question)
    correct_ans.setText(q.right_answer)
    show_question()

main_win.total = 0
main_win.score = 0

def check_answer():
    if answer[0].isChecked():
        is_correct.setText('Правильно!')
        main_win.score += 1
    else:
        is_correct.setText('Неправильно!')
    show_result()
    print('Статистика:')
    print(f'- Всего вопросов: {main_win.total}')
    print(f'- Верно: {main_win.score}')
    print(f'- Неверно: {main_win.total - main_win.score}')
    print(f'Рейтинг: {main_win.score / main_win.total * 100:.1f}%')

def show_only_answer():
    is_correct.setText('Правильный ответ:')
    show_result()

def show_final_stats():
    percent = round(main_win.score / main_win.total * 100)
    lb_question.setText(f"Тест завершён! Ваш результат: {percent}%")
    RadioGroupBox.hide()
    AnsGroupBox.hide()
    bnt_answer.hide()
    bnt_restart.show()

def next_question():
    if main_win.total == len(questions_list):
        show_final_stats()
        return
    main_win.total += 1
    remaining = len(questions_list) - main_win.total
    lb_question.setText(f'Осталось вопросов: {remaining}')
    cur_question = randint(0, len(questions_list) - 1)
    ask(questions_list[cur_question])

def click_ok():
    if bnt_answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()

bnt_show.clicked.connect(show_only_answer)
bnt_answer.clicked.connect(click_ok)       

next_question()
main_win.setLayout(main_layout)
main_win.show()
app.exec_()
