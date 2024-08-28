# Generated from calculator.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .calculatorParser import calculatorParser
else:
    from calculatorParser import calculatorParser

# This class defines a complete listener for a parse tree produced by calculatorParser.
class calculatorListener(ParseTreeListener):

    # Enter a parse tree produced by calculatorParser#prog.
    def enterProg(self, ctx:calculatorParser.ProgContext):
        pass

    # Exit a parse tree produced by calculatorParser#prog.
    def exitProg(self, ctx:calculatorParser.ProgContext):
        pass


    # Enter a parse tree produced by calculatorParser#printExpr.
    def enterPrintExpr(self, ctx:calculatorParser.PrintExprContext):
        pass

    # Exit a parse tree produced by calculatorParser#printExpr.
    def exitPrintExpr(self, ctx:calculatorParser.PrintExprContext):
        pass


    # Enter a parse tree produced by calculatorParser#blank.
    def enterBlank(self, ctx:calculatorParser.BlankContext):
        pass

    # Exit a parse tree produced by calculatorParser#blank.
    def exitBlank(self, ctx:calculatorParser.BlankContext):
        pass


    # Enter a parse tree produced by calculatorParser#parens.
    def enterParens(self, ctx:calculatorParser.ParensContext):
        pass

    # Exit a parse tree produced by calculatorParser#parens.
    def exitParens(self, ctx:calculatorParser.ParensContext):
        pass


    # Enter a parse tree produced by calculatorParser#Abs.
    def enterAbs(self, ctx:calculatorParser.AbsContext):
        pass

    # Exit a parse tree produced by calculatorParser#Abs.
    def exitAbs(self, ctx:calculatorParser.AbsContext):
        pass


    # Enter a parse tree produced by calculatorParser#MulDiv.
    def enterMulDiv(self, ctx:calculatorParser.MulDivContext):
        pass

    # Exit a parse tree produced by calculatorParser#MulDiv.
    def exitMulDiv(self, ctx:calculatorParser.MulDivContext):
        pass


    # Enter a parse tree produced by calculatorParser#AddSub.
    def enterAddSub(self, ctx:calculatorParser.AddSubContext):
        pass

    # Exit a parse tree produced by calculatorParser#AddSub.
    def exitAddSub(self, ctx:calculatorParser.AddSubContext):
        pass


    # Enter a parse tree produced by calculatorParser#float.
    def enterFloat(self, ctx:calculatorParser.FloatContext):
        pass

    # Exit a parse tree produced by calculatorParser#float.
    def exitFloat(self, ctx:calculatorParser.FloatContext):
        pass


    # Enter a parse tree produced by calculatorParser#int.
    def enterInt(self, ctx:calculatorParser.IntContext):
        pass

    # Exit a parse tree produced by calculatorParser#int.
    def exitInt(self, ctx:calculatorParser.IntContext):
        pass



del calculatorParser