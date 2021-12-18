# Все встроенные типы данных в Python приводятся к логическому типу bool по определенным правилам:
# Ложь: ‘’, [], (), {}, 0, None, ...
# Истина: ‘abc’, [1], (1,), {1:’a’}, 10, 1.1, ...
#

n = None
if n is None:
    print('it is none')
import math
x = float('nan')
math.isnan(x)
if str(type(x)) == "nan":
    print(x)


print([0] and 0 and 1.2 and '1')
print()