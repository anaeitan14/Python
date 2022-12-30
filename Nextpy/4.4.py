def gen_secs():
    return (second for second in range(0,60))

def gen_minutes():
    return (minute for minute in range(0, 60))

def gen_hours():
    return (hour for hour in range(0, 24))


def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield "%02d:%02d:%02d" % (hour,minute,second)



if __name__ == "__main__":
    time = gen_time()
    print(next(time))
    print(next(time))
    print(next(time))
    print(next(time))









