use core::ops::Range;

fn split_range(c: char, r: Range<i32>) -> Option<Range<i32>> {
    return match c {
        'F' | 'L' => Some(r.start..((r.end + r.start) / 2)),
        'B' | 'R' => Some(((r.end + r.start) / 2)..r.end),
        _ => None,
    };
}

fn get_seat_id(row: i32, col: i32) -> i32 {
    row * 8 + col
}

fn is_collapsed(r: &Range<i32>) -> bool {
    return if r.start == (r.end - 1) { true } else { false };
}

fn fold_ticket(t: &str, initial_range: Range<i32>) -> i32 {
    let final_range = t
        .chars()
        .fold(Some(initial_range), |acc, curr| {
            split_range(
                curr,
                acc.expect(
                    format!("Error in input data, got char {}, expected F or B", curr).as_str(),
                ),
            )
        })
        .unwrap();
    if !is_collapsed(&final_range) {
        panic!("Range {:?} not collapsed", final_range);
    }
    return final_range.start;
}

fn main() {
    let input = include_str!("./input.txt");
    let some_tickets = input.lines().map(|l| match l {
        "\n" | " " => None,
        _ => Some((&l[0..7], &l[7..10])),
    });
    let tickets = some_tickets.filter(|v| v.is_some()).map(|v| v.unwrap());
    let ids = tickets.map(|t| get_seat_id(fold_ticket(t.0, 0..128), fold_ticket(t.1, 0..8)));
    println!("{}", ids.max().unwrap());
    //tickets.for_each(|t| println!("tickets: {:?}", t));
}

#[test]
fn test_fold_ticket() {
    let valid_ticket = "FBFBBFF";
    let res = fold_ticket(valid_ticket, 0..128);
    assert_eq!(res, 44);
    let valid_ticket2 = "BFFFBBF";
    let res2 = fold_ticket(valid_ticket2, 0..128);
    assert_eq!(res2, 70);
    let valid_ticket3 = "RLR";
    let res2 = fold_ticket(valid_ticket3, 0..8);
    assert_eq!(res2, 5);
}

#[test]
fn test_split_range() {
    let char1 = 'F';
    let range1 = Range { start: 0, end: 128 };
    let result1 = split_range(char1, range1).unwrap();
    assert_eq!(result1, Range { start: 0, end: 64 });
    let char2 = 'B';
    let result2 = split_range(char2, result1).unwrap();
    assert_eq!(result2, Range { start: 32, end: 64 });
}
