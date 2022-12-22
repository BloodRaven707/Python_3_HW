from os import system
from random import random
import unittest


class Tests( unittest.TestCase ):
    def test_equal( self ):
        self.assertEqual( strange_function( 8 ), [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] )
        self.assertEqual( strange_function( 2 ), [-1, 1, 0, 1, 1] )
        self.assertEqual( strange_function( 1 ), [1, 0, 1] )
        self.assertEqual( strange_function( 0 ), [0] )


def strange_function(some_int: int) -> list:
    result_list = [1, 0, 1] if some_int > 0 else [0]

    for i in range( 1, some_int ):
        result_list.append( 1 if i == 1 else result_list[-1] + result_list[-2] )
        result_list.insert( 0, -1 if i == 1 else result_list[1] - result_list[0] )
                
    return result_list


def main():
    print( "Программа составляет список из чисел Негафибоначчи + Фибоначчи.\n" )
    print( f"Для k = 8 список будет выглядеть так -> { strange_function( 8 ) }\n" )

    k = int( input("Введете целое число: ") )
    print( f"Для {k = } список будет выглядеть так -> { strange_function( k ) }\n" )

if __name__ == "__main__":
    system("cls")

    main()
