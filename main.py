import datetime
emp = input ( " Enter Faculty Name " )

d1 = datetime . datetime ( 2021 , 5 , 12 , 9 , 30 , 00 )
d2 = datetime . datetime ( 2021 , 5 , 12 , 10 , 00 , 00 )
d3 = datetime . datetime ( 2021 , 5 , 12 , 10 , 15 , 00 )
d4 = datetime . datetime ( 2021 , 5 , 12 , 10 , 30 , 00 )
d5 = datetime . datetime ( 2021 , 5 , 12 , 12 , 00 , 00 )
d6 = datetime . datetime ( 2021 , 5 , 12 , 12 , 30 , 00 )
d7 = datetime . datetime ( 2021 , 5 , 12 , 13 , 30 , 00 )


e1 = datetime . datetime ( 2021 , 5 , 12 , 10 , 30 , 00 )
e2 = datetime . datetime ( 2021 , 5 , 12 , 11 , 00 , 00 )
e3 = datetime . datetime ( 2021 , 5 , 12 , 11 , 15 , 00 )
e4 = datetime . datetime ( 2021 , 5 , 12 , 11 , 30 , 00 )
e5 = datetime . datetime ( 2021 , 5 , 12 , 13 , 30 , 00 )
e6 = datetime . datetime ( 2021 , 5 , 12 , 13 , 50 , 00 )
e7 = datetime . datetime ( 2021 , 5 , 12 , 14 , 00 , 00 )


start = [ d1 , d2 , d3 , d4 , d5 , d6 , d7  ]

end = [ e1 , e2 , e3 , e4 , e5 , e6 , e7 ]



sl = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ]

print ( " JOB LIST " )
print ( "-----------" )
for i in range ( 7 ) :
	print ( " Sl NO " , sl[i] , " Start Time " , start[i] , " end time " , end[i]   )


for i in range ( 6 ) :

        if ( end[i] < start[i+1] ) : print ( " You can Attend " , start[i] , end [i] )
        i+=1
