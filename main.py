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

 # ===== QuizGame 클래스: 게임 전체를 관리 =====
class QuizGame:
    def __init__(self):
        self.quizzes = get_default_quizzes()   # 퀴즈 목록
        self.best_score = None                 # 최고 점수 (아직 없음)

    # ---------- 입력 처리 ----------
    def get_number_input(self, prompt, min_value, max_value):
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

    def get_text_input(self, prompt):
        while True:
            text = input(prompt).strip()
            if text == "":
                print("입력이 비어 있습니다. 내용을 입력해 주세요.")
                continue
            return text

    # ---------- 화면 ----------
    def show_menu(self):
        print("=" * 40)
        print("       ⛺ 나만의 캠핑 퀴즈 게임 ⛺")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    # ---------- 1. 퀴즈 풀기 ----------
    def play_quiz(self):
        if len(self.quizzes) == 0:
            print("\n등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return

        total = len(self.quizzes)
        correct = 0

        print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)")

        for i, quiz in enumerate(self.quizzes, start=1):
            quiz.display(i)
            answer = self.get_number_input("정답 입력: ", 1, 4)

            if quiz.check_answer(answer):
                print("✅ 정답입니다!")
                correct += 1
            else:
                right_text = quiz.choices[quiz.answer - 1]
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번 ({right_text}) 입니다.")

        score = int(correct / total * 100)
        print("=" * 40)
        print(f"🏆 결과: {total}문제 중 {correct}문제 정답! ({score}점)")

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")
        print("=" * 40)

    # ---------- 2. 퀴즈 추가 ----------
    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.\n")

        question = self.get_text_input("문제를 입력하세요: ")

        choices = []
        for i in range(1, 5):
            option = self.get_text_input(f"선택지 {i}: ")
            choices.append(option)

        answer = self.get_number_input("정답 번호 (1-4): ", 1, 4)

        self.quizzes.append(Quiz(question, choices, answer))
        print(f"\n✅ 퀴즈가 추가되었습니다! (현재 총 {len(self.quizzes)}개)")

    # ---------- 3. 퀴즈 목록 ----------
    def show_quiz_list(self):
        if len(self.quizzes) == 0:
            print("\n등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return

        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)
        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"[{i}] {quiz.question}")
        print("-" * 40)

    # ---------- 4. 점수 확인 ----------
    def show_score(self):
        if self.best_score is None:
            print("\n아직 퀴즈를 풀지 않았습니다. 먼저 퀴즈를 풀어 보세요!")
            return
        print(f"\n🏆 최고 점수: {self.best_score}점")

    # ---------- 게임 실행 (메뉴 반복) ----------
    def run(self):
        while True:
            self.show_menu()
            number = self.get_number_input("선택: ", 1, 5)

            if number == 1:
                self.play_quiz()
            elif number == 2:
                self.add_quiz()
            elif number == 3:
                self.show_quiz_list()
            elif number == 4:
                self.show_score()
            elif number == 5:
                print("게임을 종료합니다. 다음 캠핑에서 만나요!")
                break


# ===== 프로그램 시작 =====
game = QuizGame()   # 게임 가게 열기 (객체 만들기)
game.run()          # 영업 시작! (메뉴 반복 실행)
    