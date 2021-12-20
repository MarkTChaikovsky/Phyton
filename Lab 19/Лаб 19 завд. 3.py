"""
Довідник старости. База даних студентів групи: прізвище ім’я по-батькові,
 рік народження, адреса, рейтинг. Організувати вибір за довільним запитом.
  Дані зберігаються в масиві записів, який створюється динамічно.
"""
st_book = [['Bazeluk Lidia Oleksandrivna', '02.10.2004', 'vulica St.Bandery', 'rank 1'],
           ['Brovdi Vitaliy Mihalovich', '01.10.2004', 'vulica Svobody', 'rank 2'],
           ['Dovganich Igor Olegovich', '03.10.2004', 'vulica Virmenska', 'rank 3'],
           ['Yovbak Nika Igorivna', '04.10.2004', 'vulica Sichovih Striltsiv', 'rank 4'],
           ['Mudrenuk Sofia Evgenivna', '5.10.2004', 'Francuskij Bulvar', 'rank 5']]
with open('Lab19_3.txt', 'w') as file:
    for i in range(len(st_book)):
        file.write(' '.join(st_book[i]) + '\n')
info = str(input('що саме ви хочете: '))
f = open('Lab19_3.txt')
for line in f:
    line1 = line.split(sep=' ')
    if info in line or info + '\n' in line1:
        print(*line1[::])
f.close()