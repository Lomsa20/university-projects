def flatten(xs): #flatten mean that if list has nested lists it will convert them into one list
    if not xs:
        return []
    head, *tail = xs
    if isinstance(head, list):
        return flatten(head) + flatten(tail)
    else:
        return  [head]+ flatten(tail)
print(flatten([1, 2, [3, 4]]))
  









