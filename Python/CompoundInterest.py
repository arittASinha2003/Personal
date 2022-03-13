def compound_interest(principle, rate, time):
    CI = principle * (pow((1 + rate / 100), time))
    print("Compound interest is", CI) 
compound_interest(1000, 10.25, 5)
