fun parse_input() {

}

fun main() {
    val vals = listOf(0, 3, 9, 12)
    var num_of_zeroes = 0
    for (i in vals.indices) {
        if(i<1){
            continue
        }
        num_of_zeroes += if (vals[i] - vals[i-1] == 0) 1 else 0
    }
    println("Zeroes: " + num_of_zeroes.toString())
}