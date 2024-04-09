use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();

    let mut numbers = input.lines();
    let N :i32= numbers.next().unwrap().trim().parse().unwrap();
    let mut lst: Vec<i32> = numbers
        .map(|line| line.trim().parse::<i32>().unwrap())
        .collect();

    lst.sort_unstable_by(|a, b| b.cmp(a));

    let mut ans = 0;
    for (i, &value) in lst.iter().enumerate() {
        ans = std::cmp::max(ans, value * (i as i32 + 1));
    }

    println!("{}", ans);
}
