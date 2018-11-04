##Technologie
W rozwiązaniu zadania zdecydowałem się wykorzystać Pythona i SQLite, ponieważ zależało mi na prostocie i szybkości implementacji 
oraz minimalizacji pobieranych bibliotek czy software'u( wszystko sprowadza się do 2 linijek w Dockerfile).
Ponadto Python oferował dość przyjazne konwertowanie znacznika czasowego Unixa do czasu w UTC, skąd w prosty
sposób uzyskałem interesujące mnie dane czyli rok,miesiąc i dzień.
Stworzone przeze mnie tabele po transformacji znajdują się w pliku Schemat_bazy.jpg. 

##Wyniki
```
You're The One Dwight Yoakam 145267
Undo Björk 129778
Revelry Kings Of Leon 105162
Sehr kosmisch Harmonia 84981
Horn Concerto No. 4 in E flat K495: II. Romance (Andante cantabile) Barry Tuckwell/Academy of St Martin-in-the-Fields/Sir Neville Marriner 77632
Dog Days Are Over (Radio Edit) Florence + The Machine 71300
Secrets OneRepublic 58472
Canada Five Iron Frenzy 54655
Invalid Tub Ring 53494
Ain't Misbehavin Sam Cooke 49073
ec6dfcf19485cb011e0b22637075037aae34cf26 1040
119b7c88d58d0c6eb051365c103da5caf817bea6 641
b7c24f770be6b802805ac0e2106624a517643c17 637
4e73d9e058d2b1f2dba9c1fe4a8f416f9f58364f 592
d7d2d888ae04d16e994d6964214a1de81392ee04 586
6d625c6557df84b60d90426c0116138b617b9449 584
113255a012b2affeab62607563d03fbdf31b08e7 561
c1255748c06ee3f6440c51c439446886c7807095 547
db6a78c78c9239aba33861dae7611a6893fb27d5 529
99ac3d883681e21ea68071019dba828ce76fe94d 499
Coldplay 201081
1 2353423
2 2142793
3 2354696
4 2280733
5 2358146
6 2277770
7 2353362
8 2354811
9 2281371
10 2355043
11 2278369
12 2338840
00832bf55ed890afeb2b163024fbcfaf58803098
01cb7e60ba11f9b96e9899dd8da74c277145066e
0ac20218b5168c10b8075f1f8d4aff2746a2da39
1084d826f98b307256723cc5e9a3590600b87399
11abd6aaa54a50ed5575e8af9a485db752b97b42
28daf225834bae38f86555c8a03bca3bbf0e535d
429303f0cacab81f0c03ddfd7c2d472c8373e130
476a5902414891326ebcd8f6d9b5849f462704fa
4cd2428f7bfcff1e2423bbdfc1437a1572c23700
5283f472d868bfac68805acb83f35fd7142e3afd
```
## Schemat bazy danych
![Schemat bazy danych](Schemat.bazy.jpg)


# Lab 3 Data processing in Databases

## Download Million Song Dataset
```
bash get_dataset.sh
```

## To build example SQLite Docker image:

```
docker build -t lab3 .
```

## To run example container:
```
docker run --name lab3con lab3
```

## To stop and remove example container:
```
docker stop lab3con
docker rm lab3con
```

## To run example container in an interactive mode:
```
docker run -i -t sqlite_example /bin/bash
```
