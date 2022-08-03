import java.io.BufferedReader
 import java.io.BufferedWriter
 import java.io.InputStreamReader
 import java.io.OutputStreamWriter
 import java.math.BigInteger

 fun main() {
     val br = BufferedReader(InputStreamReader(System.`in`))
     val bw = BufferedWriter(OutputStreamWriter(System.out))
     with(br) {
         val list = readLine().toList().map { it.digitToInt() }
         val sum = list.sum()
         val ans: BigInteger = if (sum % 3 == 0 && 0 in list) {   
         BigInteger(list.sortedDescending().joinToString(""))
         } else BigInteger("-1")

         bw.write("" + ans + "\n")
         bw.flush()
         bw.close()
         close()
     }
 }
