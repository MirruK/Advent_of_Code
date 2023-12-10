use std::{collections::HashMap, iter::Cycle, str::Chars};

fn gcd(a: u64, b: u64) -> u64 {
    let mut x = a;
    let mut y = b;
    while y != 0 {
        let temp = y;
        y = x % y;
        x = temp;
    }
    x
}

fn lcm(a: u64, b: u64) -> u64 {
    if a == 0 || b == 0 {
        0
    } else {
        (a * b) / gcd(a, b)
    }
}

fn lcm_multiple(numbers: &[u64]) -> u64 {
    if numbers.is_empty() {
        return 0;
    }

    let mut result = numbers[0];
    for &num in &numbers[1..] {
        result = lcm(result, num);
    }
    result
}

fn parse_input(inp: &str) -> HashMap<String, (String, String)> {
    let mut lines = inp.lines();
    lines.next(); // Throw away the line with "RLRLRL"
    lines.next(); // Throw away the empty second line
    let mut nodes: HashMap<String, (String, String)> = HashMap::new();
    for line in lines {
        let curr_node: (String, (String, String)) = (
            line.get(0..=2).unwrap().into(),
            (
                line.get(7..=9).unwrap().into(),
                line.get(12..=14).unwrap().into(),
            ),
        );
        nodes.insert(curr_node.0, curr_node.1);
    }
    return nodes;
}

fn traverse_network(
    nodes: &HashMap<String, (String, String)>,
    start: &String,
    destination: &String,
    dist: u64,
    direction_iter: &mut Cycle<Chars<'_>>,
) -> u64 {
    if start.ends_with(destination) {
        return dist;
    }
    let next_node = match direction_iter.next() {
        Some('L') => &nodes.get(start).unwrap().0,
        Some('R') => &nodes.get(start).unwrap().1,
        _ => panic!("Abc"),
    };
    return traverse_network(nodes, &next_node, destination, dist + 1, direction_iter);
}

fn main() {
    let inp_file = include_str!("input.txt");
    let mut lines = inp_file.lines();
    let mut first_line_cycle = lines.next().unwrap().chars().cycle();
    let nodes = parse_input(inp_file);
    let dist = traverse_network(
        &nodes,
        &String::from("AAA"),
        &String::from("ZZZ"),
        0,
        &mut first_line_cycle,
    );
    let mut cloned_cycle = first_line_cycle.clone();
    let start_nodes: Vec<&String> = nodes.keys().filter(|k| k.ends_with("A")).clone().collect();
    let mut dists = vec![];
    for node in start_nodes {
        dists.push(traverse_network(
            &nodes,
            node,
            &String::from("Z"),
            0,
            &mut cloned_cycle,
        ))
    }
    println!("Part 1 --> {}", dist);
    println!("Part 2 --> {:?}", lcm_multiple(dists.as_slice()));
}
