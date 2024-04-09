use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut iterator = stdin.lock().lines();
    
    let n: i32 = iterator.next().unwrap().unwrap().trim().parse().unwrap();
    let mut ans: i32 = 0;
    for _ in 0..n {
        let num: i32 = iterator.next().unwrap().unwrap().trim().parse().unwrap();
        ans += num;
    }
    println!("{}", ans - n + 1);
}