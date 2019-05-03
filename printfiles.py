import os

with open("filenames.txt", "w") as f:
	for file in os.listdir('Media/kiekjes'):
	    f.write('"Media/kiekjes/%s", '%file)