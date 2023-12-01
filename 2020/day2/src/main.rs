use atoi::atoi;
fn get_counts(data: &Vec<&str>) -> Vec<(i64, i64)> {
    data.iter()
        .map(|s| {
            let counts = s
                .split('-')
                .map(|spl| atoi::<i64>(spl.as_bytes()))
                .collect::<Option<Vec<i64>>>()
                .unwrap();
            (counts[0], counts[1])
        })
        .collect()
}

fn get_letter(data: &Vec<&str>) -> Vec<char> {
    data.iter()
        .map(|s| s.chars().find(|c| c.is_alphabetic()).unwrap())
        .collect()
}

fn get_password(data: &Vec<&str>) -> Vec<String> {
    data.iter()
        .map(|s| String::from(s.split(' ').nth_back(0).unwrap()))
        .collect::<Vec<String>>()
}

fn count_char_in_str(c: char, s: &str) -> i64 {
    s.chars()
        .into_iter()
        .fold(0, |acc: i64, ch: char| if ch == c { acc + 1 } else { acc })
}

fn char_is_at_index(c: char, i: usize, s: &str) -> bool {
    if i < 1 {
        return s.chars().next().unwrap() == c;
    }
    s.chars().skip(i - 1).next().unwrap_or_else(|| '~') == c
}

fn main() {
    let data = include_str!("./input.txt")
        .split('\n')
        .collect::<Vec<&str>>(); //vec!["1-3 a: abcde", "1-3 b: cdefg", "2-9 c : ccccccccc"];
    let counts = get_counts(&data);
    let letters = get_letter(&data);
    let passwords = get_password(&data);

    println!("Counts: {:?}", counts);
    println!("Letters: {:?}", letters);
    //println!("Passwords: {:?}", passwords);
    // println!(
    //     "Count occurrences of \'a\' in: \"{0}\" -> {1}",
    //     passwords[0],
    //     count_char_in_str('a', &passwords[0])
    // );
    //let mut curr_n_chars;
    let mut n_valid_passwords = 0;
    //Solution part 1
    // for i in 0..passwords.len() {
    //     curr_n_chars = count_char_in_str(letters[i], &passwords[i]);
    //     if counts[i].0 <= curr_n_chars && counts[i].1 >= curr_n_chars {
    //         n_valid_passwords += 1;
    //     }
    // }
    // Solution part 2
    for i in 0..passwords.len() {
        if char_is_at_index(letters[i], counts[i].0.try_into().unwrap(), &passwords[i])
            ^ char_is_at_index(letters[i], counts[i].1.try_into().unwrap(), &passwords[i])
        {
            n_valid_passwords += 1;
        }
    }
    println!("Number of valid passwords in list: {}", n_valid_passwords);
    // assert_eq!(counts[0], (1, 3));
    // assert_eq!(counts[2], (2, 9));
}
