def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum


def first_number(num):
    while num >= 10:
        num = num // 10
    return int(num)


birth_day = 24
birth_month = 3
birth_year = 1991

first_base_number = sum_of_digits(birth_year) + sum_of_digits(birth_month) + sum_of_digits(birth_day)
second_base_number = sum_of_digits(first_base_number)
third_base_number = first_base_number - 2 * first_number(birth_day)
fourth_base_number = sum_of_digits(third_base_number)

print(first_base_number)
print(second_base_number)
print(third_base_number)
print(fourth_base_number)


