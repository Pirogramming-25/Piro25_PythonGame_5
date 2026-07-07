import random

def print_wave():
    print("~" * 62)

def print_title(title):
    print_wave()
    print(f"💀 {title} 💀".center(54))
    print_wave()


def get_player_names(players):
    names = []

    for player in players:
        names.append(player["name"])

    return names


def choose_target_by_user(player_name, player_names):
    selectable_names = []

    for name in player_names:
        if name != player_name:
            selectable_names.append(name)

    while True:
        print(f"\n{player_name}님, 누구를 지목할까요?")

        for index, name in enumerate(selectable_names, start=1):
            print(f"{index}. {name}")

        choice = input("지목할 사람 번호를 입력하세요: ").strip()

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(selectable_names):
                return selectable_names[choice - 1]

        print("잘못된 입력입니다. 번호를 다시 입력해주세요.")


def choose_target_by_computer(player_name, player_names):
    selectable_names = []

    for name in player_names:
        if name != player_name:
            selectable_names.append(name)

    target = random.choice(selectable_names)
    print(f"{player_name}님이 누군가를 조용히 지목했습니다...")
    return target


def create_pointing_map(players):
    player_names = get_player_names(players)
    pointing_map = {}

    print_title("지목 시간")
    print("각자 한 명씩 지목합니다.")
    print("컴퓨터 친구들은 랜덤으로 지목합니다.")

    for player in players:
        player_name = player["name"]

        if player["is_user"]:
            target = choose_target_by_user(player_name, player_names)
        else:
            target = choose_target_by_computer(player_name, player_names)

        pointing_map[player_name] = target

    return pointing_map


def show_pointing_result(pointing_map):
    print_title("지목 결과")

    for player_name, target_name in pointing_map.items():
        print(f"{player_name} → {target_name}")


def choose_start_player(player_names):
    while True:
        print_title("시작 사람 고르기")
        print("누구부터 숫자를 셀까요?")

        for index, name in enumerate(player_names, start=1):
            print(f"{index}. {name}")

        choice = input("시작할 사람 번호를 입력하세요: ").strip()

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(player_names):
                return player_names[choice - 1]

        print("잘못된 입력입니다. 번호를 다시 입력해주세요.")


def is_user_player(player_name, players):
    for player in players:
        if player["name"] == player_name:
            return player["is_user"]

    return False


def choose_count_number_by_user():
    while True:
        count = input("\n당신이 술래입니다! 몇 번 이동할까요? 숫자를 입력하세요: ").strip()

        if count.isdigit():
            count = int(count)

            if count >= 1:
                return count

        print("1 이상의 숫자를 입력해주세요.")


def choose_count_number_by_computer(start_player):
    count = random.randint(5, 30)
    print(f"\n{start_player}님이 술래입니다.")
    print(f"컴퓨터가 이동 숫자를 정하는 중입니다...")
    print(f"선택된 숫자는 {count}입니다!")

    return count


def find_loser(start_player, count_number, pointing_map):
    current_player = start_player

    print_title("더 게임 오브 데스 진행")
    print(f"시작 사람: {start_player}")
    print(f"이동 횟수: {count_number}")
    print()

    for count in range(1, count_number + 1):
        current_player = pointing_map[current_player]
        print(f"{count}번째 이동 → {current_player}")

    return current_player


def add_drink_to_loser(players, loser_name):
    for player in players:
        if player["name"] == loser_name:
            player["drink"] += 1
            break

    return players

def play_game(players):
    if len(players) < 3:
        print("더 게임 오브 데스는 최소 3명 이상이어야 진행할 수 있습니다.")
        print("현재 참가자가 2명이므로 이 게임은 진행할 수 없습니다.")
        print("다른 게임을 선택해주세요!")
        return players

    print("신난다~ 재미난다~ 더 게임 오브 데스!")
    print("각자 한 명을 지목하고, 숫자만큼 지목 방향을 따라갑니다.")
    print("마지막에 도착한 사람이 술을 마십니다!")

    player_names = get_player_names(players)

    pointing_map = create_pointing_map(players)
    show_pointing_result(pointing_map)

    start_player = choose_start_player(player_names)

    if is_user_player(start_player, players):
        count_number = choose_count_number_by_user()
    else:
        count_number = choose_count_number_by_computer(start_player)

    loser_name = find_loser(start_player, count_number, pointing_map)

    print_title("결과 발표")
    print(f"걸린 사람은 바로... {loser_name}님입니다!")
    print(f"{loser_name}님은 🍺 1잔을 마십니다.")

    players = add_drink_to_loser(players, loser_name)

    return players