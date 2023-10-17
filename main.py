# Написати рекурсивну функцію знаходження ступеня числа.

# def get_num_pow(number, degree):
#     if degree <= 1:
#         return number
#
#     return number * get_num_pow(number, degree - 1)
#
#
# print(get_num_pow(2, 3))
# get_num_pow(2, 3) -> 2 * get_num_pow(2, 2) => 8
# get_num_pow(2, 2) -> 2 * get_num_pow(2, 1) => 4
# get_num_pow(2, 1) => 2

# Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
# Проілюструйте роботу функції прикладом. (Протестувати)

# def print_stars_raw(N:int) -> str:
#
#    if N <= 0:
#        return ''
#    else:
#        return '*'+str(print_stars_raw(N-1))
#
# print(print_stars_raw(int(input('Enter the number of stars you want to print: '))))

# 3
# * + print_stars_raw(3-1) -> * + print_stars_raw(2) => ***
# * + print_stars_raw(2-1) -> * + print_stars_raw(1) => **
# * + print_stars_raw(1-1) -> * + '' => *


# Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
# Користувач вводить a та b. Проілюструйте роботу функції прикладом.
#
# def sum_in_range(a:int, b:int) -> int:
#     if a > b:
#         return 0
#
#     return a + sum_in_range(a+1,b)
#
# print(sum_in_range(1,5))


# 1 + sum_in_range(1+1,5) -> 1+14 => 15
# 2 + sum_in_range(1+2,5) -> 2+12 => 14
# 3 + sum_in_range(1+3,5) -> 3+9 => 12
# 4 + sum_in_range(1+4,5) -> 4+5 => 9
# 5 + sum_in_range(1+5,5) -> 5+0 => 5
