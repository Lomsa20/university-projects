int foo(int x, int y, bool b) {
    if(x > y) {
        int t = x;
        x = y;
        y = t;
    }
    while(x < y) {
        if(b) {
            ++x;
        } else {
            --y;
        }
        b = !b;
    }
    return x;
}






let foo x y b =
  let x,y = if x > y then y,x else x,y in
  let rec loop x y b =
    if x >= y then x
    else if b then loop (x+1) y (not b)
    else loop x (y-1) (not b)
  in
  loop x y b
  
---------------------------------------------------------------------------

Write a function split : int -> 'a list -> 'a list * 'a list, which takes an integer n, a list l and

    if n < 0, it raises the exception Failure with the error message "The number can not be negative"
    otherwise, returns a pair of lists (l1, l2), where
        l1 is the sublist of l consisting of the first n elements of l,
        l2 is the sublist of l obtained by dropping the first n elements from it

If n is bigger then the length of l, then (l, []) is returned.

let rec take n l=
  match l with 
    []->[]
  |h::t-> if n=1 then [h] else h::take (n-1) t;;


let rec drop n l=
  match l with
    []->[]
  |h::t-> if n=1 then t else drop (n-1) t;;

let rec split n l= 
  if n<0 then raise (Invalid_argument "The number can not be negative")
  else  
    match l with 
      []->([],[])
    |_::_->(take n l, drop n l);;
    
----------------------------------------------------------------------


Write a function check : ('a -> 'b -> bool) -> 'a -> 'b list -> bool, which takes a binary function test, a value v, and a list l and returns true if l contains an element e such that test v e is true. Otherwise it should return false.

let rec check btest v l =
  match l with
    []-> false
  |h::t-> if btest v h then true else check btest v t;; 
