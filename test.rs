use std::collections::HashMap;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
	let mut lines = input.lines();
    let mut dic: HashMap<String, u32> = HashMap::new();
	let mut n : u32 = lines.next().unwrap().parse().unwrap();
	for _ in 0..n {
		let line = lines.next().unwrap();
		*dic.entry(line.to_string()).or_insert(0) += 1;
	}

    if let max = dic.values().max().unwrap() { 
        let max = *max;

        let mut arr: Vec<String> = dic
            .into_iter()
            .filter(|&(_, v)| v == max)
            .map(|(k, _)| k)
            .collect();

        arr.sort_unstable();
        println!("{}", arr[0]);
    }
}
