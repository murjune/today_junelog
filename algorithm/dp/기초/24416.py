import sys

input = lambda: sys.stdin.readline().rstrip()
write = lambda x: sys.stdout.write(str(x) + "\n")

def fibo(i):
    global ans1
    if (i == 1 or i == 2):
        ans1 += 1
        return 1
    return fibo(i-1) + fibo(i-2)

def dpFibo(i):
    global ans2
    if (i == 1 or i == 2):
        return 1
    if (dp[i]):
        return dp[i]
    ans2 += 1
    dp[i] = dpFibo(i-1) + dpFibo(i-2)
    return dp[i]
n = int(input())
dp = [0]*(n+1)
ans1, ans2 = 0, 0
dpFibo(n)
fibo(n)
print(ans1, ans2)



import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter


var ans1 = 0
var ans2 = 0
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.out))
    val n = br.readLine().toInt()
    val d = IntArray(n) { 0 }

    bw.write("$ans1 $ans2\n")
    bw.flush()
    bw.close()
    br.close()

}

private fun fibo(i: Int): Int {
    if (i == 1 || i == 2) {
        ans1++
        return 1
    }
    return fibo(i - 1) + fibo(i - 2)
}

private fun dpFibo(i: Int, d: IntArray): Int {
    if (i == 1 || i == 2) {
        return 1
    }
    if(d[i] >= 0){

    }
}
