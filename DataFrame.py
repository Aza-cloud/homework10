# | Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

#Решение

data = pd.DataFrame({'whoAmI': lst})
values_unique = data['whoAmI'].unique()
one_hot = pd.DataFrame()

for value in values_unique:
  one_hot[value] = (data['whoAmI'] == value).astype(int)

one_hot.head()