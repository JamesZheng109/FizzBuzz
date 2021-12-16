def FizzBuzz(beg_num,end_num,num_1,num_2):
    for i in range(beg_num,end_num+1):
        t=i/num_1
        f=i/num_2
        if t.is_integer() and f.is_integer():
            print('FizzBuzz')
        elif t.is_integer():
            print('Fizz')
        elif f.is_integer():
            print('Buzz')
        else:
            print(i)
