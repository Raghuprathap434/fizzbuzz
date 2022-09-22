def Raghu_Fizz_Buzz_my_function(N):
    my_list = []
    for num in range(1,N+1):
        divisible_by_3 = (num % 3 == 0)
        divisible_by_5 = (num % 5 == 0)

        if divisible_by_3 and divisible_by_5:
            my_list.append("FizzBuzz")
        elif divisible_by_3:
            my_list.append("Fizz")
        elif divisible_by_5:
            my_list.append("Buzz")
        else:
            my_list.append(str(num))

    print(my_list)

N=100
Raghu_Fizz_Buzz_my_function(N)
