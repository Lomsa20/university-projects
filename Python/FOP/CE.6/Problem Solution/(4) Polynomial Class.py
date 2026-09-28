class Polynomial:
    def __init__(self, coeffs):
        # Store coefficients, where coeffs[i] is the coefficient for x^i
        self._coeffs = coeffs

    def __add__(self, other):
        """Overloads the '+' operator for polynomial addition."""
        max_len = max(len(self._coeffs), len(other._coeffs))

        # Pad the shorter list(s) with zeros to match the length of the longest one
        a = self._coeffs + [0] * (max_len - len(self._coeffs))
        b = other._coeffs + [0] * (max_len - len(other._coeffs))

        # Add corresponding coefficients using zip()
        return Polynomial([x + y for x, y in zip(a, b)])

    def __mul__(self, other):
        """Overloads the '*' operator for polynomial multiplication."""
        # The result length is sum of lengths - 1
        res = [0] * (len(self._coeffs) + len(other._coeffs) - 1)

        # Iterate through every term in the first polynomial (p1)
        for i, a_coeff in enumerate(self._coeffs):
            # Iterate through every term in the second polynomial (p2)
            for j, b_coeff in enumerate(other._coeffs):
                # The product of a*x^i and b*x^j is (a*b)*x^(i+j)
                # We add the product (a_coeff * b_coeff) to the result coefficient at index i + j
                res[i + j] += a_coeff * b_coeff

        return Polynomial(res)

    def __str__(self):
        """Formats the polynomial for human-readable output."""
        # Filters out zero coefficients and formats non-zero terms (e.g., '1x^0 + 2x^1')
        return " + ".join(f"{c}x^{i}" for i, c in enumerate(self._coeffs) if c)


class NamedPolynomial(Polynomial):
    """Derived class that adds a label to the polynomial."""

    def __init__(self, name, coeffs):
        super().__init__(coeffs)
        self._name = name

    def __str__(self):
        """Overrides __str__ to include the name before the polynomial expression."""
        return f"{self._name}: {super().__str__()}"


# --- Corrected Example Usage ---

# Define p1: Represents 1 + 2x + 3x^2 (Coefficients must be numbers!)
p1 = NamedPolynomial("P1", [1, 2, 3])

# Define p2: Represents 4 + 5x (Coefficients must be numbers!)
p2 = NamedPolynomial("P2", [4, 5])

print(p1)
print(p2)
print("---")
print(f"Addition (P1 + P2): {p1 + p2}")
print(f"Multiplication (P1 * P2): {p1 * p2}")