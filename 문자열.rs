use std::cmp;
use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let inputs: Vec<&str> = input.trim().split_whitespace().collect();
    let (s1, s2) = (inputs[0], inputs[1]);
    let (l1, l2) = (s1.len(), s2.len());
    let mut ans = l2;

    for i in 0..=l2 - l1 {
        let mut tmp = l1;
        for j in 0..l1 {
            if s1.chars().nth(j) == s2.chars().nth(i + j) {
                tmp -= 1;
            }
        }
        ans = cmp::min(ans, tmp);
    }

    println!("{}", ans);
}
