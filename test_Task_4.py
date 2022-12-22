from os import system
from random import random
import unittest


class Tests( unittest.TestCase ):
    def test_equal( self ):
        self.assertEqual( strange_function( 45 ), "101101" )
        self.assertEqual( strange_function( 3 ), "11" )
        self.assertEqual( strange_function( 2 ), "10" )


def strange_function( some_int: int ) -> str:
    # Работает только без отступа после :b
    return f"{some_int:b}"


def main():
    print( "Программа для преобраования десятичного числа в двоичное.\n" )

    print( f"45 - > { strange_function( 45 ) }" )
    print( f"3 -> { strange_function (3 ) }" )
    print( f"2 -> { strange_function( 2 ) }\n" )

    s = ""
    n = int(input("Введите целое число: "))
    
    while n != 0:
        s = str( n % 2 ) + s
        n //= 2

    print(f"{ int(s, 2) } -> { s }\n")


if __name__ == "__main__":
    system( "cls" )

    main()
