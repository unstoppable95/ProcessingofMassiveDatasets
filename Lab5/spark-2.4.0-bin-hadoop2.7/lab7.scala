import  scala.util.Random

val  groups = Map(0-> (0 ,1) , 1-> (1 ,1) , 2-> (2 ,2) ,  3->(3,3) ,4->(4,3) ,  5->(5,2) ,  6->(6,1))
val n = 1000000
val  random = Random

val  data = sc.parallelize(for (i<-1 to n) yield { val g=random.nextInt(7); val (mu,sigma) = groups(g); (g, mu+sigma*random.nextGaussian())})
data.cache

//check 10 records
data.take(10)

val resultsForGroups= data.map(t=>(t._1,(1,t._2,t._2*t._2))).reduceByKey((a,b)=>(a._1+b._1,a._2+b._2,a._3+b._3)).map(p=>(p._1,p._2._2/p._2._1))

resultsForGroups.take(7)
