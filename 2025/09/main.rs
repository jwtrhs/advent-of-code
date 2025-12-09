use std::env;
use std::fs;

struct Point {
    x: i64,
    y: i64,
}

fn main() {
    let args: Vec<_> = env::args().collect();
    let data = fs::read_to_string(args[1].clone()).expect("Read input file.");

    let points: Vec<Point> = data
        .lines()
        .map(|x| x.trim())
        .map(|s| {
            let coords: Vec<&str> = s.split(",").collect();
            Point {
                x: coords[0].parse::<i64>().unwrap(),
                y: coords[1].parse::<i64>().unwrap(),
            }
        })
        .collect();

    let mut largest_area: i64 = 0;

    for a in points.iter() {
        for b in points.iter() {
            let area = ((a.x - b.x).abs() + 1) * ((a.y - b.y).abs() + 1);
            if area > largest_area {
                largest_area = area;
            }
        }
    }

    println!("Part 1: {largest_area}");
}
