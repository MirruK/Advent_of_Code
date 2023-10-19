fn traverse_slope(steps: (usize, usize)) -> anyhow::Result<i32> {
    let data: &str = include_str!("./input.txt");
    let my_vec = data.split("\n").collect::<Vec<&str>>();
    let mut row_index = 0;
    let mut row_number = 0;
    let mut trees = 0;
    while row_number < my_vec.len() {
        let row = my_vec.get(row_number).unwrap();
        match row.chars().nth(row_index) {
            Some('#') => {
                trees += 1;
            }
            None => {
                println!("Row index out of row with val: {}", row_index)
            }
            _ => {}
        }
        row_index = (row_index + steps.0) % row.len();
        row_number += steps.1;
    }
    Ok(trees)
}

fn main() {
    println!("{}", traverse_slope((3, 1)).unwrap());
    let steps: [(usize, usize); 5] = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)];
    let values = steps
        .iter()
        .map(|s| i64::from(traverse_slope(*s).unwrap()))
        .product::<i64>();
    //.fold(i64::from(1), |acc, f| i64::from(f) * acc);
    println!("{}", values);
}
