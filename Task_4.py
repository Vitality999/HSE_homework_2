# 4. (1 балл)
# Для объединенного словаря из прошлого примера посчитайте итоговую сумму продуктов.
from Task_3 import output

Price = 0
Description = 'Итоговая сумма продуктов:'

for line in output.values():
    Price += line.get('Price', 'NaN')
print(Description, Price)
