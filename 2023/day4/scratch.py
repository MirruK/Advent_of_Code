import re


def split_inp():
    cards_raw = []
    with open(0) as file:
        cards_raw = list(map(lambda x: x.strip("\n"), file.readlines()))

    # Evil functional code, literally unreadable
    def get_digit_list(s: str) -> list[str]: return re.findall(r'[\d]+', s)
    def get_nums_part(s: str) -> list[str]: return s.split(":")[1].split("|")

    def composite(card_raw):
        # ["Game n: 1, 2, 3 | 1, 2, 3", ...] => [((1,2,3) ,(1,2,3)), ...]
        return tuple(map(lambda nums_strs: tuple(map(
            int, get_digit_list(nums_strs))), get_nums_part(card_raw)))
    return list(map(composite, cards_raw))


def total_points_for(card: tuple[list[int], list[int]]):
    points = 0
    matches = [0]*100
    # Create histogram of found numbers
    for num in card[0]:
        matches[num] += 1
    for num in card[1]:
        if matches[num] > 0:
            points += 1
    return 2**(points-1) if points > 0 else 0


def new_cards_won_for(card: tuple[list[int], list[int]]):
    points = 0
    matches = [0]*100
    # Create histogram of found numbers
    for num in card[0]:
        matches[num] += 1
    for num in card[1]:
        if matches[num] > 0:
            points += 1
    return points


def add_over(wins, out):
    for ind, num in enumerate(wins):
        for j in range(num):
            out[ind+1+j+(len(out)-len(wins))] += out[ind]


def main():
    splitted = split_inp()
    matches_per_card = []
    part1 = []
    for card in splitted:
        matches_per_card.append(new_cards_won_for(card))
        part1.append(total_points_for(card))

    out = [1]*len(matches_per_card)
    add_over(matches_per_card, out)
    print(f"Part 1 --> {sum(part1)}")
    print(f"Part 2 --> {sum(out)}")


main()
