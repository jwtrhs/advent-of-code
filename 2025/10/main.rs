use std::collections::{HashSet, VecDeque};
use std::env;
use std::fmt;
use std::fs;

struct Machine {
    indicator: String,
    schematics: Vec<Vec<usize>>,
    joltages: Vec<u32>,
}

impl fmt::Display for Machine {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let schematics: Vec<String> = self
            .schematics
            .iter()
            .map(|b| {
                let buttons = b
                    .iter()
                    .map(|x| x.to_string())
                    .collect::<Vec<String>>()
                    .join(",");
                format!("({})", buttons)
            })
            .collect();
        let joltages: Vec<String> = self.joltages.iter().map(|j| j.to_string()).collect();
        write!(
            f,
            "[{}] {} {{{}}}",
            self.indicator,
            schematics.join(" "),
            joltages.join(",")
        )
    }
}

fn strip(value: &str) -> &str {
    let mut chars = value.chars();
    chars.next();
    chars.next_back();
    chars.as_str()
}

fn apply_button_to_indicator(indicator: &str, schematic: &[usize]) -> String {
    let mut new_indicator: String = String::from(indicator);
    for button in schematic.iter() {
        if new_indicator.chars().nth(*button).unwrap() == '.' {
            new_indicator.replace_range(*button..*button + 1, "#");
        } else {
            new_indicator.replace_range(*button..*button + 1, ".");
        }
    }
    new_indicator
}

fn main() {
    let args: Vec<_> = env::args().collect();
    let data = fs::read_to_string(args[1].clone()).expect("Read input file.");

    let mut machines: Vec<Machine> = Vec::new();
    for line in data.lines() {
        let tok: Vec<&str> = line.split(" ").collect();
        let indicator: String = strip(tok[0]).chars().collect();
        let schematics: Vec<Vec<usize>> = tok[1..tok.len() - 1]
            .iter()
            .map(|x| {
                strip(x)
                    .split(",")
                    .map(|b| b.parse::<usize>().unwrap())
                    .collect()
            })
            .collect();
        let joltages = strip(tok[tok.len() - 1])
            .split(",")
            .map(|x| x.parse::<u32>().unwrap())
            .collect();
        machines.push(Machine {
            indicator,
            schematics,
            joltages,
        });
    }
    // for machine in machines.iter() {
    //     println!("{}", machine);
    // }

    let mut fewest_button_pushes_1: Vec<u32> = Vec::new();
    for machine in machines.iter() {
        let mut queue: VecDeque<(String, u32)> = VecDeque::new();
        let mut visited: HashSet<String> = HashSet::new();
        let first_indicator = ".".repeat(machine.indicator.len());
        queue.push_back((first_indicator.clone(), 0));
        visited.insert(first_indicator.clone());
        while !queue.is_empty() {
            let (indicator, button_pushes) = queue.pop_front().unwrap();
            if *indicator == machine.indicator {
                fewest_button_pushes_1.push(button_pushes);
                break;
            }
            let new_indicators: Vec<String> = machine
                .schematics
                .iter()
                .map(|s| apply_button_to_indicator(&indicator, s))
                .filter(|i| !visited.contains(i))
                .collect();
            for ind in new_indicators {
                queue.push_back((ind.clone(), button_pushes + 1));
                visited.insert(ind.clone());
            }
        }
    }
    println!("Part 1: {}", fewest_button_pushes_1.iter().sum::<u32>());
}
