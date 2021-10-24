print ( '請輸入兩個正整數，我們會計算兩數的最大公因數以及最小公倍數' )
x = int ( input ( '請輸入第一個數' ) )
y = int ( input ( '請輸入第二個數' ) )

if x > y :
    x, y = y, x
    
def gct ( x, y ) :

    for i in range ( x, 0, -1 ) :

        if x % i == 0 and y % i == 0 :
            return i
                
def lcm ( x, y ) :

    return x * y / gct ( x, y ) 

print ( '{}和{}的最大公因數是{}' .format ( x, y, gct ( x, y ) ) )
print ( '{}和{}的最小公倍數是{}' .format ( x, y, int ( lcm ( x, y ) ) ) )