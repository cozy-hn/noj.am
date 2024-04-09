use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let n: i32 = input.trim().parse().unwrap();

    let mut max = 0;
    let mut ans_li: Vec<i32> = Vec::new();

    for i in 1..=n {
        let mut tmp_li: Vec<i32> = vec![n, i];
        let mut next_num = n - i;
        let mut cnt = 2;

        while next_num >= 0 {
            tmp_li.push(next_num);
            let len = tmp_li.len();
            next_num = tmp_li[len - 2] - tmp_li[len - 1];
            cnt += 1;
        }

        if cnt > max {
            max = cnt;
            ans_li = tmp_li;
        }
    }

    println!("{}", max);
    for num in ans_li {
        print!("{} ", num);
    }
    println!();
}
