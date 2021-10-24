print ( '請輸入一個0~255之間的正整數，我們將會印出2~您輸入的數之間的質數')
n = int ( input ( '請輸入一個0~255之間的正整數' ) )

if 0 <= n <= 255 :

    if n == 0 :
        print ( '0不為質數' )

    if n == 1 :
        print ( 1 )

    def prime_or_not ( n ) :

        for i in range ( 2, n, 1 ) :

            if n % i == 0 :
                return False

        return True
            
    for j in range ( 2, n+1, 1 ) :
        is_prime = prime_or_not ( j )
        
        if is_prime :
            print ( j )
    
else :
    print ( '輸入錯誤，請輸入一個0~255之間的正整數' )