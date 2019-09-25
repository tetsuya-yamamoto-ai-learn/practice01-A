import random


def main():
    # 入力部
    surface_N = int(input('サイコロの面の数は？: '))
    trials_M = int(input('何回振りますか？: '))

    # 計算
    result_list = []  # 出目リスト
    for trial in range(trials_M):
        # 1からsurface_Nまでの整数で出目をランダムに選択
        result = random.randint(1, surface_N)

        # 出目を追加
        result_list.append(result)

    # 出力部
    print(result_list)


if __name__ == '__main__':
    main()
