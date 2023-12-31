from PyQt5.QtCore import Qt
from random import shuffle
from PyQt5.QtWidgets import(QApplication,QWidget,QButtonGroup,QHBoxLayout,QVBoxLayout,QGroupBox,QRadioButton,QPushButton,QLabel)

class Question():
    def __init__(self,Question,right_answer,wrong1,wrong2,wrong3):
        self.Question=Question
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3

questions_list=[]
questions_list.append(Question('Государственый язык Бразилии','Португальский','Английский','Испанский','Итальянский'))
questions_list.append(Question('Какого цвета нет на флаге России?','Зелёный','Красный','Белый','Синий'))
questions_list.append(Question('Национальная хижина якутов','Ураса','Юрта','Иглу','Хата'))

app=QApplication([])
window=QWidget()
window.setWindowTitle('Memory Card')
btn_OK=QPushButton('Answer')
lb_Quession=QLabel('Какой национальности не существует?')
RadioGroupBox=QGroupBox('Варианты ответов')
rbtn_1=QRadioButton('Энцы')
rbtn_2=QRadioButton('Смурфы')
rbtn_3=QRadioButton('Чулымцы')
rbtn_4=QRadioButton('Алеуты')
layout_ans1=QVBoxLayout()
layout_ans2=QHBoxLayout()
layout_ans3=QHBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
layout_line1=QHBoxLayout()
layout_line2=QHBoxLayout()
layout_line3=QHBoxLayout()
layout_line1.addWidget(lb_Quession,alignment=(Qt.AlignHCenter|Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK,stretch=2)
layout_line3.addStretch(1)
layout_card=QVBoxLayout()
layout_card.addLayout(layout_line1,stretch=2)
layout_card.addLayout(layout_line2,stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3,stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
'''window.setLayout(layout_card)'''

AnsGroupBox=QGroupBox('Результаты теста')
lb_Result=QLabel('прав ты или нет?')
lb_Correct=QLabel('ответ будет тут!')
layout_res=QVBoxLayout()
layout_res.addWidget(lb_Result,alignment=Qt.AlignLeft)
layout_res.addWidget(lb_Correct,alignment=Qt.AlignCenter,stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

RadioGroup=QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

'''def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_quession():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def test():
    if'Ответить'==btn_OK.text():
        show_result()
    else:
        show_quession()'''

answers=[rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Quession.setText(q.Question)
    lb_Correct.setText(q.right_answer)
    show_quession()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')

def next_question():
    window.cur_question=window.cur_question+1
    if window.cur_question>=len(questions_list):
        window.cur_question=0
    q=questions_list[window.cur_question]
    ask(q)

def click_OK():
    if btn_OK.text()=='Ответить':
        check_answer()
    else:
        next_question()

window.cur_question = -1
btn_OK.clicked.connect(click_OK)
window.setLayout(layout_card)
window.show()
app.exec()