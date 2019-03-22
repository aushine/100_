def ishvwf(num):
    num_ = int(str(num)[::-1])
    if num_ == num:
        return True
    return False
print(ishvwf(123456))