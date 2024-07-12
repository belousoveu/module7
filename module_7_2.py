def is_valid_filename(filename):
    if not filename:
        return False

    if filename.startswith("."):
        return False

    valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.-'
    return all(char in valid_chars for char in filename)


def custom_write(file_name, strings):
    if is_valid_filename(file_name):
        file_name = file_name if file_name.endswith(".txt") else file_name + ".txt"
    else:
        file_name = "default.txt"
    strings_position = {}

    with open(file_name, "w", encoding="utf-8") as f:
        for i, string in enumerate(strings):
            strings_position[(i + 1, f.tell())] = string
            f.write(string + "\n")
    return strings_position


if __name__ == "__main__":

    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!',
        'И еще одна строка. One more string'
    ]

    result = custom_write('test', info)
    for elem in result.items():
        print(elem)
