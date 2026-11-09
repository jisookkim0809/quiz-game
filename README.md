# 나만의 캠핑 퀴즈 게임

터미널에서 실행하는 캠핑 상식 퀴즈 게임입니다.
퀴즈를 풀고, 새 퀴즈를 추가하고, 목록과 최고 점수를 확인할 수 있습니다.
추가한 퀴즈와 최고 점수는 `state.json`에 저장되어 프로그램을 다시 실행해도 유지됩니다.

| 항목 | 내용 |
|:---|:---|
| 언어 | Python 3.10 이상 (개발 환경: Python 3.15.2) |
| 외부 라이브러리 | 없음 (표준 라이브러리 `json`만 사용) |
| 실행 환경 | 터미널 (Windows PowerShell에서 개발 및 테스트) |
| 데이터 파일 | 프로젝트 루트의 `state.json` (UTF-8) |

---

## 목차

1. [프로젝트 개요](#1-프로젝트-개요)
2. [퀴즈 주제와 선정 이유](#2-퀴즈-주제와-선정-이유)
3. [실행 방법](#3-실행-방법)
4. [기능 목록](#4-기능-목록)
5. [구현 과정](#5-구현-과정)
6. [파일 구조](#6-파일-구조)
7. [데이터 파일 설명 (state.json)](#7-데이터-파일-설명-statejson)
8. [실행 화면](#8-실행-화면)
9. [Git 작업 기록](#9-git-작업-기록)

---

## 1. 프로젝트 개요

Python 기본 문법(변수, 조건문, 반복문, 함수)과 클래스를 사용해 콘솔 퀴즈 게임을 처음부터 끝까지 구현했습니다.
JSON 파일 저장으로 데이터 영속성을 구현했고, Git으로 기능 단위 커밋과 브랜치 병합 기록을 남겼습니다.

### 클래스 구성

코드는 역할에 따라 두 개의 클래스로 나뉩니다.

| 클래스 | 역할 | 속성 | 메서드 |
|:---|:---|:---|:---|
| `Quiz` | 퀴즈 문제 1개를 표현 | `question` (문제)<br>`choices` (선택지 4개)<br>`answer` (정답 번호 1~4) | `display()` 문제와 선택지 출력<br>`check_answer()` 정답 여부 반환<br>`to_dict()` 저장용 dict로 변환 |
| `QuizGame` | 게임 전체를 관리 | `quizzes` (Quiz 객체 목록)<br>`best_score` (최고 점수) | 아래 표 참고 |

### QuizGame 메서드

| 구분 | 메서드 | 설명 |
|:---|:---|:---|
| 게임 진행 | `run()` | 메뉴를 반복 출력하고 선택한 기능 실행 |
| | `show_menu()` | 메뉴 화면 출력 |
| 기능 | `play_quiz()` | 퀴즈 풀기, 채점, 최고 점수 갱신 |
| | `add_quiz()` | 새 퀴즈 입력 및 등록 |
| | `show_quiz_list()` | 등록된 퀴즈 목록 출력 |
| | `show_score()` | 최고 점수 출력 |
| 입력 처리 | `get_number_input()` | 범위 내 숫자를 받을 때까지 반복 입력 (공백, 빈 입력, 문자, 범위 검사) |
| | `get_text_input()` | 빈 입력이 아닐 때까지 반복 입력 |
| 저장 | `load_data()` | 시작 시 `state.json` 불러오기 (파일 없음, 손상 처리) |
| | `save_data()` | 퀴즈 목록과 최고 점수를 `state.json`에 저장 |
| | `reset_to_default()` | 기본 퀴즈로 초기화 후 저장 |

---

## 2. 퀴즈 주제와 선정 이유

**주제: 캠핑**

캠핑은 제가 가장 좋아하는 취미입니다.
캠핑을 다니며 타프, 그라운드시트, 펙, 코펠처럼 처음에는 낯설었던 장비 이름과
텐트 안 일산화탄소 위험, 캠핑장 매너 타임 같은 꼭 알아야 할 안전 수칙과 매너를 하나씩 배웠습니다.

좋아하는 주제라서 즐겁게 문제를 만들 수 있었고,
캠핑을 처음 시작하는 사람에게 실제로 도움이 되는 퀴즈를 만들고 싶어 이 주제를 선택했습니다.

---

## 3. 실행 방법

### 준비 사항

- Python 3.10 이상
- Git

### 실행

```bash
git clone https://github.com/jisookkim0809/quiz-game.git
cd quiz-game
python main.py
```

처음 실행하면 `state.json`이 없으므로 기본 캠핑 퀴즈 6개로 시작하며, `state.json`이 자동으로 생성됩니다.

---

## 4. 기능 목록

### 메뉴 기능

| 번호 | 기능 | 설명 |
|:---:|:---|:---|
| 1 | 퀴즈 풀기 | 등록된 퀴즈를 순서대로 출제하고 정답/오답과 정답 번호를 알려줍니다. 마지막에 점수(100점 만점)를 표시하고, 최고 점수보다 높으면 갱신합니다. |
| 2 | 퀴즈 추가 | 문제, 선택지 4개, 정답 번호(1~4)를 입력받아 새 퀴즈를 등록하고 파일에 저장합니다. |
| 3 | 퀴즈 목록 | 등록된 모든 퀴즈의 문제를 번호와 함께 표시합니다. |
| 4 | 점수 확인 | 최고 점수를 표시합니다. |
| 5 | 종료 | 데이터를 저장하고 프로그램을 종료합니다. |

### 입력 및 예외 처리

| 상황 | 처리 |
|:---|:---|
| 입력 앞뒤 공백 (예: ` 1 `) | 공백을 제거한 뒤 처리 |
| 빈 입력 (Enter만 입력) | 안내 메시지 출력 후 다시 입력 |
| 숫자가 아닌 입력 (예: `abc`) | 안내 메시지 출력 후 다시 입력 |
| 허용 범위 밖 숫자 (예: 메뉴 `9`, 정답 `0`) | 안내 메시지 출력 후 다시 입력 |
| 등록된 퀴즈가 없을 때 풀기/목록 선택 | 안내 메시지 출력 |
| 퀴즈를 풀기 전에 점수 확인 선택 | 안내 메시지 출력 |
| `Ctrl + C` (KeyboardInterrupt) / 입력 종료 (EOFError) | 안내 메시지 출력 후 저장하고 정상 종료 |
| `state.json`이 없음 (첫 실행) | 기본 퀴즈로 시작하고 파일 생성 |
| `state.json`이 손상됨 | 안내 메시지 출력 후 기본 퀴즈로 복구 |

---

## 5. 구현 과정

기능을 하나씩 완성하고, 완성할 때마다 커밋하는 방식으로 진행했습니다.

### 1단계. 개발 환경 준비와 저장소 생성

- Python, Git, VS Code(Python 확장)를 설치하고 Git 사용자 이름과 이메일을 등록했습니다.
- GitHub에 `quiz-game` 저장소를 만들고 `.gitignore`, `README.md`를 작성해 첫 커밋과 push를 했습니다.
- 사용 명령어: `git init`, `git add`, `git commit`, `git push`

### 2단계. 메뉴 화면

- `print`로 메뉴를 출력하고 `input`으로 번호를 입력받았습니다.
- `while True` 반복문으로 종료를 선택할 때까지 메뉴가 계속 나오게 했고, 5번을 고르면 `break`로 빠져나옵니다.
- 입력값은 `.strip()`으로 공백을 지우고, `int()` 변환을 `try/except ValueError`로 감싸 문자 입력을 처리했습니다.
- 빈 입력과 범위 밖 숫자는 `continue`로 다시 입력받도록 했습니다.

### 3단계. Quiz 클래스

- 문제, 선택지, 정답을 하나로 묶는 `Quiz` 클래스를 만들었습니다.
- `__init__`에서 `self.question`, `self.choices`, `self.answer` 속성을 저장합니다.
- `display()`는 `enumerate`로 선택지에 1~4 번호를 붙여 출력하고, `check_answer()`는 정답 여부를 `True`/`False`로 반환합니다.

```python
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer
```

### 4단계. 기본 캠핑 퀴즈 데이터

- 캠핑 장비, 안전, 매너를 주제로 퀴즈 6개를 작성했습니다.
- `get_default_quizzes()` 함수가 `Quiz` 객체 6개가 담긴 리스트를 반환하도록 만들어, 나중에 파일이 없거나 손상됐을 때도 다시 불러올 수 있게 했습니다.

### 5단계. 퀴즈 풀기 (브랜치 작업)

- `feature/play-quiz` 브랜치를 만들어 작업한 뒤 `main` 브랜치에 병합했습니다.
- `for` 반복문으로 퀴즈를 하나씩 출제하고, 맞힌 개수를 세어 100점 만점 점수로 계산합니다.
- 오답일 때는 정답 번호와 정답 내용을 함께 보여줍니다.
- 메뉴와 정답 입력에서 같은 검사를 반복하지 않도록 입력 검사를 `get_number_input(prompt, min_value, max_value)` 함수로 분리했습니다.
- 사용 명령어: `git checkout -b`, `git checkout`, `git merge --no-ff`

### 6단계. 퀴즈 추가

- 문제와 선택지 4개를 `for` 반복문으로 입력받아 리스트에 `append`하고, 정답 번호는 `get_number_input()`으로 1~4 범위를 검사합니다.
- 빈 문자열 입력을 막기 위해 `get_text_input()` 함수를 추가했습니다.

### 7단계. 퀴즈 목록

- 등록된 퀴즈의 문제만 번호와 함께 출력하고, 퀴즈가 없을 때는 안내 메시지를 보여줍니다.

### 8단계. 점수 확인

- 최고 점수를 `None`으로 시작해 "아직 풀지 않음"과 "0점"을 구분했습니다.
- 퀴즈를 마칠 때마다 최고 점수와 비교해 더 높으면 갱신하고 "새로운 최고 점수입니다!"를 출력합니다.

### 9단계. QuizGame 클래스로 구조 정리 (리팩터링)

- 흩어져 있던 함수와 변수를 `QuizGame` 클래스로 묶었습니다.
  - 변수 `quizzes`, `best_score` → 속성 `self.quizzes`, `self.best_score`
  - 함수 `play_quiz(quizzes)` → 메서드 `self.play_quiz()`
- 메뉴의 입력 검사도 `get_number_input()`을 사용하도록 바꿔 중복 코드를 없앴습니다.
- 동작은 그대로 유지하고, 모든 메뉴를 다시 테스트해 확인했습니다.

### 10단계. state.json 저장과 불러오기

- `json` 모듈로 퀴즈 목록과 최고 점수를 `state.json`에 저장합니다.
- JSON은 객체를 직접 저장할 수 없으므로, 저장할 때는 `to_dict()`로 Quiz 객체를 dict로 바꾸고 불러올 때는 dict를 다시 Quiz 객체로 만듭니다.
- 파일이 없으면(`FileNotFoundError`) 기본 퀴즈로 시작하고, 파일이 손상되면(`json.JSONDecodeError`, `KeyError`, `TypeError`) 기본 퀴즈로 복구합니다.
- `state.json`은 실행할 때마다 바뀌는 파일이라 `.gitignore`에 추가했습니다.

```python
def save_data(self):
    quiz_list = []
    for quiz in self.quizzes:
        quiz_list.append(quiz.to_dict())

    data = {"quizzes": quiz_list, "best_score": self.best_score}

    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except OSError:
        print("데이터를 파일에 저장하지 못했습니다.")
```

### 11단계. 안전한 종료 처리

- 실행 중 `Ctrl + C`(KeyboardInterrupt)나 입력 종료(EOFError)가 발생해도 오류 화면 없이 끝나도록 `game.run()`을 `try/except`로 감쌌습니다.
- 종료 전에 `save_data()`를 호출해 그때까지의 데이터를 저장합니다.

```python
game = QuizGame()
try:
    game.run()
except (KeyboardInterrupt, EOFError):
    print("프로그램이 중단되었습니다. 데이터를 저장하고 안전하게 종료합니다.")
    game.save_data()
```

### 12단계. README 작성과 clone / pull 실습

- 실행 화면 스크린샷을 `docs/screenshots`에 모으고 README를 작성했습니다.
- 저장소를 다른 폴더(`quiz-game-clone`)로 `clone`해 README를 수정하고 push한 뒤, 원래 작업 폴더에서 `pull`로 변경 사항을 받아왔습니다.
- 사용 명령어: `git clone`, `git pull`

---

## 6. 파일 구조

```
quiz-game/
├── main.py              프로그램 전체 코드 (Quiz, QuizGame 클래스)
├── state.json           퀴즈와 최고 점수 저장 파일 (실행 시 자동 생성, Git 제외)
├── .gitignore           Git에서 제외할 파일 목록
├── README.md            프로젝트 설명서
└── docs/
    └── screenshots/     실행 화면 스크린샷
        ├── env.png          개발 환경
        ├── menu.png         메뉴 및 잘못된 입력 처리
        ├── play1.png        퀴즈 풀기 (1)
        ├── play2.png        퀴즈 풀기 (2)
        ├── play3.png        퀴즈 풀기 (3)
        ├── add_quiz1.png    퀴즈 추가 (1)
        ├── add_quiz2.png    퀴즈 추가 (2)
        ├── list.png         퀴즈 목록
        ├── score.png        점수 확인
        ├── data_keep.png    재실행 후 데이터 유지
        └── git_log.png      커밋 기록 그래프
```

---

## 7. 데이터 파일 설명 (state.json)

| 항목 | 내용 |
|:---|:---|
| 경로 | 프로젝트 루트 (`quiz-game/state.json`) |
| 인코딩 | UTF-8 (`ensure_ascii=False`로 한글을 그대로 저장) |
| 역할 | 퀴즈 목록과 최고 점수를 저장하여 프로그램을 다시 실행해도 데이터 유지 |
| 저장 시점 | 퀴즈 추가 시, 최고 점수 갱신 시, 정상 종료 시, `Ctrl + C` 종료 시 |
| 불러오기 시점 | 프로그램 시작 시 |
| Git 관리 | 실행할 때마다 내용이 바뀌는 파일이므로 `.gitignore`로 제외 |

### 스키마

| 키 | 자료형 | 설명 |
|:---|:---|:---|
| `quizzes` | list | 퀴즈 목록 |
| `quizzes[].question` | str | 문제 |
| `quizzes[].choices` | list (str 4개) | 선택지 |
| `quizzes[].answer` | int (1~4) | 정답 번호 |
| `best_score` | int 또는 null | 최고 점수 (100점 만점). 아직 기록이 없으면 `null` |

### 예시

```json
{
    "quizzes": [
        {
            "question": "텐트를 땅에 단단히 고정할 때 박는 말뚝은?",
            "choices": ["코펠", "펙", "랜턴", "릴선"],
            "answer": 2
        }
    ],
    "best_score": 100
}
```

---

## 8. 실행 화면

### 개발 환경

<img src="docs/screenshots/env.png" width="700">

### 메뉴 및 잘못된 입력 처리

<img src="docs/screenshots/menu.png" width="700">

### 퀴즈 풀기

<img src="docs/screenshots/play1.png" width="700">
<img src="docs/screenshots/play2.png" width="700">
<img src="docs/screenshots/play3.png" width="700">

### 퀴즈 추가

<img src="docs/screenshots/add_quiz1.png" width="700">
<img src="docs/screenshots/add_quiz2.png" width="700">

### 퀴즈 목록

<img src="docs/screenshots/list.png" width="700">

### 점수 확인

<img src="docs/screenshots/score.png" width="700">

### 재실행 후 데이터 유지

<img src="docs/screenshots/data_keep.png" width="700">

---

## 9. Git 작업 기록

### 커밋 메시지 규칙

| 머리말 | 의미 |
|:---|:---|
| `Feat:` | 새 기능 추가 |
| `Fix:` | 오류 수정 |
| `Refactor:` | 동작 변경 없이 코드 구조 정리 |
| `Docs:` | 문서, 스크린샷 |
| `Chore:` | 설정 |

### 사용한 Git 명령어

| 명령어 | 사용 내용 |
|:---|:---|
| `init`, `add`, `commit`, `push` | 저장소 생성 및 기능 단위 커밋 |
| `checkout`, `merge` | `feature/play-quiz` 브랜치 생성 후 `main`에 병합 (`--no-ff`) |
| `clone`, `pull` | 복제 저장소에서 README 수정 후 push, 원래 작업 폴더에서 pull로 반영 |

### 커밋 기록 (git log --oneline --graph)

`feature/play-quiz` 브랜치에서 퀴즈 풀기 기능을 만들고 `main`에 병합한 기록을 그래프로 확인할 수 있습니다.

<img src="docs/screenshots/git_log.png" width="700">

### clone / pull 실습 기록

아래 문장은 복제한 저장소(quiz-game-clone)에서 추가한 뒤, 원래 작업 폴더에서 `git pull`로 받아온 내용입니다.

> 이 줄은 clone/pull 실습을 위해 복제한 저장소(quiz-game-clone)에서 추가했습니다.