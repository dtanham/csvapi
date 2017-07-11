# Define an array mapping the array slot to a place in the REST hierarchy: (position,name)
# Use 0 to specify a column that won't be included in the hierarchy.
# Ordering in REST hierarchy starts at 1
# Headers given here must match CSV column headers

# Eg: /api/{jobcentre}/{month}
# CSV: id,site,month,total,asked_to_match,successful_match,percent_asked,percent_matched,math_rate,final_dec
mapping = [
	(0,"id"),				# 1st column
	(1, "site"),			# 2nd column
	(2, "month"),				# 3rd...
	(0, "total"),				# ...
	(0, "successful_match"),
	(0, "percent_asked"),
	(0, "percent_matched")
]

# It doesn't matter if there are more columns than are defined in the mapping array.