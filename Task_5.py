# 5. (2 балла)
# Дан один словарь с запасами продуктов на складе.
# Дан второй словарь со стоимостью этих товаров. Создайте словарь с балансом этих продуктов.


d1 = \
{'Item1': 120, 'Item2': 100, 'Item3': 500}
d2 = \
{'Item1': 5, 'Item2': 12, 'Item3': 7}

d3 = {}
for key, value in d1.items():
    d3[key] = value * d2[key]
print('Balance:', d3)

