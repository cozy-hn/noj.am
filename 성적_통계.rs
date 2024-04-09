use std::io::{self, Read};
use std::fmt::{Write};
use std::cmp::max;

fn main() {
	let mut input = String::new();
	let mut output = String::new();
	io::stdin().read_to_string(&mut input).unwrap();
	let mut iter = input.split_whitespace();
	let n: usize = iter.next().unwrap().parse().unwrap();
	for i in 1..n+1 {
		writeln!(output, "Class {}", i).unwrap();
		let m: usize = iter.next().unwrap().parse().unwrap();
		let mut scores: Vec<usize> = Vec::with_capacity(m);
		for _ in 0..m {
			scores.push(iter.next().unwrap().parse().unwrap());
		}
		scores.sort();
		let mut gap = scores[1] - scores[0];
		for i in 1..m-1 {
			gap = max(gap, scores[i+1] - scores[i]);
		}
		writeln!(output, "Max {}, Min {}, Largest gap {}", scores[m-1], scores[0], gap).unwrap();
	}
	print!("{}", output);
}