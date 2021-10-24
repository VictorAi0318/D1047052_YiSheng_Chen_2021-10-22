print ( '請輸入一個0~255之間的正整數，我們將會把這個數字轉換成2~9進制' )
n = int ( input ( '請輸入0~255之間的正整數' ) )
b = int ( input ( '請問要轉換成2~9的哪個進制?' ) )
list = []

if 0 <= n <= 255 and 2 <= b <= 9 :

    while n >= b :
        list .append ( n % b )
        n //= b

    list .append ( n )
    list .reverse ()
#    print ( '',  .join ( list ) )

else :
    print ( '輸入錯誤，請從新輸入' )