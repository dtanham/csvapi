import flask, json, pandas, os

from flask import Flask
app = Flask(__name__)

# Get the mapping definition
import column_mapping

# Load all the data into memory (naughty)
df = pandas.read_csv(os.environ.get("CSVAPI_DATA_FILE", "data.csv"))

# Build the hierarchy from the column map
hierarchy = sorted(column_mapping.mapping, key=lambda x: x[0])

# View to be mapped to all the paths in the hierarchy
def generic_view(**kwargs):
	# Map keyword args to ordered columns from mapping file
	ordered_args = []
	for i in range(len(kwargs)):
		if hierarchy[i][1] in kwargs:
			ordered_args.append(kwargs[hierarchy[i][1]])
	view_df = df.copy()
	for i in range(len(ordered_args)):
		view_df = view_df[view_df[hierarchy[i][1]] == ordered_args[i]]
	return json.dumps([view_df[x:x+1].squeeze().to_dict() for x in range(len(view_df))])

# Create routes according to mapping
path = "/"
for x in hierarchy:
	path += "<"+x[1]+">/"
	app.add_url_rule(path, view_func=generic_view)
app.add_url_rule("/", view_func=generic_view)
