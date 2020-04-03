open SimUtil

let ngram_n = 4
(* Your code goes here: *)

(* Define the function that lower-cases and filters out non-alphabetic characters *)
let filter_chars s =
  String.map (fun c -> match c with
      'a'..'z' | 'A'..'Z' -> Char.lowercase_ascii c
      | _ -> ' ') s


(* extract a list of n-grams from a string, naively *)
let ngrams n s =
  List.init ((String.length s)-n+1) (fun i -> String.sub s i n)

(* Define the function that converts a string into a list of "normalized" n-grams *)
let n_grams s =
  List.filter (fun e -> not (String.contains e ' ')) (ngrams 4 (filter_chars s))

(* Define a function to convert a list into a bag *)
let bag_of_list lst =
(* for function 'fun': if there's no such element e in acc then add it, the initial
  multiplicity is 1, else plus one to its multiplicity*)
  List.fold_left (fun acc e -> if (List.assoc_opt e acc) = None
    then ((e,1)::acc) else ((e,(List.assoc e acc)+1)::(
    List.remove_assoc e acc))) [] lst

(* Bag utility functions *)

(* multiplicity of e in bag b - 0 if not in the bag *)
let multiplicity e b = match List.assoc_opt e b with
  | None -> 0
  | Some n -> n

(* size of a bag is the sum of the multiplicities of its elements *)
let size b = List.fold_left (fun acc x -> acc+(snd x)) 0 b

(* Define the similarity function between two sets: size of intersection / size of union *)
(* if there's no *)
let intersection_size s1 s2 = List.fold_left (fun acc x ->
  (min (multiplicity (fst x) s1) (multiplicity (fst x) s2))+acc) 0 s1
let union_size s1 s2 = List.fold_left (fun acc x ->
  (max (multiplicity (fst x) s2) (multiplicity (fst x) s2))+acc) 0 s1
let similarity s1 s2 = (float_of_int (intersection_size s1 s2)) /. (float_of_int (union_size s1 s2))

(* Find the most similar representative file *)
let find_max repsims repnames = List.fold_left (fun acc x -> if max x acc = x then x else acc) (0.,"") (List.combine repsims repnames)


let main all replist_name target_name =
  (* Read the list of representative text files *)
  let repfile_list = file_lines replist_name in
  (* Get the contents of the repfiles and the target file as strings *)
  let rep_contents = List.map file_as_string repfile_list in
  let target_contents = file_as_string target_name in
  (* Compute the list of normalized n-grams from each representative *)
  let rep_ngrams = List.map n_grams rep_contents in
  (* Convert the target text file into a list of normalized n-grams *)
  let target_ngrams = n_grams target_contents in
  (* Convert all of the stem lists into stem sets *)
  let rep_bags = List.map bag_of_list rep_ngrams in
  let target_bag = bag_of_list target_ngrams in
  (* Compute the similarities of each rep set with the target set *)
  let repsims = List.map (similarity target_bag) rep_bags in
  let (sim,best_rep) = find_max repsims repfile_list in
  let () = if all then
  (* print out similarities to all representative files *)
  let () = print_endline "" in
  () else begin
  (* Print out the winner and similarity *)
  let () = print_endline "" in
  print_endline ""  end in
  (* this last line just makes sure the output prints before the program exits *)
  flush stdout
