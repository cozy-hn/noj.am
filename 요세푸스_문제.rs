use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let nums: Vec<usize> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (n, k) = (nums[0], nums[1]);

    let mut q: Vec<usize> = (1..=n).collect();
    let mut ans: Vec<usize> = Vec::new();
    let mut idx: usize = k - 1;

    while !q.is_empty() {
        ans.push(q.remove(idx));
        if !q.is_empty() {
            idx = (idx + k - 1) % q.len();
        }
    }

    println!("<{}>", ans.iter().map(usize::to_string).collect::<Vec<String>>().join(", "));
}
