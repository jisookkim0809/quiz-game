# ⛺ 나만의 캠핑 퀴즈 게임

Python으로 만든 **터미널(콘솔) 캠핑 퀴즈 게임**입니다.
메뉴에서 번호를 골라 퀴즈를 풀고, 새 퀴즈를 추가하고, 목록과 최고 점수를 확인할 수 있습니다.
추가한 퀴즈와 최고 점수는 `state.json` 파일에 저장되어 **프로그램을 껐다 켜도 그대로 유지**됩니다.

---

## 1. 프로젝트 개요

| 항목 | 내용 |
|---|---|
| 프로젝트명 | 나만의 캠핑 퀴즈 게임 (quiz-game) |
| 언어 | Python 3.10 이상 (개발 환경: Python 3.15.2) |
| 외부 라이브러리 | 없음 (표준 라이브러리 `json`만 사용) |
| 실행 환경 | 터미널 (Windows PowerShell에서 개발·테스트) |
| 주요 학습 내용 | 변수·자료형, 조건문·반복문, 함수, 클래스(객체 지향), JSON 파일 입출력, 예외 처리, Git/GitHub |

### 클래스 구성

| 클래스 | 역할 | 주요 속성 | 주요 메서드 |
|---|---|---|---|
| `Quiz` | 퀴즈 문제 **1개**를 표현 | `question`, `choices`, `answer` | `display()`, `check_answer()`, `to_dict()` |
| `QuizGame` | 게임 **전체**를 관리 | `quizzes`, `best_score` | `run()`, `show_menu()`, `play_quiz()`, `add_quiz()`, `show_quiz_list()`, `show_score()`, `load_data()`, `save_data()`, `get_number_input()`, `get_text_input()` |

---

## 2. 퀴즈 주제와 선정 이유

**주제: 캠핑** 🏕️

캠핑은 제가 가장 좋아하는 취미입니다. 캠핑을 다니면서 타프, 그라운드시트, 펙, 코펠처럼 처음엔 낯설었던 장비 이름과, 텐트 안 일산화탄소 위험·매너 타임 같은 **꼭 알아야 할 안전 수칙과 매너**를 하나씩 배웠습니다.

좋아하는 주제라서 문제를 즐겁게 만들 수 있었고, 캠핑을 처음 시작하는 사람에게 **실제로 도움이 되는 퀴즈**를 만들고 싶어서 이 주제를 선택했습니다.

---

## 3. 실행 방법

### 준비물
- Python 3.10 이상
- Git

### 실행 순서

```bash
# 1) 저장소 복제
git clone https://github.com/jisookkim0809/quiz-game.git

# 2) 폴더로 이동
cd quiz-game

# 3) 실행
python main.py
```

> 처음 실행하면 `state.json`이 없으므로 기본 캠핑 퀴즈 6개로 시작하며, 이때 `state.json`이 자동으로 만들어집니다.

---

## 4. 기능 목록

### 기본 기능

| 메뉴 | 기능 | 설명 |
|---|---|---|
| 1 | 퀴즈 풀기 | 등록된 퀴즈를 순서대로 출제하고, 정답/오답과 정답 번호를 알려 줍니다. 끝나면 점수(100점 만점)를 보여 주고 최고 점수를 갱신합니다. |
| 2 | 퀴즈 추가 | 문제, 선택지 4개, 정답 번호(1~4)를 입력받아 새 퀴즈를 등록하고 파일에 저장합니다. |
| 3 | 퀴즈 목록 | 등록된 모든 퀴즈의 문제를 번호와 함께 보여 줍니다. |
| 4 | 점수 확인 | 지금까지의 최고 점수를 보여 줍니다. |
| 5 | 종료 | 데이터를 저장하고 프로그램을 종료합니다. |

### 입력·예외 처리

