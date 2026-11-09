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

# ===== 기본 캠핑 퀴즈 데이터 =====
def get_default_quizzes():
    return [
        Quiz(
            "텐트 아래에 깔아 바닥의 습기를 막아 주는 것은?",
            ["타프", "그라운드시트", "랜턴", "코펠"],
            2
        ),
        Quiz(
            "햇빛과 비를 가리기 위해 텐트 위나 옆에 치는 넓은 천은?",
            ["타프", "침낭", "매트", "버너"],
            1
        ),
        Quiz(
            "텐트를 땅에 단단히 고정할 때 박는 말뚝은?",
            ["코펠", "펙", "랜턴", "릴선"],
            2
        ),
        Quiz(
            "밀폐된 텐트 안에서 숯불이나 난로를 피우면 위험한 가장 큰 이유는?",
            ["연기 냄새가 배서", "일산화탄소 중독 위험", "텐트 색이 바래서", "벌레가 모여서"],
            2
        ),
        Quiz(
            "캠핑장에서 조용히 해야 하는 '매너 타임'은 보통 몇 시부터일까?",
            ["오후 6시", "오후 8시", "밤 10시", "새벽 2시"],
            3
        ),
        Quiz(
            "캠핑에서 쓰는 휴대용 냄비·그릇 세트를 부르는 말은?",
            ["코펠", "타프", "펙", "스토브"],
            1
        ),
    ]

 # ===== 숫자 입력 받기 (공통 입력 검사) =====
def get_number_input(prompt, min_value, max_value):
    while True:
        text = input(prompt).strip()

        if text == "":
            print(f"입력이 비어 있습니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue

        try:
            value = int(text)
        except ValueError:
            print(f"숫자가 아닙니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue

        if value < min_value or value > max_value:
            print(f"범위를 벗어났습니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue

        return value


# ===== 퀴즈 풀기 =====
def play_quiz(quizzes):
    # 퀴즈가 하나도 없을 때
    if len(quizzes) == 0:
        print("등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
        return

    total = len(quizzes)
    correct = 0

    print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)")

    for i, quiz in enumerate(quizzes, start=1):
        quiz.display(i)
        answer = get_number_input("정답 입력: ", 1, 4)

        if quiz.check_answer(answer):
            print("✅ 정답입니다!")
            correct += 1
        else:
            right_text = quiz.choices[quiz.answer - 1]
            print(f"❌ 오답입니다. 정답은 {quiz.answer}번 ({right_text}) 입니다.")

    score = int(correct / total * 100)
    print("=" * 40)
    print(f"🏆 결과: {total}문제 중 {correct}문제 정답! ({score}점)")
    print("=" * 40)
    return correct


# ===== 퀴즈 목록 준비 =====
quizzes = get_default_quizzes()

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
        print("숫자가 아닙니다. 1-5 사이의 숫자를 입력하세요.")
        continue

    if number < 1 or number > 5:
        print("범위를 벗어났습니다. 1-5 사이의 숫자를 입력하세요.")
        continue

    if number == 1:
        play_quiz(quizzes)
    elif number == 2:
        print("퀴즈 추가를 선택했습니다.")
    elif number == 3:
        print("퀴즈 목록을 선택했습니다.")
    elif number == 4:
        print("점수 확인을 선택했습니다.")
    elif number == 5:
        print("게임을 종료합니다. 다음 캠핑에서 만나요!")
        break
    