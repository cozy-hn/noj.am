use std::io;

fn main()	{
	let mut input = String::new();
	io::stdin().read_line(&mut input).unwrap();
	let nums: Vec<i32> = input.split_whitespace().map(|s| s.parse().unwrap()).collect();
	let mut ans = (nums[0] - nums[1]).abs();

	input.clear();
	io::stdin().read_line(&mut input).unwrap();
	let n: i32 = input.trim().parse().unwrap();
	
	for _ in 0..n {
		input.clear();
		io::stdin().read_line(&mut input).unwrap();
		let tmp: i32 = input.trim().parse().unwrap();

		ans = ans.min((nums[1] - tmp).abs()+1);
	}
	println!("{}", ans);
}