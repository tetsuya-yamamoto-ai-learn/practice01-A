def main():
    # 入力部
    integer_group = input('データを入力してください(スペース区切り) > ')

    # 計算部
    # リストに分割(split →　mapでint型に変換)
    integer_list = list(map(int, integer_group.split(' ')))

    # 各基礎統計量を計算
    # 合計
    sum = 0.0
    for num in integer_list:
        sum += num

    # 最大値
    max = integer_list[0]
    for num in integer_list:
        if num > max:
            max = num

    # 最小値
    min = integer_list[0]
    for num in integer_list:
        if num < min:
            min = num

    # 平均
    average = sum / len(integer_list)

    # 出力部
    print('合計値: ', int(sum))
    print('最大値: ', max)
    print('最小値: ', min)
    print('平均値: ', int(average))


if __name__ == '__main__':
    main()
