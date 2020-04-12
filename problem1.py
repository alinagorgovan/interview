START = 0
END = 1
TEXT = 2

def replace_text(text, replace_list):
    str_list = list(text)
    result = []
    i = 0

    for r in replace_list:
        result += str_list[i:r[START]]
        result += list(r[TEXT])
        i = r[END]

    return "".join(result)

print(replace_text("Lorem Ipsum este pur şi simplu o macheta pentru \
                   text a industriei tipografice.",
                   [[17, 30, "cu siguranta"], [33, 40, "emblema"],
                    [66, 77, "informatice"]]))