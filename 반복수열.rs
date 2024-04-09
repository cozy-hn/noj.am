use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let mut parts = input.trim().split_whitespace();
    let n = parts.next().unwrap();
    let p: u32 = parts.next().unwrap().parse().unwrap();

    let mut sequence = Vec::new();
    sequence.push(n.to_string());

    loop {
        let last = sequence.last().unwrap();
        let new_value = last.chars()
            .map(|c| c.to_digit(10).unwrap().pow(p) as i32)
            .sum::<i32>()
            .to_string();

        if sequence.contains(&new_value) {
            println!("{}", sequence.iter().position(|x| x == &new_value).unwrap());
            break;
        }
        sequence.push(new_value.clone());
    }
}
