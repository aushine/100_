import datetime as dt
if __name__ == "__main__":
    #output today date format is dd/mm/yyyy. use strftime()function
    print(dt.date.today().strftime('%d/%m/%Y'))
    # create date object
    miyazakiBirthDate = dt.date(1941, 1, 5)
    print(miyazakiBirthDate.strftime('%d/%m/%Y'))