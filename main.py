def foo(*integers, **words):
    result = 1
    for x in integers:
        result *= x
    print("Wynik mnozenia:",  result)
    result = ""
    for arg in words.values():
        result += arg
    print("Wynik konkatenacji:", result)


# tej funkcji nie można wywołać ponieważ argument 'age' powinien wystąpić przed argumentem *others
def person_print(name, last_name, *others, age):
    formatted_data = 'Imię: {}, nazwisko: {}, wiek: {}'.format(name,last_name,age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)

if __name__ == '__main__':
    foo(1, 2, 3, a="Ewelina", b="Zygmunt")
