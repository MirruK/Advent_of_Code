# AoC day 7 lessons learned

My ego took a big hit trying to solve this one
I think I got pretty close but I eventually had to
look up the answer on youtube

## Takeaways
1. Use a stack datastructure when you have nested
structures. The last in first out principle works well
for these sorts of problems

2. Writing better recursive functions

3. Using map within a recursive function where
map takes the function itself as one of its inputs

4. Utilizing the power of dictionaries
and related methods. dict.values and just dictionary magic
in general can be super useful for representing many
forms of data

5. A call to the float constructor like this: float("inf"),
yields a highest floating value number, might turn out useful
