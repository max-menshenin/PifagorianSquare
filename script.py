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


def get_digit_count_occurrence(n, d):
    count = 0
    while n > 0:
        if n % 10 == d:
            count += 1
        n = n // 10
    return count


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

result_square_string = str(birth_day) + str(birth_month) + str(birth_year) + str(first_base_number)\
                       + str(second_base_number) + str(third_base_number) + str(fourth_base_number)
print(result_square_string, get_digit_count_occurrence(int(result_square_string), 4))
