# def pdnf(truth_table: list) -> str:
#     pdnf = ""
#     symbols = ["A", "B", "C", "D"]

#     truth_table.pop(0)

#     for column in truth_table:
#         if column[4] == 0:
#             continue

#         temp_row = column
#         temp_row.pop(-1)

#         for row in range(0, len(temp_row)):
#             if column[row] == 1:
#                 pdnf += f"{symbols[row]}"
#             else:
#                 pdnf += f"{symbols[row]}'"

#         if column != truth_table[-1]:
#             pdnf += " + "

#     return pdnf


def pdnf(truth_table: list) -> str:
    pdnf = []
    symbols = ["A", "B", "C", "D"]

    # Убираем заголовок, работаем с копией
    truth_table = truth_table[1:]

    for column in truth_table:
        if column[-1] == 0:  # Последний элемент - значение функции
            continue

        term = []
        for i in range(len(symbols)):  
            if column[i] == 1:
                term.append(symbols[i])
            else:
                term.append(f"{symbols[i]}'")

        pdnf.append("".join(term))

    return " + ".join(pdnf)