# Generated from calculator.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .calculatorParser import calculatorParser
else:
    from calculatorParser import calculatorParser

# This class defines a complete generic visitor for a parse tree produced by calculatorParser.

class calculatorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by calculatorParser#prog.
    def visitProg(self, ctx:calculatorParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculatorParser#printExpr.
    def visitPrintExpr(self, ctx:calculatorParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculatorParser#blank.
    def visitBlank(self, ctx:calculatorParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculatorParser#parens.
    def visitParens(self, ctx:calculatorParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculatorParser#Abs.
    def visitAbs(self, ctx:calculatorParser.AbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculatorParser#MulDiv.
    def visitMulDiv(self, ctx:calculatorParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculatorParser#AddSub.
    def visitAddSub(self, ctx:calculatorParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculatorParser#float.
    def visitFloat(self, ctx:calculatorParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculatorParser#int.
    def visitInt(self, ctx:calculatorParser.IntContext):
        return self.visitChildren(ctx)



del calculatorParser