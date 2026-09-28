1.(*Go Through List at last*)
let rec last = function
  | [] -> None
  | [x] -> Some x
  | _ :: t -> last t;;
(*ignore head go recursion at tail*)
2.(*Go Through List at last two*)
let rec last_two = function
  |[] -> None
  |[x; y] -> Some (x, y)
  |_ :: t -> last_two t;;
(*If list is [1] so one element 
it returns None and if there is 
atleast two it will return last two*)
3.(*N'th Element of a List*)
let rec nth n = function
  |[] -> None
  |h :: t -> if n = 0 then Some h else nth (n-1)t;;
(*h :: t means head to tail and n = 0 
we return head and otherwise recursion
happend until we get nth number and
to happen that (n-1) t that tail 
shrinks by 1 element*)

(*additional Factorial Calculation*)
let rec fac n = 
  if n < 2 then 1 
  else n * fac(n-1);;

4.(*lenght of list*)
let rec lenght n = function [ 1, 2, 3,4 ]   
  |[] -> n
  |_ :: t -> lenght(n+1)t;;

5.(*Reverse a List*)
let rec rev acc = function
  |[] -> acc
  |h :: t -> rev (h :: acc) t;;
(*
rev []    [1;2;3]  →  rev [1]    [2;3]
rev [1]   [2;3]    →  rev [2;1]  [3]
rev [2;1] [3]      →  rev [3;2;1] []
rev [3;2;1] []     →  [3;2;1]*)
(*Additional*)

let rec foo  x y b = 
  let x,y = if x > y then y,x else x,y in
  let rec loop x y b = 
    if x >= y then x
    else if b then loop (x+1) y (not b)
    else loop x (y-1) (not b)
  in 
  loop x y b;;




let rec last = function
  |[] -> None
  |[x] -> Some x
  |_ :: t -> last t

let rec last_two = function
  |[] | [_] -> None
  |[x; y] -> Some (x, y)
  |_ :: t -> last_two t

let rec nth n = function
  |[] -> None
  |h :: t -> if n = 0 then Some h else nth (n-1) t  

let rec lenght n = function
  |[] -> n
  |_ :: t -> lenght (n+1) t

let rec reverse acc = function
  |[] -> acc 
  |h :: t -> reverse (h:: acc) t

let rec remove_at n = function
  |[] -> []
  |h::t -> if n = 0 then t else h :: remove_at (n-1) t ;; [1, 2,3, 4] 0 -> [2,3,4] 1 -> [1,3,4] 2 -> [1,2,4] 3 -> [1,2,3]

let rec remove_at n = function
  |[] -> []
  |h::t -> if n = 0 then t else h :: remove_at (n-1) t
  
let rec drop n l =
  match n, l with
  |0,_ -> l
  |_,[]-> []
  |n,_::t -> drop (n-1) t 