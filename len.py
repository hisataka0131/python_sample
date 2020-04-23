def len_command(command):
    cmd, text = command.split()
    length = len(text)
    response = '文字の長さは{}文字です。'.format(length)
    return response 