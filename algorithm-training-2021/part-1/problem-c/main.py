#!/usr/bin/env python3

"""
Телефонные номера в адресной книге мобильного телефона имеют один из следующих форматов: +7<код><номер>, 8<код><номер>, <номер>, где <номер> — это семь цифр, а <код> — это три цифры или три цифры в круглых скобках. Если код не указан, то считается, что он равен 495. Кроме того, в записи телефонного номера может стоять знак “-” между любыми двумя цифрами (см. пример). На данный момент в адресной книге телефона Васи записано всего три телефонных номера, и он хочет записать туда еще один. Но он не может понять, не записан ли уже такой номер в телефонной книге. Помогите ему! Два телефонных номера совпадают, если у них равны коды и равны номера. Например, +7(916)0123456 и 89160123456 — это один и тот же номер.
Формат ввода

В первой строке входных данных записан номер телефона, который Вася хочет добавить в адресную книгу своего телефона. В следующих трех строках записаны три номера телефонов, которые уже находятся в адресной книге телефона Васи. Гарантируется, что каждая из записей соответствует одному из трех приведенных в условии форматов.
Формат вывода

Для каждого телефонного номера в адресной книге выведите YES (заглавными буквами), если он совпадает с тем телефонным номером, который Вася хочет добавить в адресную книгу или NO (заглавными буквами) в противном случае. 
"""


def sub_solution_c(s: str) -> int:
    r = ""
    for c in s:
        if c.isdigit():
            r += c
    if len(r) == 11:
        code = r[-10:-7]
        number = r[-7:]
        if code == "495":
            return int(number)
        return int(code + number)
    return int(r)


def read(name: str = 'input.txt') -> (list[int]):
    reader = open(name, 'r')
    a = sub_solution_c(reader.readline())
    b = sub_solution_c(reader.readline())
    c = sub_solution_c(reader.readline())
    d = sub_solution_c(reader.readline())
    reader.close()
    return [a, b, c, d]


def write(result: list[bool], name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    for b in result:
        if b:
            writer.write("YES\n")
        else:
            writer.write("NO\n")
    writer.close()
    pass


def solution_c(l: list[int]) -> list[bool]:
    r = list[bool]()
    for idx in range(1, len(l)):
        if l[0] == l[idx]:
            r.append(True)
        else:
            r.append(False)
    return r


def problem_c() -> None:
    write(solution_c(read()))
    pass


def main():
    problem_c()
    pass


if __name__ == "__main__":
    main()
    pass
