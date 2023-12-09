use std::cmp::Ordering;

fn compare_slices(slice1: &Vec<u32>, slice2: &Vec<u32>) -> Ordering {
    slice1.cmp(slice2)
}

// Maps cards as expected, for part 1
fn card_char_to_num(c: char) -> u32 {
    return match c {
        'T' => 10,
        'J' => 11,
        'Q' => 12,
        'K' => 13,
        'A' => 14,
        // Overflow impossible, largest num == 9
        _ => c.to_digit(10).unwrap(),
    };
}

// Gives jacks a value of 1, for use in part 2
fn card_char_to_num_mod(c: char) -> u32 {
    return match c {
        'T' => 10,
        'J' => 1,
        'Q' => 12,
        'K' => 13,
        'A' => 14,
        // Overflow impossible, largest num == 9
        _ => c.to_digit(10).unwrap(),
    };
}

fn parse_input(input: &str) -> Vec<(&str, &str)> {
    let lines: Vec<Vec<&str>> = input
        .lines()
        .map(|line| line.split(' ').collect())
        .collect();
    return lines.iter().map(|pair| (pair[0], pair[1])).collect();
}

fn evaluate_hand(hand: &str) -> i32 {
    let mut occurences: [i32; 14] = [0; 14];
    let mut num;
    for c in hand.chars() {
        num = card_char_to_num_mod(c) - 1;
        occurences[if num <= 13 { num as usize } else { 0 }] += 1;
    }
    // PART 2: Switches out Jacks for whatever other card you have most of
    if occurences[0] != 0 {
        let occurences_wo_first = occurences.get(1..).unwrap();
        let max_with_index = occurences_wo_first
            .iter()
            .enumerate()
            .max_by(|(_, val1), (_, val2)| val1.cmp(val2))
            .map(|(i, val)| (i, val))
            .unwrap();
        occurences[max_with_index.0 + 1] += occurences[0];
        occurences[0] = 0;
    }
    occurences.sort_by(|v, v2| {
        if v2 == v {
            Ordering::Equal
        } else if v2 < v {
            Ordering::Less
        } else {
            Ordering::Greater
        }
    });
    return match occurences.get(0..5) {
        // Five of a kind
        Some([5, 0, 0, 0, 0]) => 7,
        // Four of a kind
        Some([4, 1, 0, 0, 0]) => 6,
        // Full house
        Some([3, 2, 0, 0, 0]) => 5,
        // Three of a kind
        Some([3, 1, 1, 0, 0]) => 4,
        // Two pair
        Some([2, 2, 1, 0, 0]) => 3,
        // Pair
        Some([2, 1, 1, 1, 0]) => 2,
        // High Card
        Some([1, 1, 1, 1, 1]) => 1,
        Some(_) => 0,
        None => panic!("Hand incidence list is None, i.e. something went horribly wrong"),
    };
}

fn main() {
    let input = include_str!("input.txt");
    let mut hands = parse_input(input).clone();
    hands.sort_by(|h1, h2| {
        let h1_score = evaluate_hand(h1.0);
        let h2_score = evaluate_hand(h2.0);
        let h1_nums: Vec<u32> = h1.0.chars().map(|c| card_char_to_num_mod(c)).collect();
        let h2_nums: Vec<u32> = h2.0.chars().map(|c| card_char_to_num_mod(c)).collect();
        if h1_score > h2_score {
            Ordering::Greater
        } else if h1_score == h2_score {
            compare_slices(&h1_nums, &h2_nums)
        } else {
            Ordering::Less
        }
    });
    let mut total = 0;
    for (i, (_, bid)) in hands.iter().enumerate() {
        total += bid.parse::<usize>().unwrap() * (i + 1);
    }
    println!("{:?}", total);
}

#[test]
fn test_eval_hand() {
    let test_result = evaluate_hand("J2JTJ");
    println!("Test result: {}", test_result);
    assert_eq!(test_result, 6);
}
