def decode(message_file):
    file = open(message_file, "r")
    lines = file.readlines()

    word_number_pair = []
    for line in lines:
        number, word = line.split()
        word_number_pair.append((int(number), word))
    pyramid = sorted(word_number_pair, key=lambda x: x[0])

    decoded_message = ''
    items_on_row = 1
    row = 1
    for i in range(len(pyramid)):
        if i + 1 == items_on_row:
            decoded_message += pyramid[i][1] + ' '
            items_on_row += row + 1
            row += 1

    print(decoded_message)


decode('coding_qual_input.txt')
