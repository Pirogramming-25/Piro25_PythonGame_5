# -*- coding: utf-8 -*-

import random


ROUND_COUNT = 3

QUESTIONS = [
    {
        "question": "술자리에서 더 난감한 상황은?",
        "A": "건배사 시켰는데 머리가 새하얘짐",
        "B": "친구 이름을 순간적으로 까먹음",
    },
    {
        "question": "더 버티기 힘든 것은?",
        "A": "안주 없이 술 마시기",
        "B": "물 없이 매운 음식 먹기",
    },
    {
        "question": "더 피하고 싶은 벌칙은?",
        "A": "흑역사 사진 공개",
        "B": "즉석 애교 10초 하기",
    },
    {
        "question": "술자리에서 더 위험한 사람은?",
        "A": "계속 짠 하자고 하는 사람",
        "B": "갑자기 진지한 얘기 꺼내는 사람",
    },
    {
        "question": "둘 중 하나만 고른다면?",
        "A": "평생 소주만 마시기",
        "B": "평생 맥주만 마시기",
    },
    {
        "question": "더 당황스러운 상황은?",
        "A": "내가 보낸 카톡을 모두가 보고 있음",
        "B": "내 플레이리스트가 갑자기 공개됨",
    },
    {
        "question": "술자리 마지막 안주로 더 좋은 것은?",
        "A": "뜨끈한 라면",
        "B": "바삭한 치킨",
    },
    {
        "question": "더 곤란한 선택은?",
        "A": "내가 계산하기",
        "B": "내가 다음 장소 정하기",
    },
    {
        "question": "당신이 해보고 싶은것은?",
        "A": "밤새 술자리 끝까지 남기",
        "B": "술자리 단체 사진 센터 차지하기",
    },
    {
        "question": "더 피하고 싶은 친구 유형은?",
        "A": "내 잔이 비면 바로 채워주는 친구",
        "B": "내 흑역사를 계속 꺼내는 친구",
    },
    {
        "question": "술자리 게임에서 더 무서운 사람은?",
        "A": "규칙을 너무 잘 아는 사람",
        "B": "규칙을 몰라도 계속 이기는 사람",
    },
    {
        "question": "더 창피한 순간은?",
        "A": "노래방 첫 소절부터 음이탈",
        "B": "조용한 순간에 배에서 소리남",
    },
    {
        "question": "더 힘든 귀가길은?",
        "A": "막차 놓쳐서 택시비 폭탄",
        "B": "집 앞까지 왔는데 엘레베이터 고장",
    },
    {
        "question": "더 어려운 선택은?",
        "A": "친구 대신 애교 부려주기",
        "B": "친구 대신 벌칙 춤 춰주기",
    },
    {
        "question": "더 아찔한 상황은?",
        "A": "술자리에서 전 애인 마주치기",
        "B": "술자리에서 교수님 마주치기",
    },
    {
        "question": "더 참기 어려운 것은?",
        "A": "내가 좋아하는 안주 마지막 한 입 양보하기",
        "B": "내가 고른 노래 후렴 전에 끊기",
    },
    {
        "question": "더 싫은 벌칙은?",
        "A": "랜덤 연락처에 안부 문자 보내기",
        "B": "모르는 사람 앞에서 30초 자기소개 하기",
    },
    {
        "question": "술자리에서 더 필요한 능력은?",
        "A": "절대 안 취하는 간",
        "B": "무슨 말을 해도 웃기는 입담",
    },
]


def print_wave():
    print("~" * 62)


def choose_user_answer():
    while True:
        answer = input("당신의 선택은? (A/B): ").strip().upper()

        if answer in ["A", "B"]:
            return answer

        print("잘못된 입력입니다. A 또는 B만 입력해주세요.")


def choose_computer_answer():
    return random.choice(["A", "B"])


def group_players_by_answer(answers):
    group_a = []
    group_b = []

    for player_name, answer in answers.items():
        if answer == "A":
            group_a.append(player_name)
        else:
            group_b.append(player_name)

    return group_a, group_b


def create_score_board(players):
    scores = {}
    streaks = {}

    for player in players:
        scores[player["name"]] = 0
        streaks[player["name"]] = 0

    return scores, streaks


