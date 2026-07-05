# -*- coding: utf-8 -*-

import random

from games import jisoo_game, yeonwoo_game, yewon_game


DRINK_LIMITS = {
    "1": ("소주 한 병 반병", 2),
    "2": ("소주 한 병", 4),
    "3": ("소주 한 병 반", 6),
    "4": ("소주 두 병", 8),
    "5": ("소주 두 병 이상", 10),
}

COMPUTER_CANDIDATES = [
    "은서",
    "하연",
    "연서",
    "예진",
    "헌도",
    "민수",
    "지은",
    "서준",
]

GAME_LIST = [
    ("지수의 게임", jisoo_game.play_game),
    ("연우의 소수파 술자리 밸런스 게임", yeonwoo_game.play_game),
    ("예원의 게임", yewon_game.play_game),
]


def print_wave():
    print("~" * 62)


def print_title(title):
    print_wave()
    print(f"🍺 {title} 🍺".center(54))
    print_wave()


def pause():
    input("\n엔터를 누르면 계속합니다...")


def show_intro():
    print_title("오늘의 ALCOHOL GAME")
    print("혼자 하는 Python 술게임에 오신 것을 환영합니다!")
    print("친구들을 초대하고, 미니게임을 진행하며 살아남아 보세요.")
    print("누군가 치사량에 도달하면 게임이 종료됩니다.")
    pause()


def choose_drink_limit():
    while True:
        print_title("소주 기준 당신의 주량은?")
        for number, drink_info in DRINK_LIMITS.items():
            level, limit = drink_info
            print(f"🍺 {number}. {level} ({limit}잔)")

        choice = input("당신의 치사량(주량)은 얼마만큼인가요? (1~5): ")

        if choice in DRINK_LIMITS:
            level, limit = DRINK_LIMITS[choice]
            print(f"\n선택 완료! 당신의 주량은 '{level}', 치사량은 {limit}잔입니다.")
            return limit

        print("\n잘못된 입력입니다. 1~5 사이의 숫자를 입력해주세요.")


def choose_computer_count():
    while True:
        print_title("같이 취할 친구 초대하기")
        count = input("함께 취할 친구들은 얼마나 필요한가요? (1~3명): ")

        if count.isdigit():
            count = int(count)
            if 1 <= count <= 3:
                return count

        print("\n최대 3명까지 초대할 수 있습니다. 1~3 사이로 입력해주세요.")


def create_players():
    print_title("입장하기")
    user_name = input("당신의 이름을 입력하세요: ").strip()

    while user_name == "":
        user_name = input("이름은 비워둘 수 없습니다. 다시 입력하세요: ").strip()

    user_limit = choose_drink_limit()
    players = [
        {
            "name": user_name,
            "drink": 0,
            "limit": user_limit,
            "is_user": True,
            "minority_streak": 0,
        }
    ]

    computer_count = choose_computer_count()
    computer_names = random.sample(COMPUTER_CANDIDATES, computer_count)

    print("\n오늘 함께 취할 친구들이 입장합니다!")
    for name in computer_names:
        level, limit = random.choice(list(DRINK_LIMITS.values()))
        players.append(
            {
                "name": name,
                "drink": 0,
                "limit": limit,
                "is_user": False,
                "minority_streak": 0,
            }
        )
        print(f"오늘 함께 취할 친구는 {name}입니다! (주량: {level}, 치사량: {limit}잔)")

    pause()
    return players


def show_status(players):
    print_title("현재 술자리 상황")
    for player in players:
        remaining = player["limit"] - player["drink"]
        if remaining < 0:
            remaining = 0

        print(
            f"{player['name']}은(는) 지금까지 🍺 {player['drink']}잔 | "
            f"치사량까지 {remaining}잔"
        )


def choose_game_by_user():
    while True:
        print_title("오늘의 Alcohol GAME")
        for index, game in enumerate(GAME_LIST, start=1):
            print(f"🍺 {index}. {game[0]}")
        print("🍺 exit. 게임 그만하기")

        choice = input("어떤 게임을 진행할까요? 번호를 선택해주세요: ").strip()

        if choice.lower() == "exit":
            return None

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(GAME_LIST):
                return GAME_LIST[choice - 1]

        print("\n잘못된 입력입니다. 게임 번호를 다시 선택해주세요.")


def choose_game_by_computer(player):
    game_name, game_function = random.choice(GAME_LIST)
    print_title("컴퓨터 플레이어의 턴")
    print(f"{player['name']}님이 게임을 고르는 중입니다...")
    print(f"{player['name']}님이 [{game_name}]을 선택했습니다!")
    pause()
    return game_name, game_function


def choose_game_by_turn(player):
    if player["is_user"]:
        return choose_game_by_user()

    return choose_game_by_computer(player)


def find_finished_players(players):
    finished_players = []

    for player in players:
        if player["drink"] >= player["limit"]:
            finished_players.append(player)

    return finished_players


def get_most_drunk_players(players):
    most_drinks = 0
    most_drunk_players = []

    for player in players:
        if player["drink"] > most_drinks:
            most_drinks = player["drink"]
            most_drunk_players = [player]
        elif player["drink"] == most_drinks:
            most_drunk_players.append(player)

    return most_drunk_players


def show_outro_message(players, finished_players):
    most_drunk_players = get_most_drunk_players(players)
    most_drunk_names = ", ".join(player["name"] for player in most_drunk_players)
    survivors = []

    for player in players:
        if player["drink"] < player["limit"]:
            survivors.append(player["name"])

    print("\n오늘의 술자리 리포트")
    print_wave()
    print(f"🍺 가장 많이 마신 사람: {most_drunk_names}")

    if survivors:
        print(f"🍺 끝까지 살아남은 사람: {', '.join(survivors)}")
    else:
        print("🍺 오늘은 아무도 멀쩡히 살아남지 못했습니다.")

    if finished_players:
        for player in finished_players:
            over_drink = player["drink"] - player["limit"]
            if over_drink < 0:
                over_drink = 0
            print(f"🍺 {player['name']}님은 치사량보다 {over_drink}잔 더 마셨습니다.")
    else:
        print("🍺 치사량에 도달한 사람 없이 평화롭게 마무리되었습니다.")

    print_wave()
    print("오늘의 술자리는 여기까지!")
    print("다음 술자리에서는 더 강한 간으로 돌아오세요.")
    print("٩(^ᴗ^)۶ 수고하셨습니다 ٩(^ᴗ^)۶")


def show_final_result(players, finished_players):
    print_title("게임 종료")

    if finished_players:
        for player in finished_players:
            print(f"{player['name']}님이 치사량에 도달했습니다!")
    else:
        print("사용자가 게임을 종료했습니다.")

    print("\n지금까지의 play 상황")
    print_wave()
    for player in players:
        print(f"{player['name']}: {player['drink']}잔 / 치사량 {player['limit']}잔")

    show_outro_message(players, finished_players)


def move_next_turn(turn_index, players):
    return (turn_index + 1) % len(players)


def main():
    show_intro()
    players = create_players()
    turn_index = 0

    while True:
        show_status(players)
        current_player = players[turn_index]

        print_title(f"{current_player['name']}님의 차례")
        selected_game = choose_game_by_turn(current_player)

        if selected_game is None:
            show_final_result(players, [])
            break

        game_name, game_function = selected_game
        print(f"\n🍺 [{game_name}]을 시작합니다!")
        print_wave()
        players = game_function(players)

        show_status(players)
        finished_players = find_finished_players(players)
        if finished_players:
            show_final_result(players, finished_players)
            break

        turn_index = move_next_turn(turn_index, players)
        pause()


if __name__ == "__main__":
    main()
