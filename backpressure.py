import random
import time


def emit_gel(step):
    negative_step = False
    current = 50
    while True:
        sign = (yield current)
        if sign == -1:
            negative_step = True
        elif sign == 1:
            negative_step = False
        if negative_step:
            random_step = random.randint((-1 * step), 0)
        else:
            random_step = random.randint(0, step)
        current += random_step


def valve(generator):
    for pressure in generator:
        time.sleep(0.01)
        if pressure > 80 and pressure < 91:
            print(f"{'*' * pressure} {pressure}")
            print(f"valve tripped, high pressure {pressure}")
            pressure = generator.send(-1)
        elif pressure < 20 and pressure > 9:
            print(f"{'*' * pressure} {pressure}")
            print(f"valve tripped, low pressure {pressure}")
            pressure = generator.send(1)
        elif pressure < 10 or pressure > 90:
            generator.close()
            print(f"generator emergency shutdown")
            break
        print(f"{'*' * pressure} {pressure}")


if __name__ == '__main__':
    gen = emit_gel(15)
    valve(gen)
