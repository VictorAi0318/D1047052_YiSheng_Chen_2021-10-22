n = int ( input ( '請輸入一個大於1的正整數' ) )

if n > 1 :

    def fun ( n ) :

        n = float ( n )

        if n == 1 :
            return 2

        else :
            return ( fun ( n-1 ) + fun ( n//2 ) )

else :
    print ( '輸入錯誤，請重新輸入')

print ( fun ( n ) )