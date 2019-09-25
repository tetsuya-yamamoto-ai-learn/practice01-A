def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    # 気温の合計を計算
    sum_temperature = 0.0
    for point_weather_information in weather_information:
        sum_temperature += point_weather_information['temperature']

    # 気温の合計/データ数で平均気温を計算
    average_temperature = sum_temperature / len(weather_information)
    print('average_temperature : ', average_temperature)

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    # 大阪府リストを作成
    list_osaka_station = []
    for point_weather_information in weather_information:
        if point_weather_information['prefecture'] == '大阪府':
            list_osaka_station.append(point_weather_information["station"])

    # 大阪府リストをカンマ区切りで統合して表示
    osaka_station = ','.join(list_osaka_station)
    print(osaka_station)

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    # 気温の合計を計算
    sum_fukuoka_temperature = 0.0
    data_num_fukuoka = 0
    for point_weather_information in weather_information:
        if point_weather_information['prefecture'] == '福岡県':
            sum_fukuoka_temperature += point_weather_information['temperature']
            data_num_fukuoka += 1

    # 気温の平均 = 気温の合計 / データの数で平均気温を計算
    average_fukuoka_temperature = sum_fukuoka_temperature / data_num_fukuoka
    print('average_fukuoka_temperature : ', average_fukuoka_temperature)


if __name__ == '__main__':
    main()
