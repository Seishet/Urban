def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        next_ = get_multiplied_digits(int(str_number[1:]))
        if next_ != 0:
            return (first * next_)
        else:
            return (first)
    else:
        return (first)

print(get_multiplied_digits(2220001))

