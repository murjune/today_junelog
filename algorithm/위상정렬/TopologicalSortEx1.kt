import java.util.LinkedList

object TopologicalSortEx1 {
    // 진입차수를 활용한 DAG 방식
    fun topologySort(graph: Array<MutableList<Int>>, indegrees: IntArray, v: Int, e: Int) {

        val result = mutableListOf<Int>()
        val q = LinkedList<Int>()

        // 처음 시작할 때는 진입차수가 0 인 노드를 큐에 삽입
        repeat(v) {
            val node = it + 1
            if (indegrees[node] == 0) q.add(node)
        }
        while (q.isNotEmpty()) {
            val cur = q.remove()
            result.add(cur)

            for (next in graph[cur]) {
                indegrees[next] -= 1
                if (indegrees[next] == 0) q.add(next)
            }
        }
        println(result.joinToString(" "))
    }
    // dfs를 활용한 DAG 방식
    fun topologySort2(graph: Array<MutableList<Int>>, v: Int, e: Int) {
        val visited = BooleanArray(v + 1) { false }
        val result = mutableListOf<Int>()
        fun dfs(cur: Int) {
            visited[cur] = true
            for (next in graph[cur]) {
                if (visited[next].not()) dfs(next)
            }
            // 랜덤으로 수ㅗㅃㅂ기

            result.add(cur)
        }

        repeat(v) {
            val node = it + 1
            if (visited[node].not()) {
                dfs(node)
            }
        }
        println(result.reversed().joinToString(" "))
    }


    @JvmStatic
    fun main(args: Array<String>) {
        val (v, e) = readln().split(" ").map { it.toInt() }
        val indegress = IntArray(v + 1)
        val graph = Array(v + 1) { mutableListOf<Int>() }
        repeat(e) {
            val (a, b) = readln().split(" ").map { it.toInt() }
            graph[a].add(b)
            indegress[b] += 1
        }
        topologySort(graph, indegress, v, e)
        topologySort2(graph, v, e)
    }
}
/*
input
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

output
1 2 5 3 6 4 7
* */
