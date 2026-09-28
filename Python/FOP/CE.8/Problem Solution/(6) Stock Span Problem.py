def stock_span(prices):
    stack = []          # (price, span)
    result = []

    for price in prices:
        span = 1

        while stack and stack[-1][0] <= price:
            span += stack.pop()[1]

        stack.append((price, span))
        result.append(span)

    return result


prices = list(map(int, input("Enter stock prices separated by space: ").split()))
print(stock_span(prices))
