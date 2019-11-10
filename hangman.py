import random


def hangman(word):
    wrong = 0
    stages = [r"",
              r"-----     ",
              r"|    |    ",
              r"|    O    ",
              r"|   /|\   ",
              r"|   / \   ",
              r"|         "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")

    while True:
        msg = "１文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        if "_" not in board:
            print("あなたの勝ち！")
            win = True
            break
        if wrong < len(stages) - 1:
            print("\n".join(stages[0:e]))
        else:
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}。".format(word))


if __name__ == "__main__":
    word_list = [
        "cat",
        "dog",
        "fox"
    ]
    hangman(random.choice(word_list))
