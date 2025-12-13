use std::env;
use std::fmt;
use std::fs;

struct Shape {
    index: u32,
    shape: Vec<Vec<char>>,
}

impl Shape {
    fn from_input(input: &[&str]) -> Shape {
        let mut iter = input.iter();
        let index = iter
            .next()
            .unwrap()
            .strip_suffix(":")
            .unwrap()
            .parse::<u32>()
            .unwrap();
        let shape: Vec<Vec<char>> = iter.map(|x| x.chars().collect()).collect();

        Shape { index, shape }
    }
}

impl fmt::Display for Shape {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "{}:\n{}",
            self.index,
            self.shape
                .iter()
                .map(|x| x.iter().collect::<String>())
                .collect::<Vec<String>>()
                .join("\n"),
        )
    }
}

struct Grid {
    width: u32,
    height: u32,
    quantities: Vec<u32>,
}

impl Grid {
    fn from_input(input: &str) -> Grid {
        let mut first_iter = input.split(": ");
        let mut width_height = first_iter.next().unwrap().split("x");
        let width = width_height.next().unwrap().parse::<u32>().unwrap();
        let height = width_height.next().unwrap().parse::<u32>().unwrap();
        let quantities = first_iter
            .next()
            .unwrap()
            .split(" ")
            .map(|x| x.parse::<u32>().unwrap())
            .collect();

        Grid {
            width,
            height,
            quantities,
        }
    }
}

impl fmt::Display for Grid {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "{}x{}: {}",
            self.width,
            self.height,
            self.quantities
                .iter()
                .map(|x| x.to_string())
                .collect::<Vec<String>>()
                .join(" ")
        )
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let data = fs::read_to_string(&args[1]).expect("Read input file.");

    let mut shapes: Vec<Shape> = Vec::new();
    let mut grids: Vec<Grid> = Vec::new();

    let lines: Vec<&str> = data.lines().collect();
    let mut i: usize = 0;
    while i < lines.len() {
        if lines[i].ends_with(":") {
            let mut shape_lines: Vec<&str> = Vec::new();
            while !lines[i].is_empty() {
                shape_lines.push(lines[i]);
                i += 1;
            }
            shapes.push(Shape::from_input(&shape_lines));
        } else {
            grids.push(Grid::from_input(lines[i]));
        }
        i += 1;
    }

    for shape in shapes {
        println!("{}\n", shape);
    }
    for grid in grids {
        println!("{}", grid);
    }
}
