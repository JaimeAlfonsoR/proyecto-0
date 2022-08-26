import nltk as tk


def main():
    filename = 'prueba1.txt'
    file = open(filename).read()
    tokens = tk.word_tokenize(file)
    parser(tokens)


""""
**** Palabras y letras del lenguaje del robot: ****

M : to move forward
R: to turn right
C: to drop a chip
B: to place a balloon
c: to pickup a chip
b: to grab a balloon
P: to pop a balloon

J(n): jump forward n steps
G(x,y): go to position (x,y)

PROG: program definition begins
GORP: program definition ends

VAR: declaration of variables (list of names) separated by commas
    (a name is a string of alphanumeric characters that begins with a letter)
    (the list is followed by ;)

PROC: procedure definition followed by a name, followed by a list of
    parameters within parenthesis separated by commas,
    followed by a block of instructions

CORP: end of the procedure

-Un bloque de instrucciones es una secuencia de instrucciones 
    separado por semiclons within curly brackets {}

-----------------------------------------------------------------------------
COMANDOS:

walk(n): donde n es un numero, variable o parametro
jump(n)
jumpTo(n,m)
veer(D): where D can be left, right, or around
look(O): where O can be north, south, east or west
drop(n)
grab(n)
get(n)
pop(n)
walk(d,n)
walk(o, n)

------------------------------------------------------------------------------
CONDICIONALES:

1) if (condition)Block1 else Block2 fi
    executes Block1 if condition is true and Block2 if condition is false.

2) if (condition)Block1 fi
    executes Block1 if condition is true does not do anything if it is false.

3) while (condition)do Block od
    executes Block while condition is true

4) repeatTimes n Block per
    executes block n times, where n is a variable or a parameter or a number.

-------------------------------------------------------------------------------
Condiciones:

isfacing(O): donde O es norte, sur, este u oeste.
isValid(ins, n): where ins can be walk, jump, grab, pop, pick, free,
                drop, and n is a number or a variable
canWalk(d,n)
canWalk(o, n)
not(cond): where cond is a condition

"""


def varsRobot():
    pass


def parser(tokens):
    if tokens[0] == 'PROG' and tokens[-1] == 'GORP':
        # Elimina la palabra prog y gorp para hacer testeos
        tokens.remove(tokens[0])
        tokens.remove(tokens[-1])

        for each in tokens:
            print(each)

            # if each == 'VAR':
            # continue

            # if each != '' and each != ',' and each != ';':
            # vars.append(each)


if __name__ == "__main__":
    main()
