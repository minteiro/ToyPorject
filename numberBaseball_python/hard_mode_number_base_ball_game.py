import random


def intro():
    print("+------------------------------------------------------+")
    print("|             궁극의 숫자 야구 게임(매운맛)            |")
    print("+------------------------------------------------------+")
    print("|  컴퓨터가 수비수가 되어 세 자릿수를 하나 골랐습니다. |")
    print("|  각 숫자는 0~9중에 하나며 중복되는 숫자는 없습니다.  |")
    print("|  모든 숫자와 위피를 맞히면 승리합니다.               |")
    print("|  숫자와 순서가 둘 다 맞으면 스트라이크 입니다.       |")
    print("|  숫자만 맞고 순서가 틀리면 볼입니다.                 |")
    print("|  숫자가 틀리면 아웃 입니다.                          |")
    print("+------------------------------------------------------+")


def user_defence():  # 유저 수비수 정하기
    t = 0
    while t < 3:
        t = 0
        num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        global user_select_numbers
        user_select_numbers = []
        for i in range(1, 4):
            num = input(" %s 번째 수비수를 입력하세요: " % str(i))
            if num in num_list:  # num_list에서 숫자를 뽑고 뽑은 숫자는 리스트에서 제거
                num_list.remove(num)
                user_select_numbers.append(num)
                t = t + 1
            elif num in user_select_numbers:  # index error 안뜨게 반복으로 처리
                t = t - 100
            else:  # num_list에 있는 숫자가 아닌 문자열 이 입력됬을때 #index error 안뜨게 반복으로 처리
                t = t - 1000

        if t == 3:  # 정상 적으로 숫자를 뽑앗을 때 str로 저장되있던 수들을 int로 변경
            for i in range(0, 3):
                n = user_select_numbers[i]
                n = int(n)
                user_select_numbers[i] = n
            print("########################################################")
            print("당신의 수비수:", user_select_numbers)
            print("########################################################")
        elif -500 < t < 0:  # 중복
            print("중복된 수를 선택할 수 없습니다.")
        elif t < -500:  # 예외문자열
            print("0~9사이의 숫자를 입력해 주세요.")


def rcp():  # 가위바위보
    print("공격 순서를 정합니다.")
    t = 0
    global winner
    while t == 0:  # t != 0 이되면 반복문 탈출
        com = random.choice(["가위", "바위", "보"])
        print("########################################################")
        user = input("가위~바위~보!!: ")
        print("########################################################")

        winner = None
        if com == "가위":
            if user == "가위":
                winner = "무승부"
            elif user == "바위":
                winner = "user"
            elif user == "보":
                winner = "computer"
            else:
                winner = str(user)
        elif com == "바위":
            if user == "가위":
                winner = "computer"
            elif user == "바위":
                winner = "무승부"
            elif user == "보":
                winner = "user"
            else:
                winner = str(user)
        else:
            if user == "가위":
                winner = "user"
            elif user == "바위":
                winner = "computer"
            elif user == "보":
                winner = "무승부"
            else:
                winner = str(user)

        if winner == "computer":
            print("컴퓨터: ", com)
            print("사용자: ", user)
            print("승자 : ", "컴퓨터")
            print("컴퓨터가 선공 합니다.")
            t = 1
        elif winner == "user":
            print("컴퓨터: ", com)
            print("사용자: ", user)
            print("승자 : ", "사용자")
            print("사용자가 선공 합니다.")
            t = 2
        elif winner == "무승부":
            print("컴퓨터: ", com)
            print("사용자: ", user)
            print("승자 : ", "무승부")
            t = 0
        else:
            print("가위, 바위, 보 중 하나를 입력해주세요")
            t = 0


def user_attack():  # 유저 공격수 처리 알고리즘
    global user_st_count
    global user_ba_count
    global user_ou_count
    user_st_count = 0
    user_ba_count = 0
    user_ou_count = 0
    t = 0
    while t < 3:  # 중복, 예외 문자열 처리
        t = 0
        num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        user_guess = []
        for i in range(1, 4):
            num = input(" %s 번째 공격수를 입력하세요: " % str(i))
            if num in num_list:
                num_list.remove(num)
                user_guess.append(num)
                t = t + 1
            elif num in user_guess:
                t = t - 100
            else:
                t = t - 1000
        if t == 3:
            for i in range(0, 3):
                n = user_guess[i]
                n = int(n)
                user_guess[i] = n
            print("당신의 공격수:", user_guess)
        elif -500 < t < 0:
            print("중복된 수를 선택할 수 없습니다.")
        elif t < -500:
            print("0~9사이의 숫자를 입력해 주세요.")

    for i in range(0, 3):  # 점수 판단 아고리즘
        if user_guess[i] == com_select_numbers[i]:
            user_st_count = user_st_count + 1
        elif user_guess[i] in com_select_numbers:
            user_ba_count = user_ba_count + 1
        else:
            user_ou_count = user_ou_count + 1
    print_user_count()
    if user_st_count == 3:
        print('경기가 종료 되었습니다.')
        print("########################################################")
        print("winner: you")
        print("########################################################")
        quit()


