use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();

    let mut lines = input.trim().split('\n').skip(1);

    let tips_iter = lines.map(|line| line.parse::<i32>().unwrap());

    let mut tips: Vec<i32> = tips_iter.collect();
    tips.sort_unstable_by(|a, b| b.cmp(a));

    let mut total_tips : i64 = 0;
    let mut rank = 0;

    for tip in tips {
        let adjusted_tip = tip - rank;
        if adjusted_tip > 0 {
            total_tips += adjusted_tip as i64;
            rank += 1;
        } else {
            break;
        }
    }
    println!("{}", total_tips);
}
