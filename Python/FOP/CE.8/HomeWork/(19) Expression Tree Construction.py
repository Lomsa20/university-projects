class Node:
    def __init__(self, val):
        # Stores either an operator ('+', '-', '*', '/') or an integer operand
        self.val = val
        # Pointer to left child in the expression tree
        self.left = None
        # Pointer to right child in the expression tree
        self.right = None


def make_node(ops, nodes):
    """
    Pops one operator from the operator stack
    Pops two nodes from the node stack
    Creates a new tree node and pushes it back to nodes stack
    """
    # Remove the operator
    op = ops.pop()

    # Right operand is popped first (LIFO stack)
    right = nodes.pop()

    # Left operand is popped second
    left = nodes.pop()

    # Create a new tree node with the operator
    node = Node(op)

    # Attach left and right subtrees
    node.left = left
    node.right = right

    # Push the constructed subtree back onto the stack
    nodes.append(node)


def build_expression_tree(expr):
    """
    Builds an expression tree from an infix expression
    Assumes tokens are space-separated (e.g. '3 + 4 * 2')
    """
    # Operator precedence mapping
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    # Stack for operators
    ops = []

    # Stack for tree nodes
    nodes = []

    # Split expression into tokens
    tokens = expr.split()

    for token in tokens:
        # If token is a number, create a leaf node
        if token.isdigit():
            nodes.append(Node(int(token)))

        # Opening parenthesis is pushed to operator stack
        elif token == '(':
            ops.append(token)

        # Closing parenthesis triggers node creation
        elif token == ')':
            # Build nodes until matching '(' is found
            while ops and ops[-1] != '(':
                make_node(ops, nodes)
            # Remove '(' from stack
            ops.pop()

        # Operator handling with precedence rules
        elif token in precedence:
            # Process operators with higher or equal precedence
            while (ops and ops[-1] in precedence and
                   precedence[ops[-1]] >= precedence[token]):
                make_node(ops, nodes)

            # Push current operator
            ops.append(token)

    # Process remaining operators
    while ops:
        make_node(ops, nodes)

    # Final node is the root of the expression tree
    return nodes[-1]
