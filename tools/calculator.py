import ast
import operator
from langchain.tools import tool

# Allowed mathematical operations
operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg
}


def safe_calculate(expression):
    node = ast.parse(expression, mode="eval").body

    def evaluate(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in operators:
            left = evaluate(node.left)
            right = evaluate(node.right)
            return operators[type(node.op)](left, right)

        if isinstance(node, ast.UnaryOp) and type(node.op) in operators:
            return operators[type(node.op)](evaluate(node.operand))

        raise ValueError("Unsupported mathematical expression")

    return evaluate(node)


@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions such as 25 * 4 or 100 / 5."""

    try:
        result = safe_calculate(expression)
        return str(result)

    except Exception:
        return "Sorry, I could not calculate that expression."
