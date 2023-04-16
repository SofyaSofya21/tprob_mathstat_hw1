# В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали. 
# Какова вероятность того, что все извлеченные детали окрашены?

import formulae as f

total_n = f.combinations(15,3) # всего вариантов как достанутся 3 детали
positive_res_m = f.combinations(9,3) # кол-во способов достать 3 окрашенных детали
positive_res_p = f.probability(positive_res_m,total_n) # p = 0.1846

print(positive_res_p)