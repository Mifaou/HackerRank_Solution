def is_leap(year):
    leap = False

    if not year%4==0:
        return leap
    else :
        if not year%100==0:
            return not leap
        else :
            if year%400==0:
                return not leap
            else :
               return leap