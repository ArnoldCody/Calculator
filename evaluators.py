#coding:utf-8
#Arnold
#Python Calculator (calculator.py)

from expressionTree import NumberExpressionTree, OperatorExpressionTree

class Evaluators:
    def __init__(self):
        pass
    def evaluate(self, root):
        """test
        self.root = root
        print "root:", self.root
        """
        if isinstance(root, NumberExpressionTree):
            return root.getNumber()
        oper = root.getOperator() # 第一个 root 一定是 OperatorExpressionTree 的实例
        # test print oper
        if oper == '~':
            return -1.0 * self.evaluate(root.right)
        else:
            leftChild = self.evaluate(root.left) # 这种变量赋值遇到 return 会直接终止后续命令，返回 NumberExpressionTree 的实例时，不会运行上面的 oper = root.getOperator()
            rightChild = self.evaluate(root.right)
            if oper == '+':
                # test print "%d + %d = %d" % (leftChild, rightChild, leftChild + rightChild)
                return leftChild + rightChild
            elif oper == '-':
                # test print "%d - %d = %d" % (leftChild, rightChild, leftChild - rightChild)
                return leftChild - rightChild
            elif oper == '*':
                # test print "%d * %d = %d" % (leftChild, rightChild, leftChild * rightChild)
                return leftChild * rightChild
            elif oper == '/':
                try:
                    # test print "%d / %d = %d" % (leftChild, rightChild, leftChild / rightChild)
                    return leftChild / rightChild
                except ZeroDivisionError:
                    return float('Inf')
        return 0.0
