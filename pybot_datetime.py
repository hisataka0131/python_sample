from datetime import date, datetime

# 今日の日ずけを返す関数
def today_command():
    today = date.today()
    response = '今日の日ずけは{}です。'.format(today)
    return response

# 現在時刻を返す関数
def now_command():
    now = datetime.now()
    response = '現在時刻は{}です'.format(now)
    return response

# 指定した日の曜日を返す関数
def weekday_command(command):
    try:
        data = command.split()
        year = int(data[1])
        month = int(data[2])
        day = int(data[3])
        one_day = date(year, month, day)

        weekday_str = '月火水木金土日'
        weekday = weekday_str[one_day.weekday()]

        response = '{} は {} 曜日です'.format(one_day, weekday)
    except IndexError:
        response = '3つの値(年月日)を指定してください'
    except ValueError:
        response = '正しい日付を指定してください'
    return response