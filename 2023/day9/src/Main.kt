import java.io.File

fun processList(values: ArrayList<Int>, intermediates: ArrayList<ArrayList<Int>>): ArrayList<ArrayList<Int>>{
    if(values.all { v -> v == 0 }) {
        return intermediates
    }
    val processed: ArrayList<Int> = ArrayList();
    for (i in values.indices) {
        if(i < 1) {continue}
        processed.add(values[i] - values[i-1])
    }
    return processList(processed, intermediates.plusElement(processed) as ArrayList<ArrayList<Int>>)
}

fun add_up(sequences: ArrayList<ArrayList<Int>>): Int {
    // All last elements except for uppermost
    val lasts = sequences.map { seq -> seq.last() }.subList(0, sequences.size-1)
    var total = 0
    for (i in lasts.size - 1 downTo 0) {
        total += lasts[i]
    }
    return total
}

fun sub_up(sequences: ArrayList<ArrayList<Int>>): Int {
    // All last elements except for uppermost
    val lasts = sequences.map { seq -> seq.first() }.subList(0, sequences.size-1)
    var total = 0
    for (i in lasts.size - 1 downTo 0) {
        total = lasts[i] - total
    }
    return total
}

fun parseInput(filename: String) {
    var nums: ArrayList<Int>;
    var intermediates = ArrayList<ArrayList<Int>>()
    val totals = ArrayList<Int>();
    val subs = ArrayList<Int>()
    for (line in File(filename).readLines()){
        intermediates = ArrayList()
        // "0 3 6" => [0, 3, 6]
        nums = line.split(" ").map { s -> s.toInt() } as ArrayList<Int>
        intermediates.add(nums)
        intermediates = processList(nums, intermediates)
        totals.add(add_up(intermediates))
        subs.add(sub_up(intermediates))
    }
    println("Part 1 --> " + totals.sum())
    println("Part 2 --> " + subs.sum())
}

fun main() {
    parseInput("input.txt")
}