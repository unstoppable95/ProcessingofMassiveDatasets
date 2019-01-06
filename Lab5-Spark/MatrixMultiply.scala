//read examples of 2D arrays (row, culumn, value)
val matrixM = sc.textFile("M.txt").map(line =>{val t = line.split(" "); (t(0).trim.toInt, t(1).trim.toInt, t(2).trim.toDouble)})

val matrixN = sc.textFile("N.txt").map(line =>{val t = line.split(" "); (t(0).trim.toInt, t(1).trim.toInt, t(2).trim.toDouble)})

//prepare matrix N -> row (column, value) 
val newN = matrixN.map(n=> (n._1,(n._2,n._3)))
//prepare matrix M-> column (row, value)
val newM = matrixM.map(m => (m._2,(m._1,m._3)))

//newM.join(newN) example (13,((6,-8.0),(17,-4.0)))
val mxn = newM.join(newN).
map({case( rowNcolM, ((rowM,valueM),(colN,valueN))) => ((rowM,colN), valueM*valueN)}).
reduceByKey(_+_).
sortByKey(true).
map({case((rowM,colN), sum) => (rowM, colN, sum.toInt)})

mxn.collect().foreach(println)
