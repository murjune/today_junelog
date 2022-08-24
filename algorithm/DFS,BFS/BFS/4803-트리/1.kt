import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter
import java.util.*

val br = BufferedReader(InputStreamReader(System.`in`))
val bw = BufferedWriter(OutputStreamWriter(System.out))
val graph = mutableListOf<MutableList<Int>>().apply {
    repeat(501) {
        add(mutableListOf())
    }
}
val visited = BooleanArray(501).apply { set(0, true) }
var case = 0
fun main() {
    while (true) {
        var ans = 0
        case++
        val (n, m) = br.readLine().split(" ").map { it.toInt() }
        if (n == 0 && m == 0) {
//            bw.write("$cnt\n")
            bw.flush()
            bw.close()
            br.close()
            return
        }
        repeat(m) {
            val (a, b) = br.readLine().split(" ").map { it.toInt() }
            graph[a].add(b)
            graph[b].add(a)
        }
        val d =
            repeat(n + 1) lab@{ idx ->
                if (idx == 0) return@lab

                if(!visited[idx] && bfs(idx)){
                        ans++
                }
            }
        when(ans){
            0 -> {
                bw.write("Case $case: No trees.\n")
            }
            1 -> {
                bw.write("Case $case: There is one tree.\n")
            }
            else -> {
                bw.write("Case $case: A forest of $ans trees.\n")
            }
        }
    }
}

private fun bfs(node: Int): Boolean {
    var isCycle = true
    val q = LinkedList<Int>().apply { add(node) }
    visited[node] = true

    while (q.isNotEmpty()) {
        val curNode = q.poll()

       for (nextNode in graph[curNode]){
           if(!visited[node]){
               q.add(node)
               visited[node] = true
           }else{
               isCycle = false
           }
       }
    }
    return isCycle
}

