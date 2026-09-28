(*What is a lazy list?*)
(*A lazy list is a list where elements are computed only when needed.*)
(*This is useful when working with infinite lists or when the computation of elements is expensive.*)

(*In OCaml, we can define a lazy list using a recursive data structure.*)

type 'a lazy_list = Cons of 'a * (unit -> 'a lazy_list)
(*Which we can read like this Cons(value, Function) in function part 
we can write a any function that returns new value*)

1.(*e.g. we want to create a lazy list of natural numbers*)
let rec lnat n = Cons(n, fun() -> lnat(n+1))
(*Explanation of each element in Cons()
n is value which we need to return now and next time and fun() is some kind of freezer 
which will freeze the next element until we call it 
and lnat(n+1) is just the next element which will be replace in Cons(n, fun()-> ...)*)

(*Now we can create a lazy list of natural numbers starting from 0*)

2.(*Next example*)
(*ltake which means take the first n elements from a lazy list*)
let rec ltake n (Cons(a,next)) = 
    match n with 
    |0 -> []
    |_ -> a :: ltake (n-1)(next())
(*using cases*)
let rec ltake n (Cons(a,next)) =
    if n = 0 then []
    else a:: ltake (n-1)(next())
(*using if/else*)
(*Explanation:*)
(*here when we enter (n) its mean how many elements we want to take 
and Cons(a,next) is the lazy list with head a and tail next 
next is just function that returns next element 
if n = 0 then we return an empty list, 
otherwise we return a:: ltake (n-1)(next()) where it goes through head a to n-1 elements 
and freezes the rest element using next()
*)

3.(*lfilter*)
let rec lfilter p (Cons(a,next)) =
  if p a then Cons(a, fun() -> lfilter p (next()))
  else lfilter p (next())
(*Explanation:*)
(*lfilter takes a predicate function p and a lazy list Cons(a,next) 
and returns a new lazy list that contains only the elements of the original list that satisfy the predicate p.*)
(*If the head a satisfies the predicate p, we include it in the new lazy list 
and recursively call lfilter on the tail next() to filter the rest of the list.*)
(*If the head a does not satisfy the predicate p, we simply skip it and recursively call lfilter on the tail next()
 to continue filtering the rest of the list.*)
4.(*ldrop*)
let rec ldrop n (Cons(a,next))= 
  match n with 
  |0 -> Cons(a,next)
  |_ -> ldrop(n-1)(next())
(*Case Example*)
let rec ldrop n (Cons(a,next)) = 
  if n = 0 then Cons(a,next)
  else ldrop (n-1)(next())
(*Explanation:*)
(*ldrop takes a number n and a lazy list Cons(a,next) and 
returns a new lazy list that drops the first n elements of the original list.*)
(*If n is 0, we return the original lazy list Cons(a,next)
 because we don't need to drop any elements.*)
(*If n is greater than 0, we recursively call ldrop on the tail next()
 to drop the first element and decrease n by 1 until we have dropped n elements.*)
5.(*Lmap*)
let rec lmap f Cons(a,next) = Cons(f a, fun() -> lmap f (next()))
(*Explanation:*)
(*lmap takes a function f and a lazy list Cons(a,next) 
and returns a new lazy list that applies the function f to each element*)
(*lmap f (next()) this where magic happens and 
every next element is applied with function f*)

6.(*Fibonacci*)
let rec lfib () =
  let rec aux a b = Cons(a, fun() -> aux b (a + b)) in
  aux 0 1
(*With Helper Function*)
let rec fib a b  = Cons(a, fun() -> fib b (a + b))
(*Without Helper Function*)
(*Explanation: *)
(*lfib takes no arguments*)

7.(*Lazy Tree: Layerd Tree*)
let rec layer_tree n = LNode(n, fun() -> layer_tree (n+1), fun() -> layer_tree (n+1))
(*Explanation:*)
(*layer_tree takes a number n and returns a lazy tree 
where each node contains the value n and has two children that are also lazy trees.*)
(*The left child is created by recursively calling layer_tree with n+1, 
and the right child is also created by recursively calling layer_tree with n+1.*)
(*This creates an infinite binary tree where each level contains the same value n, 
and the values increase as we go down the tree.*)
8.(*Interval Tree*)
let rec interval_tree a b = 
    LNode((a,b), fun() -> interval_tree a ((a+b)/.2.0), fun() -> interval_tree ((a+b)/.2.0) b)
(*Explanation:*)
(*interval_tree takes two numbers a and b and returns
 a lazy tree where each node contains the interval (a,b) 
 and has two children that are also lazy trees.*)
(*and using a((a+b)/2.0) it work on left side and b((a+b)/2.0) it work on right side*)

(**)
9.let rec top n t = 
    match t with
    |LNode(a,l,r) -> if n = 0 then Leaf else Node(a, top (n-1) (l()), top (n-1) (r()))

10. let rec lzip f (Cons(a,next_a)) (Cons(b,next_b)) = 
    Cons(f a b, fun() -> lzip f (next_a()) (next_b()))
(*Explanation:*)
(*lzip takes a function f and two lazy lists Cons(a,next_a) and Cons(b,next_b)