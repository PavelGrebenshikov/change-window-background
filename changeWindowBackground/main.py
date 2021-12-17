from changeBackground import ChangeBackground
import argparse

def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("-r", "--random", action="store_true")
    args = parse.parse_args()

    input_user_path = input("Введите путь: ")
    change_bg = ChangeBackground(r"{0}".format(input_user_path).strip())

    if args.random:
        change_bg.change_random_background()
    else:
        change_bg.change_backgorund()

if __name__ == "__main__":
    main()