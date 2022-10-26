def ex1():
    """Return the boolean True"""
    return True


def ex2():
    """Return the boolean False"""
    return False


def ex3():
    """Return integer 10"""
    return 10


def ex4():
    """Return float 3.5"""
    return 3.5


def ex5():
    """Return the string a"""
    return "a"


def ex6():
    """Return the string EAS503"""
    return "EAS503"


def ex7():
    """
    True or False: Buffalo is in New York.
    Return True or False
    """
    return True


def ex8():
    """
    True or False: New York is the largest state in the United States
    Return True or False
    """
    return False


def ex9():
    """
    Which of the following in an incorrect Python variable name? Return a letter without parenthesis.
    (a) -- test1234
    (b) -- 3pi
    (c) -- __factor
    (d) -- mean__value__2
    """
    return "b"


def ex10():
    """
    Square 3 and 4 and return the their summed value
    """
    return (3 * 3) + (4 * 4)


def ex11():
    """
    Divide 2020 by 5 and return the value
    """
    return 2020 / 5


def ex12():
    """
    Return the remainder of 512 divided by 16
    """

    return 512 % 16


def ex13():
    """
    Return 36 divided by 5
    """
    return 36 / 5


def ex14():
    """
    Return the quotient when 36 divided by 5
    """
    return 36 // 5


def ex15():
    """
    Return the area of a circle with radius 6
    """
    return 3.14 * (6 * 6)


def ex16():
    """
    Given the temperature in fahrenheit (temperature_in_f), return the temperature in Celsius
    """
    temperature_in_f = 67
    return (temperature_in_f - 32) * 5 / 9


def ex17():
    """
    Given the string 'EAS503', return the letter E using the square-bracket syntax
    """
    return "EAS503"[0]


def ex18():
    """
    Given the string 'EAS503', return the letter S using the square-bracket syntax
    """
    return "EAS503"[2]


def ex19():
    """
    Given the string 'EAS503', return the last character in the string using the square-bracket syntax
    """
    return "EAS503"[-1]


def ex20():
    """
    Given a float value, convert it to an int type and return the value
    """
    return int(3.00000)


def ex21():
    """
    PI is given in string data type, return it in float data type
    """
    return float("3.14159")


def ex22():
    """
    Return the data type of the variable test_variable
    """
    test_variable = "Hello World!"
    return type(test_variable)


def ex23():
    """
    Return the data type of the variable test_variable
    """
    test_variable = 1.000000001
    return type(test_variable)


def ex24():
    """
    True or False: In Python you can declare a variable without specifying its data type.
    Return True or False
    """
    return True


def ex25():
    """
    True or False: In Python a variable that was used as a string can be reused as a float.
    Return True or False
    """
    return True


def ex26():
    """
    Given the height and base of a triangle, calculate its area and return it
    """
    base, height = 15, 1
    return (base * height) / 2


def ex27(filename):
    """
    Open the file specified by filename and sum the values found in them.
    Return the value of sum and write the string 'The total is <>.' in a file called 'ex1_output.txt'
    Must name output file: 'ex1_output.txt'
    """
    total = 0
    file = open('ex1_input.txt', 'r')
    lines = file.readlines()
    for i in lines:
        total += int(i)
    file.close
    file = open('ex1_output.txt', 'w')
    file.write('The total is {}.'.format(str(total)))
    return total
