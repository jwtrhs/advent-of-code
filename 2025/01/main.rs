use std::env;
use std::fs;

fn main() {
    let args: Vec<_> = env::args().collect();
    let data = fs::read_to_string(args[1].clone()).expect("Read input file.");
    let lines = data.split("\n");

    let mut position = 50;
    let mut count1 = 0;
    let mut count2 = 0;
    for line in lines.collect::<Vec<_>>() {
        if line.is_empty() {
            continue;
        }
        let direction = line.chars().nth(0).expect("Input is valid.");
        let distance = line[1..].parse::<i32>().unwrap();
        for _ in 0..distance {
            let offset = match direction {
                'R' => 1,
                _ => -1,
            };
            position = (position + offset) % 100;
            if position == 0 {
                count2 += 1;
            }
        }
        if position == 0 {
            count1 += 1;
        }
    }

    println!("Part 1: {}", count1);
    println!("Part 2: {}", count2);
}
