# Из колоды в 52 карты извлекаются случайным образом 4 карты. 
# a) Найти вероятность того, что все карты – крести. 
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

import formulae as f

# а)
total_n = f.combinations(52,4) # всего сочетаний 4 карт из колоды 52
positive_m = f.combinations(13,4) # варианты получить 4 карты крести из всех имеющихся крестей
result_p = f.probability(positive_m,total_n) # p = 0.0026
 
print(result_p)

# б)
positive_m2 = f.combinations(4,1)*f.combinations(48,3) # возможности получить одновременно 1 туз и 3 не туза
result_p2 = f.probability(positive_m2,total_n) # p = 0.2556

print(result_p2)
