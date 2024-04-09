use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut input = String::new();
    stdin.read_line(&mut input).unwrap();
    let mut parts = input.trim().split_whitespace();
	let n: usize = parts.next().unwrap().parse().unwrap();
	let m: usize = parts.next().unwrap().parse().unwrap();

    input.clear();
    stdin.read_line(&mut input).unwrap();
    let j: usize = input.trim().parse().unwrap();

    let mut move_cnt = 0;
    let mut pos = 1;

    for _ in 0..j {
        input.clear();
        stdin.read_line(&mut input).unwrap();
        let apple: usize = input.trim().parse().unwrap();

        if pos <= apple && apple < pos + m {
            continue;
        }
        if pos > apple {
            move_cnt += pos - apple;
            pos = apple;
        } else if pos + m <= apple {
            move_cnt += apple - (pos + m - 1);
            pos = apple - (m - 1);
        }
    }

    println!("{}", move_cnt);
}
