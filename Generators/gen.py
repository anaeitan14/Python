basic_list = [ x*10 for x in range(0,10)]

nested_for = [x*y for x in range(1,11) for y in range(1,11)]

basic_gen = (x*100 for x in range(0,10))

def iter_gen():
    for number in range(0,10):
        yield number*10




if __name__ == "__main__":
    nums = iter_gen()
    try:
        while True:
            print(next(nums))
    except:
        print("Done no more numbers to print")

