1. reverse X 10/10
2. append list X 8/10
3. factorial X 10/10
4. fibonacci X - 10/10
5. length of list X 10/10 [1,2,3,4] -> 4 []-> 0
6. drop X 7/10
7. take X 1/10
8. odd_elements X 8/10
9. filter X -
10. fold_right - 
11. Tree size
12. Tree Flatten
14. Leave Counter
13. Tree insertion
14. Tree removal
15. Tree cosntruction
16. Tree traversal
17. list all leaves(not Nodes but only leafs) in a tree
18. All Internal Nodes in tree
19. lookup in tree
20. Maping
21. fold_left
22. fold_right
23. lnatural
24. ltake from llist
25. lfilter from llist
26. layer ltree
27. update tree
28. Insert new tree

let subtree = Node(xsize,xlsize,xl,xr)
28.let rec insert t i subtree =
    match t with 
    |Leaf a -> 
        if i = 0 then Node(1+xsize,xlsize,Leaf a, subtree )
        else if i = 1 then Node(1+xsize,1,subtree,Leaf a)
        else raise(Failure "Index out of bound")
    |Node(size,lsize,l,r) -> if i< lsize then 
        Node(size+xsize,lsize+xlsize,insert l i subtree,r)
        else Node(size+xsize,lsize,l,insert r (i-lsize) subtree)
27.let rec update t i x =
    match t with
    |leaf a -> if  i = 0 then x else failwith "Index out of bound"
    ||Node(size,lsize,l,r) -> 
        if i<0 || i >size then t
        else if i <lsize then 
        Node(size,lsize,update l i x,r)
        else
        Node(size,lsize,l,update r (i-lsize) x)

13.let rec insert t i x = 
  match t with 
    |Leaf _ -> 
        if i =0 then Node(2, 1, Leaf x, t)
        else if 
            Node(2, 1, t, Leaf x) else raise(Failure"Index out of bound") 
    |Node(size, lsize, lt,rt) ->
        if i < lsize then 
            Node(size + 1, lsize +1, insert lt i x, rt)
        else
            Node(size + 1, lsize, lt, insert rt (i-lsize) x)


26.let rec layer_tree n = 
    LNode(n, fun() -> layer_tree (n+1),
     fun() -> layer_tree (n+1))

(*Tail recursion is when the recursive call is the last 
operation in the function — nothing happens after it returns.*)

25. let rec lfilter p (Cons(a,nexxt)) = 
    if p a then Cons(a, fun() -> lfilter p (next()))
    else lfilter p(next())

24.let rec ltake n (Cons(a, next)) = 
    match n with 
    |0 -> []
    |_ -> a :: ltake (n-1)(next())
(*here its take all element and its eventualy freeze memory and 
then we enter some number and its recursively returns all its past elements*)
23. let rec lnat n = Cons(n, fun() -> lnat (n+1)) 
(*type__lnat: int -> int llist*)
(*it takes all natural numbers starting from n and goes to infinite *)

21.let rec fold_left f acc = function
    |[] -> acc 
    |h:: t -> fold_left f (f acc h) t
(*fold_left: *)



(*Mapping: applying a function to each element of a list *)
20.let rec map f= function
|[] -> []
|h ::t -> f h :: map f t (*it goes thruogh list and applies f(function) to each element*)
(*e.g. map (fun x -> x * 2) [1;2;3] = [2;4;6]*)

                                        
19.let rec lookup t i =
    match t with 
    |Leaf a -> 
        if i = 0 then
            a 
        else 
            None
    |Node(size, Lsize, l, r) -> 
        if i < lsize then
            lookup l i
        else 
            lookup r (i - lsize)


18.let rec Internal_Nodes t = let rec doit t acc = 
    match t with 
    |Empty -> acc 
    |Node(a,Empty, Empty) -> acc
    |Node(a,l,r) -> let acc = doit r acc 
in doit l (a::acc) in doit t []



17.let rec Leaves_in_List t = let rec doit t acc = 
    match t with 
    |Empty -> acc
    |Node(a,Empty,Empty) -> a::acc 
    |Node(_,l,r) -> let acc = doit r acc 
        in doit l acc 
    in doit t []

14.let rec leave_counter = function
    |Empty > 0
    | Leaf _ -> 1
    |Node(l,r) -> leave_counter l + leave_counter r

12.let rec flatten t =
    let rec doit t xs = (*xs is accumulator that start with []  *)
    match t with 
    |leaf x -> x:: xs (*here if leaf x then insert it to accumulator which is [] using :: *)
    |Node(l,r) -> 
        let xs = doit r xs (*append the flattened right subtree to the accumulator*)
    in doit l xs (*then append the flattened left subtree to the result of flattening the right subtree*)
in doit t [] (*finally return everything we have into list*)


12.let rec flatten = function
    |Leaf n -> [n]
    |Node(l,r) -> flatten l @ flatten r

11.let rec size = function
    |Leaf _ -> 1 (*Leaf _ means that it can be any value e.g Leaf 120*)
    |Node (l, r) -> size l + size r 


[1;2;3;4] ->  2 4 -> [1;3]
9.let rec filter p  = 
    match l with 
    | [] -> []
    | h:: t -> if p h then h :: filter p t else filter p t

filter [1;2;3;4] p = even 
→ 1 even? no  → filter [2;3;4]
→ 2 even? yes → 2 :: filter [3;4]
→ 3 even? no  → filter [4]
→ 4 even? yes → 4 :: filter []
→ [4] [2]
result = [2;4]


8.let rec odd_elements l= 
    match l with
    | [] -> []
    | [x] -> [x]
    | h::_::t -> h :: odd_elements t
7.let rec take n l = 
    match n, l with
    | 0, _ -> []
    | _, [] -> []
    | n, h :: t -> h :: take (n-1) t
6.let rec drop n l =
    match n , l with
    | 0,_ -> l
    | _,[] -> [] 
    | n,_ :: t -> drop (n-1) t

5.let rec length l = 
    match l with 
    | [] -> 0
    | _ :: t -> 1 + length t 
1.let rec rev l = 
    match l with 
    | [] -> []
    | [x] -> [x]         
    | h :: t -> rev t @ [h] 
2.let rec append l1 l2 =
    match l1 with  
    | [] -> l2
    | h::t -> h :: append t l2
3.let rec fact n =  
    match n with
    | 0 -> 1
    | _ -> n * fact (n-1)
4.let rec fib n =
    match n with 
    | 0 -> 0
    | 1 -> 1
    | _ -> fib (n-1) + fib (n-2)
9.let rec filter p = function
  | [] -> []
  | h :: t -> if p h then h :: filter p t else filter p t
let filter p l = list.fold_right(fun x a -> if p x then x::a else a) l [];; 
[1;2;3;4;5] 1 + 2 + 3 + 4 + 5 = 15

fold_left (fun acc x -> if List.length x > List.length acc than x else acc) [] [[1;2];[3;4;5];[6]]

fold_left(fun acc (a,b) -> (b,a) :: acc) [] [(1,2);(3,4);(5,6)](*Reverse list*)
fold_left(fun acc x -> acc @ (b,a)) [] [(1,2);(3,4);(5,6)](*Reverse list but not efficient because of @*)