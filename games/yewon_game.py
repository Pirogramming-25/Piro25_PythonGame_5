import random


def show_players(players):
    print("\n현재 참가자 상태")
    print("-" * 35)

    for player in players:
        name = player["name"]
        drink = player["drink"]
        limit = player["limit"]
        left = limit - drink

        print(f"{name} : 현재 {drink}잔 / 치사량 {limit}잔 / 남은 잔 {left}잔")


def get_user_count(current_number):
    while True:
        count = input("몇 개의 숫자를 말할까요? (1~3) : ")

        if count.isdigit():
            count = int(count)

            if 1 <= count <= 3:
                return count

        print("잘못 입력했습니다. 1, 2, 3 중 하나만 입력해주세요.")


def play_game(players):
    print("\n" + "=" * 40)
    print("🍦 취중 베스킨라빈스 31 게임 시작!")
    print("=" * 40)
    print("자기 차례마다 숫자를 1개, 2개, 3개까지 말할 수 있습니다.")
    print("31을 말하는 사람이 벌주를 마십니다.")
    print("=" * 40)

    current_number = 0
    turn = 0

    while current_number < 31:
        player = players[turn % len(players)]

        print(f"\n{player['name']}님의 차례입니다.")
        print(f"현재 숫자 : {current_number}")

        if turn % len(players) == 0:
            count = get_user_count(current_number)
        else:
            count = random.randint(1, 3)
            print(f"{player['name']}님은 {count}개의 숫자를 말합니다.")

        spoken_numbers = []

        for i in range(count):
            current_number += 1
            spoken_numbers.append(current_number)

            if current_number == 31:
                break

        print(f"{player['name']} : ", end="")
        for number in spoken_numbers:
            print(number, end=" ")
        print()

        if current_number >= 31:
            print("\n" + "!" * 40)
            print(f"31을 말한 사람은 {player['name']}님입니다!")
            print(f"{player['name']}님 벌주 한 잔!")
            print("!" * 40)

            player["drink"] += 1

            show_players(players)

            return players

        turn += 1