meal = 44.50
tax = 6.75 / 100
tip = 15.0 / 100


meal = meal + meal * tax
total = (meal * tip) + meal

print 'Your total bill plus tip is ' +  ("%.2f" % total)
