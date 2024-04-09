use std::io::{self, Read};
use std::collections::HashSet;

fn main() {
    let stdin = io::stdin();
    let mut buffer = String::new();
    stdin.lock().read_to_string(&mut buffer).unwrap();
    let mut lines = buffer.lines();

    loop {
        let first_line = lines.next().unwrap();
        let parts: Vec<usize> = first_line.split_whitespace()
                                          .map(|s| s.parse().unwrap())
                                          .collect();
        let (n, m) = (parts[0], parts[1]);

        if n == 0 && m == 0 {
            break;
        }

        let mut s1: HashSet<i32> = HashSet::with_capacity(n);
        for _ in 0..n {
            let num = lines.next().unwrap().parse().unwrap();
            s1.insert(num);
        }

        let mut common_count = 0;
        for _ in 0..m {
            let num = lines.next().unwrap().parse().unwrap();
            if s1.contains(&num) {
                common_count += 1;
            }
        }

        println!("{}", common_count);
    }
}
