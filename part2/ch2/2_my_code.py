"""コンピュータとじゃんけん
    1.OPTIONの表示
    2.ユーザにOPTIONの選択を促す
    3.ユーザが選んだOPTIONの表示
    4.コンピュータが選んだOPTIONの表示
    5.結果の判定
    6.結果の表示
"""

import random
from typing import Union

OPTIONS = ["グー", "チョキ", "パー"]


def print_options() -> None:
    """
    OPTIONの表示
    """
    print("\n".join(f"({i}) {option}" for i, option in enumerate(OPTIONS, 1)))


def get_player_choice() -> str:
    """
    プレイヤーが選択したオプションを返す関数
    Returns:
        str : Optionを返す
    """
    choice_option = int(input("「グー」か「チョキ」か「パー」を番号で選んでください: "))

    return OPTIONS[choice_option - 1]


def get_computer_choice() -> str:

    return random.choice(OPTIONS)


def print_choices(player_choice: str, computer_choice: str) -> None:
    print(f"あなたが選んだのは{player_choice}")
    print(f"コンピュータが選んだのは{computer_choice}")


def judgemen_choice(player_choice: str, computer_choice: str) -> Union[bool, None]:
    """じゃんけんの判定

    Args:
        player_choice (str): playerの選択
        computer_choice (str): computerの選択

    Returns:
        bool | None: playerの勝ち=True、playerの負けFalse | 引き分け=None
    """
    if player_choice == computer_choice:
        return None

    if (
        (player_choice == "グー" and computer_choice == "チョキ")
        or (player_choice == "チョキ" and computer_choice == "パー")
        or (player_choice == "パー" and computer_choice == "グー")
    ):
        return True

    return False


def print_result(player_choice: str, computer_choice: str) -> None:
    """結果の表示

    Args:
        player_choice (str): playerの選択
        computer_choice (str): computerの選択
    """

    if judgemen_choice(player_choice, computer_choice):
        print(f"おめでとうございます！ 「{player_choice}」の勝ちです。")
    elif judgemen_choice(player_choice, computer_choice) is None:
        print("引き分けです。")
    else:
        print(f"残念でした。「{computer_choice}」の勝ちです。")


if __name__ == "__main__":
    print_options()
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print_choices(player_choice, computer_choice)
    print_result(player_choice, computer_choice)
