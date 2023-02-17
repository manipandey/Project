def fibonacci(num):
    a, b = 0, 1
    print(a)
    print(b)
    for i in range(2, num):
        c = a + b
        print(c)
        a, b = b, c

fibonacci(10) 
