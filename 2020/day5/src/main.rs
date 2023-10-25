use core::ops::Range;

enum SeatRangeOrRow {
    SeatRange(Range<i32>),
    Row(i32),
}

// Just return Range, check for range with same upper and lower bound later
fn split_range(c: char, r: Range<i32>) -> Option<SeatRangeOrRow> {
    let new_range = match c {
        'F' => Some(Range {
            start: r.start,
            end: (r.end + r.start) / 2,
        }),
        'B' => Some(Range {
            start: (r.end + r.start) / 2,
            end: r.end,
        }),
        _ => None,
    };
    return match new_range {
        Some(x) => {
            if x.start == x.end {
                Some(SeatRangeOrRow::Row(x.start))
            } else {
                Some(SeatRangeOrRow::SeatRange(x))
            }
        }
        None => None,
    };
}

fn fold_ticket(t: &str) -> i32 {
    //t.chars().fold(, f)
    todo!()
}

fn main() {
    println!("Hello, world!");
}
