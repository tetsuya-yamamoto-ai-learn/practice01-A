def main():
    # 入力部
    rows = int(input("行数を入力してください: "))
    cols = int(input("列数を入力してください: "))

    # 出力部
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            exp = f'{row: >2} x {col: >2} = {row * col: >2}'  # 表示する式
            print(exp, end=' | ')
        print('');


if __name__ == '__main__':
    main()
