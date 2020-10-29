def last_digit(isbn):
    #replace '-' with emptyp space 
    isbn = isbn.replace('-', '')
    #conver into integer
    isbn = list(map(int, isbn))
    #run the calculation for digit 12 for isbn
    l = 10 - ((
        isbn[0] + (3*isbn[1]) + isbn[2] + (3*isbn[3]) + isbn[4] + (3*isbn[5]) +
        isbn[6] + (3*isbn[7]) + isbn[8] + (3*isbn[9]) + isbn[10] + (3*isbn[11])
    ) % 10)
    #format final input to align with isbn format
    return(f'{isbn[0]}{isbn[1]}{isbn[2]}-{isbn[3]}-{isbn[4]}{isbn[5]}{isbn[6]}-{isbn[7]}{isbn[8]}{isbn[9]}{isbn[10]}{isbn[11]}-{l}')
