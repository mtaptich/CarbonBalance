import json, csv, math

def addbond(sym, source,target, bond, size):
	molecule["nodes"].append({"atom": sym, "size": size})
	molecule["links"].append({"source": source, "target": target, "bond": bond})

def propane(nodeid):
	addbond("H",0+nodeid,3+nodeid,1,1)
	addbond("H",1+nodeid,3+nodeid,1,1)
	addbond("H",2+nodeid,3+nodeid,1,1)
	addbond("C",3+nodeid,4+nodeid,1,12)
	addbond("C",4+nodeid,5+nodeid,1,12)
	addbond("C",5+nodeid,4+nodeid,1,12)
	addbond("H",6+nodeid,5+nodeid,1,1)
	addbond("H",7+nodeid,5+nodeid,1,1)
	addbond("H",8+nodeid,5+nodeid,1,1)
	addbond("H",9+nodeid,4+nodeid,1,1)
	addbond("H",10+nodeid,4+nodeid,1,1)

	return nodeid + 11;

def O2(nodeid):
	addbond("O",0+nodeid,1+nodeid,1,16)
	addbond("O",1+nodeid,0+nodeid,1,16)
	return nodeid + 2;


elements = {}
with open('data/periodic.csv', 'r') as f:
    next(f)
    reader = csv.reader(f)
    for line in reader:
    	elements[line[1]] = {"mass": line[3], "color": line[4]}

molecule = {"nodes": [], "links":[]}

nodeid = 0
for i in range(0,5):
	print nodeid
	nodeid = propane(nodeid)

for i in range (0,7):
	nodeid = O2(nodeid);



with open('data/molecule.json', 'wb') as fp:
    json.dump(molecule, fp)