def line_up():  # 컴퓨터 공격 숫자 조합 만들기
    num = 122
    for i in range(123, 988):
        num = num + 1
        str_num = str(num)
        if str_num[0] != str_num[1]:
            if str_num[1] != str_num[2]:
                if str_num[2] != str_num[0]:
                    a = int(str_num[0])
                    b = int(str_num[1])
                    c = int(str_num[2])
                    line_up = []
                    line_up.append(a)
                    line_up.append(b)
                    line_up.append(c)
                    line_up_list.append(line_up)
    # print(line_up_list) #컴퓨터 공격 숫자 조합


def computer_attack():  # 컴퓨터 공격 알고리즘
    global numbers
    global q
    global st_count
    global ba_count
    global ou_count
    # global com_guess
    random.shuffle(line_up_list)
    com_guess = line_up_list[0]  # 숫자 선정(랜덤)
    print(com_guess)
    line_up_list.remove(com_guess)  # 선정 숫자 제거

    st_count = 0
    ba_count = 0
    ou_count = 0
    for i in range(0, 3):  # 점수판정
        if com_guess[i] == user_select_numbers[i]:
            st_count = st_count + 1
        elif com_guess[i] in user_select_numbers:
            ba_count = ba_count + 1
        else:
            ou_count = ou_count + 1
    print_count()  # 점수표시
    score = []
    score.append(st_count)
    score.append(ba_count)
    score.append(ou_count)

    x_count = 0
    for j in range(0, len(line_up_list)):  # 점수기반 라인업 제거
        jd_st_count = 0
        jd_ba_count = 0
        jd_ou_count = 0
        jd_guess = line_up_list[j]
        for k in range(0, 3):  # 점수판정
            if jd_guess[k] == com_guess[k]:
                jd_st_count = jd_st_count + 1
            elif jd_guess[k] in com_guess:
                jd_ba_count = jd_ba_count + 1
            else:
                jd_ou_count = jd_ou_count + 1

        jd_score = []
        jd_score.append(jd_st_count)
        jd_score.append(jd_ba_count)
        jd_score.append(jd_ou_count)

        if score != jd_score:
            line_up_list[j] = "x"
            x_count = x_count + 1

    for x in range(0, x_count):  # 생성된 "x" 제거
        line_up_list.remove("x")
    # print(line_up_list) #컴퓨터의 남은 수

    q = q + 1

    if st_count == 3:
        print('경기가 종료 되었습니다.')
        print("########################################################")
        print("winner: computer")
        print("########################################################")
        print("컴퓨터의 수비수:", com_select_numbers)
        print("########################################################")
        quit()


def print_count():  # 컴퓨터 점수판
    print("s | " + "🔴 "*st_count + "⚫ "*(3-st_count) + "| " + str(st_count))
    print("b | " + "🔴 "*ba_count + "⚫ "*(3-ba_count) + "| " + str(ba_count))
    print("o | " + "🔴 "*ou_count + "⚫ "*(3-ou_count) + "| " + str(ou_count))


def print_user_count():  # 유저 점수판
    print("s | " + "🔵 "*user_st_count + "⚫ " *
          (3-user_st_count) + "| " + str(user_st_count))
    print("b | " + "🔵 "*user_ba_count + "⚫ " *
          (3-user_ba_count) + "| " + str(user_ba_count))
    print("o | " + "🔵 "*user_ou_count + "⚫ " *
          (3-user_ou_count) + "| " + str(user_ou_count))


def com_user():  # 컴퓨터 선공
    while True:
        print("#######################", q +
              1, "회차 #########################")
        computer_attack()
        user_attack()


def user_com():  # 유저 선공
    while True:
        print("#######################", q +
              1, "회차 #########################")
        user_attack()
        computer_attack()


# 게임시작
intro()
##################################################################
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(numbers)
com_select_numbers = []
for i in range(0, 3):
    com_select_numbers.append(numbers[i])
# print(com_select_numbers)  # 치트키
print("########################################################")
print("컴퓨터가 수비수를 골랏습니다.")
print("########################################################")
##################################################################
line_up_list = []
line_up()
##################################################################
q = 0
user_select_numbers = []
user_defence()
##################################################################
winner = None
rcp()
##################################################################
if winner == "computer":
    com_user()
elif winner == "user":
    user_com()
    
##################################################################
