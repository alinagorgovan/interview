import datetime

CONTROL_NUMBER = "279146358279"

def check_cnp(cnp):
    if not cnp.isdecimal() or len(cnp):
        print("Invalid cnp.")
        return -1

    s = int(cnp[0])

    if s == 0:
        print("Invalid sex code.")
        return -1

    date = f"{cnp[3:5]}/{cnp[5:7]}/{cnp[1:3]}"
    try:
        datetime.datetime.strptime(date, '%m/%d/%y')
    except ValueError:
        print("Invalid date.")
        return -1


    jj = int(cnp[7] + cnp[8])
    if jj < 1 or jj > 52:
        print("Invalid county id.")
        return -1

    nnn = int(cnp[9] + cnp[10] + cnp[11])

    if nnn == 0:
        print("Invalid county day number.")
        return -1

    cnp = list(map(int, list(cnp)))
    control_list = list(map(int, list(CONTROL_NUMBER)))

    c = cnp[12]
    check = sum(x * y for x, y in zip(cnp[:12], control_list)) % 11
    if check != c or (check == 10 and c != 1):
        print("Invalid control number.")
        return -1

    return 0

print(check_cnp("2980707090058"))
