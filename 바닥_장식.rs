use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();

    let mut lines = input.lines();
    let first_line = lines.next().unwrap();
    let (n, m) = {
        let mut iter = first_line.split_whitespace().map(|x| x.parse::<usize>().unwrap());
        (iter.next().unwrap(), iter.next().unwrap())
    };

    let mut maze: Vec<Vec<char>> = lines.map(|line| line.chars().collect()).collect();
    let mut ans = 0;

    for i in 0..n {
        for j in 0..m {
            if maze[i][j] == '-' {
                ans += 1;
                for k in j..m {
                    if maze[i][k] == '-' {
                        maze[i][k] = '.';
                    } else {
                        break;
                    }
                }
            } else if maze[i][j] == '|' {
                ans += 1;
                for k in i..n {
                    if maze[k][j] == '|' {
                        maze[k][j] = '.';
                    } else {
                        break;
                    }
                }
            }
        }
    }
    println!("{}", ans);
}
