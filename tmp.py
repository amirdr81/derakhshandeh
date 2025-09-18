def cash_format(input):
    rem = len(input) % 3
    text = ""
    if(rem): text = str((input[0:rem])) + ","
    for i in range(int(len(input[rem:]) / 3)): text += (input[rem:][3 * i : 3 * i + 3] + ",")
    return text[0 : len(text) - 1]

print(cash_format("12345"))