import flask, json, pandas

from flask import Flask
app = Flask(__name__)

# Get the mapping definition
import column_mapping

# Define the separator
SEPARATOR = ","

# Load all the data into memory (naughty)
headers = []
data = []
with open("data.csv") as d:
	# Assume header row
	data = d.readlines()
	data = [x.split(SEPARATOR) for x in data]
	headers = data[0]
	data = data[1:]

# Grab the number of columns
column_count = len(data[0])

# Get headers for the dataframe
df = pandas.read_csv("data.csv")

# Build the hierarchy from the column map
hierarchy_raw = sorted(column_mapping.mapping, key=lambda x: x[0])
hierarchy = []
# Remove those values with zero in the index
for i in range(len(hierarchy_raw)):
	if hierarchy_raw[i][0] > 0:
		hierarchy.append(hierarchy_raw[i])

# Create views to support dynamic mapping
def view_builder():
	def viewfunc(*args):
		view_df = df.copy()
		for i in range(len(args)):
			view_df = view_df[view_df[hierarchy[i][1]] == args[i]]
		output = [view_df[x:x+1].squeeze().to_dict() for x in range(len(view_df))]
		return json.dumps(output)
	return viewfunc

def generic_view(**kwargs):
	args = []
	for i in range(len(kwargs)):
		if hierarchy[i][1] in kwargs:
			args.append(kwargs[hierarchy[i][1]])
	view_df = df.copy()
	for i in range(len(args)):
		view_df = view_df[view_df[hierarchy[i][1]] == args[i]]
	output = [view_df[x:x+1].squeeze().to_dict() for x in range(len(view_df))]
	return json.dumps(output)

# Create routes according to mapping
path = "/"
for x in hierarchy:
	path += "<"+x[1]+">/"
	app.add_url_rule(path, view_func=generic_view)


@app.route("/")
def home():
    return "Hello API"

