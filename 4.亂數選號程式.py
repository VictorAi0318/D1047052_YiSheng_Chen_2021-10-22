import random as rand

n = input ( '請輸入一個正整數' )

rand .seed ( n )

print ( rand .sample ( range ( 1, 42 ), 6 ) )