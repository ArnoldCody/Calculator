# coding:utf-8
#Scott Snow
#Comp 141, Homework 7
#Python Calculator (calculator.py)
"""
扫描整个表达，返回 self.tokens
"""

from calcExceptions import CalcExceptions
import token

#Scanner Class
#Takes in user input and splits into tokens
class Scanner: # personal notes
    def __init__(self):
        self.tokens = list()
        self.cursor = 0
        self.EndExp = False
        self.CharNext = ''
        self.expr = ""

    def parseExpression(self, expression):
        self.tokens = list() # intend to return this list
        self.expr = expression # notice there is a ' ' in the end of expression
        self.EndExp = False
        self.cursor = -1
        self.advCursor() # self.cursor += 1, return self.CharNext = self.expr[self.cursor], until self.cursor >= len(self.expr)
        self.token = None
        while True:
            self.token = self.getNextToken()
            if self.token is not None and self.EndExp is False:
                self.tokens.append(self.token) # append a class instance to a list
            else:
                break
        """test
        print self.tokens
        when input is 1+1
        return [<token.NumberToken instance at 0x10a2335a8>, <token.Operator\
                Token instance at 0x10a2335f0>, <token.NumberToken instance \
                at 0x10a233758>]
        """
        return self.tokens

    def getNextToken(self):
        self.token = None
        if self.CharNext == " ": # add ' ' at the end of input already
            self.EndExp = True # finally, return True
        if self.EndExp is True:
            self.token = None
        elif self.isParenthesis(self.CharNext): # test if self.CharNext is '(' or ')'
            self.token = token.ParenToken(self.CharNext) # self.token is instance of class ParenToken(Token) which is a child class of class Token(object)
            self.advCursor() # get next self.CharNext
        elif self.isOperator(self.CharNext): # test if self.CharNext is +-*/
            self.token = token.OperatorToken(self.CharNext) # self.token is instance of class OperatorToken(Token) which is a child class of class Token(object)
            self.advCursor() # get next self.CharNext
        elif self.isDigitOrDecimal(self.CharNext): # test if self.CharNext is 0-9 or '.'
            self.token = token.NumberToken(self.scanNumber()) # self.token is instance of class OperatorToken(Token) which is a child class of class Token(object)
        else:
            return self.token
        return self.token

    def scanNumber(self): # 返回数字
        self.isDigit = False
        self.wholePart = 0.0
        self.fractionalPart = 0.0
        self.fractionalMultiplier = 0.1
        self.past_decimal = False
        while self.EndExp is False and self.isDigitOrDecimal(self.CharNext):
            if self.CharNext == '.': # 遇见 ".", self.past_decimal = True
                if self.past_decimal:
                    raise CalcExceptions("badly formed number - multiple decimal points")
                self.past_decimal = True
            elif self.isDigitOrDecimal(self.CharNext):
                self.isDigit = True
                if self.past_decimal is False: # 算整数部分
                    self.wholePart = int(self.wholePart) * 10 + int(self.CharNext)
                else: # 算小数部分
                    self.fractionalPart += int(self.CharNext) * self.fractionalMultiplier
                    self.fractionalMultiplier /= 10.0
            self.advCursor()
        if self.isDigit is False:
            raise CalcExceptions("badly formed number - decimal point with no digits")
        return self.wholePart + self.fractionalPart # 返回整数部分+小数部分

    def advCursor(self): # 使 self.CharNext 历便 self.expr 里面的每一个数字或运算符，然后逐个返回 self.CharNext
        self.cursor += 1
        if self.cursor >= len(self.expr):
            self.EndExp = True
        else:
            self.CharNext = self.expr[self.cursor]

    def isWhiteSpace(self, c):
        if (c == ' ') or (c == '\t') or (c == '\n'):
            return True

    def isParenthesis(self, c):
        if (c == '(') or (c == ')'):
            return True

    def isOperator(self, c):
        if (c == '+') or (c == '-') or (c == '*') or (c == '/') or (c == '~'):
            return True

    def isDigitOrDecimal(self, c):
        if ('0' <= c <= '9') or (c == '.'):
            return True
