def heisei_command(command):
    heisei, year_str = command.split()
    if year_str.isdigit():
        year = int(year_str)
        if year >= 1989:
            heisei_year = year - 1988
            response = '西暦{}は、平成{}です'.format(year, heisei_year)
        else:
            response = '西暦{}は、平成ではありません'.format(year)
    else:
        response = '数値を指定してください'
    return response