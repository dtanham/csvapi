# Define an array mapping the array slot to a place in the REST hierarchy: (position,name)
# Ordering in REST hierarchy starts at 1
# Headers given here must match CSV column headers

# Eg: /api/{site}/{month}
# CSV: id,site,month,total,asked_to_match,successful_match,percent_asked,percent_matched,math_rate,final_dec
mapping = [
	(1, "site"),
	(2, "month")
]

# It doesn't matter if there are more columns than are defined in the mapping array.