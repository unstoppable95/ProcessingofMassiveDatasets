import  scala.util.Random

val  groups = Map(0-> (0 ,1) , 1-> (1 ,1) , 2-> (2 ,2) ,  3->(3,3) ,4->(4,3) ,  5->(5,2) ,  6->(6,1))
val n = 1000000
val  random = Random

val  data = sc.parallelize(for (i<-1 to n) yield { val g=random.nextInt(7); val (mu,sigma) = groups(g); (g, mu+sigma*random.nextGaussian())})
data.cache

//for groups
// group , (number of examples, average, variance)
val resultsForGroups= data.map(t=>(t._1,(1,t._2,t._2*t._2))).reduceByKey((a,b)=>(a._1+b._1,a._2+b._2,a._3+b._3)).map(p=>(p._1,(p._2._1,(p._2._2/p._2._1),(p._2._3/p._2._1)-(p._2._2/p._2._1)*(p._2._2/p._2._1))))

resultsForGroups.collect().foreach(println)

//for all
//(0,(number of examples, sum, sum*sum))
val dataAll =data.map(t=>(t._1,(1,t._2,t._2*t._2))).reduceByKey((a,b)=>(a._1+b._1,a._2+b._2,a._3+b._3)).reduce((a,b) =>(0,(a._2._1+b._2._1, a._2._2+b._2._2, a._2._3+b._2._3)))


//(number of examples, average, variance)
val resultsAll = (dataAll._2._1, (dataAll._2._2/dataAll._2._1), (dataAll._2._3/dataAll._2._1)-(dataAll._2._2/dataAll._2._1)*(dataAll._2._2/dataAll._2._1))


println(resultsAll)