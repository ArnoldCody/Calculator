#coding:utf-8
#Author:Arnold YANG
#Python Calculator (calculator.py)

"""继续学习此代码
研究返回值
"""


from calcExceptions import CalcExceptions
import expressionTree
from token import TokenType

#Parsers class - parses tokens 解析 tokens
class Parsers:
    def __init__(self):
        self.tokens = list()
        self.tokenIterator = 0
        self.currentToken = None
        self.eTree = None

    def parse(self, tokens): # 解析每个 tokens 列表里面的实例
        if len(tokens) == 1:
            raise CalcExceptions("Parser received an empty token list.")
        self.tokens = tokens
        self.currentToken = self.tokens[0] # 取 tokens 里的第一个实例
        eTree = self.parseExpression() # call parseExpression()
        # test print eTree
        if self.currentToken is not None:
            raise CalcExceptions("Unconsumed tokens at end of expression.")
        """test
        print "eTree: ", eTree
        eTree.test()
        """
        return eTree # 返回的是 的一个实例


    def consumeToken(self): # 取下一个实例
        # test print self.tokenIterator
        if self.tokenIterator <= self.tokens.index(self.tokens[-1]):
            self.tokenIterator += 1
        if self.tokenIterator > self.tokens.index(self.tokens[-1]):
            self.currentToken = None
        else:
            self.currentToken = self.tokens[self.tokenIterator]

    def parseExpression(self):
        expr = self.parseTerm()
        """test
        print "expr: ", expr
        print expr.getNumber()
        """
        while self.currentToken is not None and self.currentToken.getType() == TokenType.OPERATOR_TOKEN and (
                    self.currentToken.getValue() == '+' or self.currentToken.getValue() == '-'):
            oper = self.currentToken.getValue() # 调用 token 类的 getValue(), 返回 +-
            self.consumeToken() # 取下一个实例
            expr = expressionTree.OperatorExpressionTree(oper, expr, self.parseTerm())
            """
            term 里面的 self.parseFactor() 开启解析下一个数字。然后一直递归。直至解析完成，最后 eTree 的 right 分支会根据 4 则运算法则逐渐成长）
            """
        return expr

    def parseTerm(self):
        term = self.parseFactor()
        """test
        print "term: ", term
        print term.getNumber()
        """
        while self.currentToken is not None and self.currentToken.getType() == TokenType.OPERATOR_TOKEN and (
                    self.currentToken.getValue() == '*' or self.currentToken.getValue() == '/'):
            oper = self.currentToken.getValue() # 调用 token 类的 getValue(), 返回 */
            self.consumeToken() # 取下一个实例
            term = expressionTree.OperatorExpressionTree(oper, term, self.parseFactor())
        """
        term 里面的 self.parseFactor() 开启解析下一个数字。然后一直递归。直至解析完成，最后 eTree 的 right 分支会根据 4 则运算法则逐渐成长）
        """
        return term

    def parseFactor(self):
        if self.currentToken is None:
            raise CalcExceptions('Reached end of tokens while expecting a number.')
        factor = None
        if self.currentToken.getType() == TokenType.PAREN_TOKEN and self.currentToken.getValue() == '(':
            self.consumeToken() # 取下一个实例
            factor = self.parseExpression()
            if self.currentToken is None or self.currentToken.getValue() != ')':
                raise CalcExceptions('Badly formed parenthesized expression.')
            self.consumeToken()
        elif self.currentToken.getType() == TokenType.OPERATOR_TOKEN and self.currentToken.getValue() == '~':
            self.consumeToken()
            subExpr = self.parseNumber()
            factor = expressionTree.OperatorExpressionTree('~', None, subExpr)
        else:
            factor = self.parseNumber()
            """test
            print "factor: ", factor
            print factor.getNumber()
            """
        return factor


    def parseNumber(self):
        if self.currentToken is None:
            raise CalcExceptions('Reached end of tokens while expecting a number.')
        if self.currentToken.getType() == TokenType.NUMBER_TOKEN:
            value = self.currentToken.getValue()
            self.consumeToken()
            return expressionTree.NumberExpressionTree(value)
        else:
            raise CalcExceptions("Expected a number.")
