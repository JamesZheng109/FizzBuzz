def FizzBuzz(beg_num,end_num,num_1,num_2,word1='',word2=''):
    if word1=='':word1='Fizz'
    if word2=='':word2='Buzz'
    for i in range(beg_num,end_num+1):
        t,f=i/num_1,i/num_2
        if t.is_integer() and f.is_integer():print(f'{word1}{word2}')
        elif t.is_integer():print(word1)
        elif f.is_integer():print(word2)
        else:print(i)
