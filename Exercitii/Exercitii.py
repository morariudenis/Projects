values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)


exam_st_date = (11,12,2014)
print( "The examination will start from %s.%s.%s "%exam_st_date)