| 상황 | 처리 |
|---|---|
| 입력 앞뒤 공백 (예: ` 1 `) | 공백을 제거하고 처리 |
| 빈 입력 (그냥 Enter) | 안내 메시지 후 다시 입력 |
| 숫자가 아닌 입력 (예: `abc`) | 안내 메시지 후 다시 입력 |
| 범위 밖 숫자 (예: 메뉴 `9`, 정답 `0`) | 안내 메시지 후 다시 입력 |
| 퀴즈가 0개일 때 풀기/목록 | 안내 메시지 출력 |
| 아직 퀴즈를 풀지 않았을 때 점수 확인 | 안내 메시지 출력 |
| `Ctrl + C` / 입력 종료(`Ctrl + Z`, EOF) | 안내 메시지 → 데이터 저장 → 안전하게 종료 |
| `state.json`이 없음 (첫 실행) | 기본 퀴즈로 시작하고 파일 생성 |
| `state.json`이 손상됨 | 안내 메시지 → 기본 퀴즈로 복구 |

---

## 5. 파일 구조

```
quiz-game/
├── main.py              # 프로그램 전체 코드 (Quiz, QuizGame 클래스)
├── state.json           # 퀴즈·최고 점수 저장 파일 (실행 시 자동 생성, Git 제외)
├── .gitignore           # Git에 올리지 않을 파일 목록
├── README.md            # 프로젝트 설명서
└── docs/
└── screenshots/     # 실행 화면 스크린샷
        ├── env.png
        ├── menu.png
        ├── play1.png
        ├── play2.png
        ├── play3.png
        ├── add_quiz1.png
        ├── add_quiz2.png
        ├── list.png
        ├── score.png
        └── data_keep.png
---

## 6. 데이터 파일 설명 (`state.json`)

| 항목 | 내용 |
|---|---|
| 경로 | 프로젝트 루트 (`quiz-game/state.json`) |
| 인코딩 | UTF-8 (한글이 그대로 저장되도록 `ensure_ascii=False` 사용) |
| 역할 | 퀴즈 목록과 최고 점수를 저장해 프로그램을 다시 실행해도 데이터를 유지 |
| 저장 시점 | 퀴즈 추가 시, 최고 점수 갱신 시, 정상 종료 시, `Ctrl + C` 종료 시 |
| 불러오기 시점 | 프로그램 시작 시 |
| Git 관리 | 실행할 때마다 바뀌는 데이터라서 `.gitignore`로 제외 |

### 스키마 (데이터 구조)

| 키 | 자료형 | 설명 |
|---|---|---|
| `quizzes` | list | 퀴즈 목록 |
| `quizzes[].question` | str | 문제 |
| `quizzes[].choices` | list (str 4개) | 선택지 4개 |
| `quizzes[].answer` | int (1~4) | 정답 번호 |
| `best_score` | int 또는 null | 최고 점수 (100점 만점), 아직 풀지 않았으면 `null` |

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

## 7. 실행 화면

### 메뉴 + 잘못된 입력 처리
![메뉴](docs/screenshots/menu.png)

### 퀴즈 풀기
![퀴즈 풀기 1](docs/screenshots/play1.png)
![퀴즈 풀기 2](docs/screenshots/play2.png)
![퀴즈 풀기 3](docs/screenshots/play3.png)

### 퀴즈 추가
![퀴즈 추가 1](docs/screenshots/add_quiz1.png)
![퀴즈 추가 2](docs/screenshots/add_quiz2.png)

### 퀴즈 목록
![퀴즈 목록](docs/screenshots/list.png)

### 점수 확인
![점수 확인](docs/screenshots/score.png)

### 재실행 후 데이터 유지
![데이터 유지](docs/screenshots/data_keep.png)

---

## 8. Git 작업 방식

- **기능 단위 커밋**: 메뉴 → Quiz 클래스 → 기본 데이터 → 퀴즈 풀기 → 추가 → 목록 → 점수 → 구조 정리 → 파일 저장 → 안전 종료 → README 순서로 커밋했습니다.
- **커밋 메시지 규칙**

| 머리말 | 의미 |
|---|---|
| `Feat:` | 새 기능 |
| `Fix:` | 오류 수정 |
| `Refactor:` | 동작은 그대로, 코드 구조 정리 |
| `Docs:` | 문서·자료 |
| `Chore:` | 설정 |

- **브랜치**: `feature/play-quiz` 브랜치에서 퀴즈 풀기 기능을 개발한 뒤 `main`에 병합(`merge --no-ff`)했습니다.
- **사용한 Git 명령어**: `init`, `add`, `commit`, `push`, `checkout`, `clone`, `pull`