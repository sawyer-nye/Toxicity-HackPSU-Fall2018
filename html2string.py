html_file = open("results_test.html", "r")
lines = html_file.readlines()

for line in lines:
	print("print(\"" + line.rstrip().replace('"', '\\"') + "\")")

html_file.close()