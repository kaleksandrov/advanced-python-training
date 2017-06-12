import module1


def main():
    width=5
    for num in range(5,12):
        for base in 'dXob':
            print('{0:{width}{base}}'.format(num, base=base, \
                    width=width), end=' ')
            print()


def swap(l):
    l[1], l[0] = l


if __name__ == '__main__':
    main()
    a = 1
    b = 2
    l = [a, b]
    print(l)
    swap(l)
    # swap1(a, b)
    print(l)
