from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()

d = QDate(1998, 5, 7)

print(f'Days in month: {d.daysInMonth()}')
print(f'Days in year: {d.daysInYear()}')