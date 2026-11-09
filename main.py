# 캠핑 퀴즈 게임 

# ===== Quiz 클래스: 퀴즈 문제 하나를 표현 =====

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 문제와 선택지를 화면에 보여 주기

    def display(self, number):
        print("-" * 40)  
        print(f"[문제 {number}]")
        print(self.question)
        print() 
        for i, option in enumerate(self.choices, start=1):
            print(f"{i}. {option}")
        print()

    # 정답인지 확인하기 (맞으면 True, 틀리면 False)

    def check_answer(self, user_answer):
        return user_answer == self.answer

# ===== 메뉴 =====

while True:
    print("=" * 40)
    print("       ⛺ 나만의 캠핑 퀴즈 게임 ⛺")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인") 
    print("5. 종료")
    print("=" * 40)
     
    choice = input("선택: ").strip() 

    if choice == "":
        print("입력이 비어 있습니다. 1-5 사이의 숫자를 입력하세요.")
        continue

    try:
        number = int(choice)
    except ValueError:
        print("숫자가 아닙니다. 1-5사이의 숫자를 입력하세요.")
        continue

    if number < 1 or number > 5:
        print("범위를 벗어났습니다. 1-5 사이의 숫자를 입력하세요.")
        continue

    if number == 1:
        print("퀴즈 풀기를 선택했습니다.")
    elif number == 2:
        print("퀴즈 추가를 선택했습니다.")  
    elif number == 3:
        print("퀴즈 목록을 선택했습니다.")
    elif number == 4:
        print("점수 확인을 선택했습니다.")
    elif number == 5:
        print("게임을 종료합니다. 다음 캠핑에서 만나요!")
        break
    