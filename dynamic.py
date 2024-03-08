x = 1

def main():

    print(assign())
    pass

def assign():
    x = 2
    return f()

def f():
    print(x)
    return x

if __name__ == "__main__":
    main()