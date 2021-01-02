date = '28.11.1992'
d, m, y = date.split('.')
print(d, m, y)

days = {
    '28': 'двадцать восьмое',
}

months = {
    '11': 'ноября'
}

result = f'{days[d]} {months[m]} {y} года'
print(result)