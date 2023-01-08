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


def digit_count_occurance(n, d):
    count = 0
    # Loop to find the digits of N
    while (n > 0):
        # check if the digit is D
        if n % 10 == d:
            count = count + 1
        n = n // 10
    return count


birth_day = 24
birth_month = 9
birth_year = 1991

first_base_number = sum_of_digits(birth_year) + sum_of_digits(birth_month) + sum_of_digits(birth_day)
second_base_number = sum_of_digits(first_base_number)
third_base_number = first_base_number - 2 * first_number(birth_day)
fourth_base_number = sum_of_digits(third_base_number)

print(first_base_number)
print(second_base_number)
print(third_base_number)
print(fourth_base_number)
print(digit_count_occurance(birth_year, 9))



