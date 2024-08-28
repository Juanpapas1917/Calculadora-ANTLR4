from calculatorVisitor import calculatorVisitor
from calculatorParser import calculatorParser


class MyVisitor(calculatorVisitor):
    """
    Un visitante personalizado para el árbol de análisis sintáctico, implementando operaciones matemáticas.
    """

    def visitPrintExpr(self, ctx: calculatorParser.PrintExprContext):
        """
        Visita un contexto de expresión de impresión, evalúa la expresión y la imprime.

        :param ctx: El contexto de expresión de impresión.
        :return: El valor de la expresión impresa.
        """
        value = self.visit(ctx.expr())
        print(value)
        return value

    def visitInt(self, ctx):
        """
        Visita un contexto de entero y devuelve su valor como un entero.

        :param ctx: El contexto de entero.
        :return: El valor entero del contexto.
        """
        return int(ctx.INT().getText())

    def visitMulDiv(self, ctx):
        """
        Visita un contexto de multiplicación o división y realiza la operación correspondiente.

        :param ctx: El contexto de multiplicación o división.
        :return: El resultado de la operación de multiplicación o división.
        :raises: Un mensaje de error si se intenta dividir por cero.
        """
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == calculatorParser.MUL:
            return left * right
        if right == 0:
            return "No se puede dividir en 0"
        return left / right

    def visitAbs(self, ctx):
        """
        Visita un contexto de valor absoluto y devuelve el valor absoluto de la expresión.

        :param ctx: El contexto de valor absoluto.
        :return: El valor absoluto de la expresión.
        """
        value = self.visit(ctx.expr())
        return abs(value)

    def visitAddSub(self, ctx: calculatorParser.AddSubContext):
        """
        Visita un contexto de adición o sustracción y realiza la operación correspondiente.

        :param ctx: El contexto de adición o sustracción.
        :return: El resultado de la operación de adición o sustracción.
        """
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == calculatorParser.ADD:
            return left + right
        else:
            return left - right

    def visitParens(self, ctx):
        """
        Visita un contexto de paréntesis y evalúa la expresión contenida en los paréntesis.

        :param ctx: El contexto de paréntesis.
        :return: El resultado de la expresión contenida en los paréntesis.
        """
        return self.visit(ctx.expr())
