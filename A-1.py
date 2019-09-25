# A-1 日本の九九表の作成


def main():
    # 日本の九九表の表示
    for gyo in range(1, 10):
        for retsu in range(1, 10):
            print(f'{gyo * retsu}', end=' ')  # 九九の内容
        print('')  # 改行


if __name__ == '__main__':
    main()
