sunday = 0
monday = 1
tuesday = 2
wednesday =3
thursday = 4
friday = 5
saturday =6

trip_begin = int(input("What day will your trip start 'Sunday = 0 ... Saturday = 6?"))
duration_of_trip = int(input("How many days do you intend to stay?"))
total = trip_begin + duration_of_trip
answer = total % 7
print ("You will be returning on day",answer,"of the week!")

