insert new tree
let x = Node(xsize,xlsize,lx,rx)
let rec insert_new_tree t i x =
  match t with
  |Leaf a -> if i = 0 then x else None
  