def show_rule():
    print_wave()
    print("🍺 소수파 술자리 밸런스 점수 게임 🍺")
    print_wave()
    print("총 3개의 밸런스 질문에 답합니다.")
    print("다수파는 +1점, 소수파는 -1점입니다.")
    print("연속으로 소수파가 되면 추가 -1점입니다.")
    print("동률이면 모두 0점입니다.")
    print("마지막에 점수가 가장 낮은 사람이 벌칙주 1잔을 마십니다.")
    print_wave()


def show_question(round_number, question):
    print(f"\n[{round_number}라운드]")
    print_wave()
    print(f"Q. {question['question']}")
    print(f"A. {question['A']}")
    print(f"B. {question['B']}")
    print_wave()


def collect_answers(players):
    answers = {}

    for player in players:
        if player["is_user"]:
            answers[player["name"]] = choose_user_answer()
        else:
            answers[player["name"]] = choose_computer_answer()

    return answers


def show_answers(players, answers):
    print("\n모두 선택을 완료했습니다!")

    for player in players:
        name = player["name"]
        print(f"{name}: {answers[name]}")


def show_vote_result(group_a, group_b):
    print("\n투표 결과")
    print_wave()
    print(f"A 선택: {', '.join(group_a) if group_a else '없음'}")
    print(f"B 선택: {', '.join(group_b) if group_b else '없음'}")
    print_wave()


def add_majority_score(scores, streaks, majority_names):
    for name in majority_names:
        scores[name] += 1
        streaks[name] = 0
        print(f"{name}: 다수파 +1점")


def add_minority_score(scores, streaks, minority_names):
    for name in minority_names:
        streaks[name] += 1
        total_score = -1

        if streaks[name] >= 2:
            total_score -= 1
            print(f"{name}: 연속 소수파 추가 -1점")

        scores[name] += total_score
        print(f"{name}: 소수파 {total_score}점")


def apply_round_score(scores, streaks, group_a, group_b):
    if len(group_a) == len(group_b):
        print("A와 B가 동률입니다. 이번 라운드는 모두 0점입니다.")
        for name in scores:
            streaks[name] = 0
        return

    if len(group_a) < len(group_b):
        print(f"A가 소수파입니다. ({len(group_a)}명)")
        add_minority_score(scores, streaks, group_a)
        add_majority_score(scores, streaks, group_b)
    else:
        print(f"B가 소수파입니다. ({len(group_b)}명)")
        add_minority_score(scores, streaks, group_b)
        add_majority_score(scores, streaks, group_a)


def show_score_board(scores):
    print("\n현재 점수판")
    print_wave()

    for name, score in scores.items():
        print(f"{name}: {score}점")

    print_wave()


def find_lowest_score_names(scores):
    lowest_score = min(scores.values())
    lowest_names = []

    for name, score in scores.items():
        if score == lowest_score:
            lowest_names.append(name)

    return lowest_score, lowest_names


def apply_final_penalty(players, loser_names):
    print("\n최종 벌칙")
    print_wave()
    print(f"최저 점수자: {', '.join(loser_names)}")
    print("최저 점수자는 벌칙주 1잔을 마십니다!")

    for player in players:
        if player["name"] in loser_names:
            player["drink"] += 1
            print(f"{player['name']}님 현재 마신 잔 수: {player['drink']}잔")

    print_wave()


def play_game(players):
    scores, streaks = create_score_board(players)
    selected_questions = random.sample(QUESTIONS, ROUND_COUNT)

    show_rule()

    for round_number, question in enumerate(selected_questions, start=1):
        show_question(round_number, question)
        answers = collect_answers(players)
        show_answers(players, answers)

        group_a, group_b = group_players_by_answer(answers)
        show_vote_result(group_a, group_b)
        apply_round_score(scores, streaks, group_a, group_b)
        show_score_board(scores)

    lowest_score, loser_names = find_lowest_score_names(scores)
    print(f"\n최종 최저 점수는 {lowest_score}점입니다.")
    apply_final_penalty(players, loser_names)
    print("소수파 술자리 밸런스 점수 게임이 종료되었습니다.")

    return players
