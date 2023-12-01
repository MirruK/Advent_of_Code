use anyhow;

fn eval_answer(data: &Vec<i64>) -> i64 {
    println!("Data length: {}", data.len());
    let smallest = data.iter().fold(10000000000000, |acc, x| i64::min(acc, *x));
    println!("{}", smallest);
    let mut curr_sum;
    let mut total_skips = 0;
    for i in 0..data.len() {
        for j in 0..data.len() {
            if data[i] == data[j] || data[i] + data[j] + smallest > 2020 {
                total_skips += 1;
                continue;
            }
            curr_sum = 2020 - data[i] - data[j];
            for k in 0..data.len() {
                if data[k] == curr_sum {
                    println!("Total skips: {}", total_skips);
                    return data[i] * data[j] * data[k];
                }
            }
        }
    }
    println!("Total skips: {}", total_skips);

    return -1;
}
fn main() -> anyhow::Result<()> {
    let s: Vec<i64> = include_str!("input.txt")
        .split('\n')
        .map(str::parse::<i64>)
        .collect::<Result<Vec<_>, _>>()?;

    println!("Answer: {}", eval_answer(&s));
    Ok(())
}
