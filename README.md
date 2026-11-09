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
5. [파일 구조](#5-파일-구조)
6. [데이터 파일 설명 (state.json)](#6-데이터-파일-설명-statejson)
7. [실행 화면](#7-실행-화면)
8. [Git 작업 기록](#8-git-작업-기록)
9. [요구사항 충족 확인 (평가자용)](#9-요구사항-충족-확인-평가자용)

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

## 5. 파일 구조

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

## 6. 데이터 파일 설명 (state.json)

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

## 7. 실행 화면

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

## 8. Git 작업 기록

### 작업 순서

| 순서 | 작업 | 커밋 |
|:---:|:---|:---|
| 1 | 프로젝트 초기 설정 | `Chore` |
| 2 | 메뉴 기능 | `Feat` |
| 3 | Quiz 클래스 | `Feat` |
| 4 | 기본 퀴즈 데이터 | `Feat` |
| 5 | 퀴즈 풀기 (`feature/play-quiz` 브랜치에서 개발 후 `main`에 병합) | `Feat`, `Merge` |
| 6 | 퀴즈 추가 | `Feat` |
| 7 | 퀴즈 목록 | `Feat` |
| 8 | 점수 확인 | `Feat` |
| 9 | QuizGame 클래스로 구조 정리 | `Refactor` |
| 10 | state.json 저장/불러오기 | `Feat` |
| 11 | Ctrl+C / EOF 안전 종료 | `Fix` |
| 12 | README 작성 및 스크린샷 | `Docs` |
| 13 | clone / pull 실습 | `Docs` |

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

<img src="docs/screenshots/git_log.png" width="700">

### clone / pull 실습 기록

아래 문장은 clone/pull 실습을 위해 복제한 저장소(quiz-game-clone)에서 추가한 뒤, 원래 작업 폴더에서 `git pull`로 받아온 내용입니다.

> 이 줄은 clone/pull 실습을 위해 복제한 저장소(quiz-game-clone)에서 추가했습니다.

---

## 9. 요구사항 충족 확인 (평가자용)

### 요구사항별 구현 위치

| 요구사항 | 구현 위치 | 확인 방법 |
|:---|:---|:---|
| 메뉴 출력 및 선택 | `QuizGame.run()`, `show_menu()` | 실행 직후 메뉴 화면 |
| 잘못된 입력 처리 (공백, 빈 입력, 문자, 범위) | `QuizGame.get_number_input()` | 메뉴에서 Enter, `abc`, `9` 입력 |
| 퀴즈 풀기 / 결과 표시 | `QuizGame.play_quiz()` | 메뉴 1 |
| 퀴즈 추가 | `QuizGame.add_quiz()` | 메뉴 2 |
| 퀴즈 목록 | `QuizGame.show_quiz_list()` | 메뉴 3 |
| 최고 점수 확인 및 갱신 | `QuizGame.show_score()`, `play_quiz()` | 메뉴 4 |
| 주제 퀴즈 5개 이상 | `get_default_quizzes()` (6개) | 메뉴 3 |
| 클래스 2개 이상 | `Quiz`, `QuizGame` | `main.py` |
| state.json 저장/불러오기 | `QuizGame.save_data()`, `load_data()` | 아래 테스트 1 |
| 파일 없음 / 손상 처리 | `QuizGame.load_data()` | 아래 테스트 2, 3 |
| Ctrl+C / EOF 안전 종료 | `main.py` 마지막 `try/except` | 아래 테스트 4 |
| 커밋 10개 이상 | 커밋 19개 | `git log --oneline` |
| 브랜치 생성 및 병합 | `feature/play-quiz` → `main` | `git log --oneline --graph` |
| Git 명령어 7종 | init, add, commit, push, checkout, clone, pull | 8장 참고 |

### 직접 확인해 볼 수 있는 테스트

| 번호 | 테스트 | 방법 | 예상 결과 |
|:---:|:---|:---|:---|
| 1 | 데이터 유지 | 메뉴 2로 퀴즈 추가, 메뉴 1로 퀴즈 풀기 → 메뉴 5로 종료 → 다시 실행 | 시작 시 "저장된 데이터를 불러왔습니다 (퀴즈 7개, 최고점수 N점)" 출력, 메뉴 3·4에서 확인 |
| 2 | 파일 없음 | `state.json` 삭제 후 실행 | "저장된 데이터가 없어 기본 퀴즈로 시작합니다" 출력, 파일 새로 생성 |
| 3 | 파일 손상 | `state.json`의 첫 글자 `{` 삭제 후 실행 | "저장 파일이 손상되어 기본 퀴즈로 복구합니다" 출력 |
| 4 | 안전 종료 | 실행 중 `Ctrl + C` 입력 | 오류 메시지 없이 안내 문구 출력 후 저장하고 종료 |