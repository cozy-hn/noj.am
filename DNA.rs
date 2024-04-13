use std::io::{self, Read};
use std::collections::HashMap;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();

    let mut lines = input.lines();
    let first_line = lines.next().unwrap();
    let mut parts = first_line.split_whitespace();
    let n: usize = parts.next().unwrap().parse().unwrap();
    let m: usize = parts.next().unwrap().parse().unwrap();

    let dna: Vec<&str> = lines.collect();

    let mut result = String::new();
    let mut dist = 0;

	let mut counts = HashMap::new();
    for i in 0..m {
		counts.clear();
		counts.insert('A', 0);
		counts.insert('C', 0);
		counts.insert('G', 0);
		counts.insert('T', 0);

        for dna_str in &dna {
            *counts.get_mut(&dna_str.chars().nth(i).unwrap()).unwrap() += 1;
        }

        let max_value = *counts.values().max().unwrap();
        dist += n - max_value;

        let mut sorted_keys: Vec<char> = counts.keys().copied().collect();
        sorted_keys.sort();

        for key in sorted_keys {
            if counts[&key] == max_value {
                result.push(key);
                break;
            }
        }
    }

    println!("{}\n{}", result, dist);
}