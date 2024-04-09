use std::io;

fn two_pointer(n: i32) -> i32
{
    let mut count = 0;
    let mut left_pos = 1;

    let mut cur_sum = 0;
    for right_pos in 1..=n / 2 + 1 
    {
        cur_sum += right_pos;

        while cur_sum >= n 
        {
            if cur_sum == n 
            {
                count += 1;
            }

            cur_sum -= left_pos;
            left_pos += 1;
        }
    }

    count
}

fn main()
{
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let n: i32 = input.trim().parse().expect("Please type a number!");

    let mut result = two_pointer(n);
    if n == 1 || n == 2
    {
        result = 0;
    }
    println!("{}", result + 1);
}
