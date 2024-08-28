from calculatorVisitor import calculatorVisitor
from calculatorParser import calculatorParser


class MyVisitor(calculatorVisitor):

    def visitPrintExpr(self, ctx: calculatorParser.PrintExprContext):
        value = self.visit(ctx.expr())
        print(value)
        return value

    def visitInt(self, ctx):
        return int(ctx.INT().getText())


    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == calculatorParser.MUL:
            return left * right
        if right == 0:
            return "No se puede dividir en 0"
        return left / right


    def visitAbs(self,ctx):
        value = self.visit(ctx.expr())
        return abs((value))


    def visitAddSub(self, ctx: calculatorParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == calculatorParser.ADD:
            return left + right
        else:
            return left - right

    def visitParens(self, ctx):
        return self.visit(ctx.expr())
