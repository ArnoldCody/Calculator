#coding:utf-8
#Author: Arnold YANG
#Python Calculator (calculator.py)

import evaluators
from parsers import Parsers
from token import TokenType
from calcExceptions import *
import scanner

#Function used to print a description of the token
#followed by the token itself
def printTokens(tokens):
    iterator = 0
    expressions = ''
    """test
    print "tokens[iterator]: ", tokens[iterator]
    print "tokens[iterator].getType(): ", tokens[iterator].getType()
    print "tokens[iterator].getValue(): ", tokens[iterator].getValue()
    """
    while iterator != len(tokens):
        # 用三个条件句call tokens列表 里面类的methods，之后print，直到 iterator = len(tokens)
        if tokens[iterator].getType() == TokenType.NUMBER_TOKEN:
            print "Number:\t\t",
            print tokens[iterator].getValue()
            expressions += str(tokens[iterator].getValue()) + ' '
        elif tokens[iterator].getType() == TokenType.OPERATOR_TOKEN:
            print "Operator:\t",
            print tokens[iterator].getValue()
            expressions += str(tokens[iterator].getValue()) + ' '
        elif tokens[iterator].getType() == TokenType.PAREN_TOKEN:
            print "Parenthesis:\t",
            print tokens[iterator].getValue()
            expressions += str(tokens[iterator].getValue()) + ' '
        iterator += 1
    print 'Expression:',
    print expressions

def main(): # 运行主程序
    while True:
        print "\nPython Calculator: "
        line = list()
        while True: # delete the ' ' in input and add a ' ' in the end
            user_input = raw_input("Enter Expression: ")
            user_input = user_input.replace(' ', '')
            if user_input is not None and len(user_input.strip()) == 0:
                break
            user_input += " "
            line.append(user_input)
            break
        expr = line
        """test
        test print len(expr)
        if input is 1+1
        return ["1+1 "]
        """

        if len(expr) == 0:
            break
        try:
            scan = scanner.Scanner()
            tokens = list()
            # test print "tokens: ", tokens
            tokens = scan.parseExpression(expr[0])
            # 返回列表self.tokens，里面包含 token.py 里面类的实例
            # test print "tokens: ", tokens
            printTokens(tokens) # 打印 expression 以及每一个 tokentype 和 tokenvalue
            parsers = Parsers() # 将 parsers 设为 Class Parsers 的一个实例
            expressionTree = parsers.parse(tokens) # call Parsers.parse()
            # test print "expressionTree: ", expressionTree
            evaluator = evaluators.Evaluators()
            result = evaluator.evaluate(expressionTree)
            # test print "2nd expressionTree: ", expressionTree
            print '\nResult:',
            print result
        except CalcExceptions, x:
            print 'Error!:',
            print x.message


if __name__ == '__main__':
    main()
