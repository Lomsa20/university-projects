Mady By Lomsa

(*This is Excersizes to practise with Tail Recursion*)
(*What you need to do here is to correctly choose which one is tail recursive*)
(*e.g*)
let rec f a =
  match a with
  | [] -> a
  | x::xs -> (x+1)::f xs 
(*This is not tail recursive because the recursive call is not the last operation*)
(*how i now this?*)
(*First we need to find what Function does then trace the execution and finally say that this is not tail recursive*)
(*
[1,2,3] -> [2,3,4]

*)

(* 1 *)
let rec sum_list = function
  | [] -> 0
  | h :: t -> h + sum_list t [1,2,3] 0 -> 0+1 = 1, 1+2 = 3, 3+3 -> 6  no tail recursion
(*[1,2,3] -> *)
(* 2 *)
let rec count acc = function
  | [] -> acc
  | _ :: t -> count (acc + 1) t (*this is tail recursive because the recursive call is the last operation it is mentioned down*)
  (*[1,2,3] acc ->  0+1 = 1 , 1+1 = 2, 2 + 1 = 3, 3+0 ... acc = 3...
  acc = 0 *)

(* 3 *)
let rec power base exp =
  if exp = 0 then 1
  else base * power base (exp - 1)
 exp = 0, base = n -> 1 
 exp != 0 , base = n -> base * power(base, exp-1) -> base * (base * power(base, exp-2)) -> base * (base * (base * power(base, exp-3))) ... no tail recursion
 exp = 4 base = 3 -> 3 * power 3(3) -> 3 * (3 * power 3(2)) -> 3 * (3 * (3 * power 3(1))) -> 3 * (3 * (3 * (3 * power 3(0)))) -> 3 * (3 * (3 * (3 * 1))) -> 81
 this is not tail recursion because power function is called later in the expression and not at the end of the function
 (* 4 *)
let rec flatten = function
  | [] -> []
  | h :: t -> h :: flatten t

(* 5 *)
let rec gcd a b =
  if b = 0 then a
  else gcd b (a mod b)

(* 6 *)
let rec map f = function
  | [] -> []
  | h :: t -> f h :: map f t

(* 7 *)
let rec find acc target = function
  | [] -> acc
  | h :: t ->
      if h = target then find true target t
      else find acc target t

(* 8 *)
let rec depth = function
  | Leaf _ -> 0
  | Node (l, r) -> 1 + max (depth l) (depth r)


Problem 1: List Packing
Implement a function val pack : a list -> a list list = <fun> that
packs consecutive duplicates of list elements into sublists. If a list contains
repeated elements, they should be placed in separate sublists.
Requirement: The function must be tail-recursive.
Examples
• Input: [a; a; a; b; c; c ; a;  a ]
• Output: [[ a ;  a ;  a ]; [ b ]; [ c ;  c]; [a; a]]
• Input: []
• Output: []

let rec pack lst = 
  let rec aux current acc = function
    |[] -> List.rev(if current = [] then acc else current ::acc) First Case(*here if Original list will be emptied and if current is empty return what we have in accumulator 
      or else return everything that is stored in current to  accumulator*)
    |[a]-> List.rev ((a :: current) :: acc) (*same happend here if original list has only one element then insert it in current list and then add this list into accumulator*)
    |x::(y::_ as t) ->  (*here we write that go through all element but when you arrive at the y we just dont care the rest This _ is symbol for that,
     and as t just represent y::_, meaning we can use t with the same value as y::_ here this also means [1,2,3,4] x = 1, y = 2, t = [2,3,4]*)
      if x = y then aux (x::current) acc t (*when we arrive at the same two or more elements we insert all this elements in current list,
         then move this in accumulator here [1,1,2,2,3,4] x::current = (1::[]), acc = [], t = [1,2,2,3,4] *)
      else aux [] ((x::current)::acc) t (*if elements are not the same, we start a new sublist. [1,1,2,2,3,4] ((x::current)::acc) = [[1; 1]; [2; 2]; [3];[4] overall*)
  in aux [] [] lst


Implement a function val flatten : 'a tree -> 'a list that converts a binary tree into a list containing all its elements in left-to-right (in-order) order, 
where the tree type is:
type 'a tree = Leaf | Node of 'a tree * 'a * 'a tree
Requirement: The function must be tail-recursive.
Examples

Input: Node (Node (Leaf, 1, Leaf), 2, Node (Leaf, 3, Leaf))
Output: [1; 2; 3]
Input: Leaf
Output: []
Input: Node (Node (Node (Leaf, 1, Leaf), 2, Leaf), 3, Node (Leaf, 4, Node (Leaf, 5, Leaf)))
Output: [1; 2; 3; 4; 5]



let  flatten t = 
  let rec aux 