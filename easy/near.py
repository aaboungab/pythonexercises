#number of tables in times-table
tables = 10 

#defines rows
for row in range (1, tables + 1):
    for column in range(1, tables + 1):
        print(row * column, end="\t")
    print()