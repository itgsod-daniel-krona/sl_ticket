def fares(age, child=False, student=False, senior=False):
    if child or student or senior:
        return 'Halv'
    else:
        if age < 18 or age > 65:
            return 'Halv'
        else:
            return 'Hel'


# tests
print 'child, 7', fares(7)
print 'child, 6', fares(6, child=True)
print 'young adult, 17', fares(17)
print 'student, 16', fares(16, student=True)
print 'adult, 23', fares(23)
print 'student, 23', fares(23, student=True)
print 'adult, 59', fares(59)
print 'senior, 59', fares(59, senior=True)
print 'senior, 67', fares(67)


#ett till program som ocksa funkar
#age = 'Ticket price'

#for age in range(0, 151):
    #print age
    #if age > 65 < 151:
        #print 'Price = Half a ticket'
    #elif age > 18 < 64:
        #print 'Price = Full ticket'
    #elif age > 7 < 17:
        #print 'Price = Half a ticket'
    #elif age > 1 < 6:
        #print 'Price = Free'+
        #charlotte callaa