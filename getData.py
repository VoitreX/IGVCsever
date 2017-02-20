from pg import DB
Graphdb = DB(dbname='robo10', host='127.0.0.1', port=5432,  user='postgres', passwd='POSTGRES')
q = Graphdb.query("SELECT * FROM pathing.edges")
rawedges=q.getresult()
#print(q2)

q3 = Graphdb.query("SELECT * FROM pathing.points")
rawpoints=q3.getresult()
#print(q4)

dictEdges = {}
dictPoints = {}

class POINT():
	def __init__(self, id, longitude, latitude, elevation):
		self.id = id
		self.longitude = longitude
		self.latitude = latitude
		self.elevation = elevation
		self.edges = []
	def getID(slef):
		return self.id
	def getIDA(self):
		return self.longitude
	def getIDB(self):
		return self.latitude
	def getDIR(self):
		return self.elevation
	def __repr__(self):
		return "**ID:"+str(self.id)+" Long:"+str(self.longitude)+" LAT:"+str(self.latitude)+" Elev:"+str(self.elevation)+"**"

class EDGE():
	def __init__(self, id, ida, idb, direction):
		self.id = id
		self.ida = ida
		self.idb = idb
		self.direction = direction
		self.weight = 0
	def getID(slef):
		return self.id
	def getIDA(self):
		return self.ida
	def getIDB(self):
		return self.idb
	def getDIR(self):
		return self.direction
	def __repr__(self):
		return "**ID:"+str(self.id)+" IDA:"+str(self.ida)+" IDB:"+str(self.idb)+" Direction:"+str(self.direction)+"**"

class GRAPH():
	def __init__(self, edges, points):
		self.edges=edges
		self.points=pointsi

	def getEdge(self, edgeIndex):
		return self.edges[edgeIndex]
	def getPoint(self, pointIndex):
		return self.points[pointIndex]

	#def edit_edge(self, num):
	#	pass
	
	def edit_point(self, pointIndex, long, lat, elev):
		edit_p = self.points[pointIndex]
		edit_p.longitude = long
		edit_p.latitude = lat
		edit_p.elevation = elev
		

		#edit server side too
		Graphdb.query("UPDATE pathing.points SET longitude = %3.12f , latitude = %3.12f , elevation = %3.12f WHERE id = %d", (long, lat, elev, pointIndex) )

	
	def rm_edge(self, edgeIndex):
		rm_e = self.edges[edgeIndex]
		
		rm_ida = rm_e.ida
		rm_idb = rm_e.idb

		rm_ida.edges.remove(rm_e)
		rm_idb.edges.remove(rm_e)
		#will need to remove edge from data base too
		Graphdb.query("DELETE FROM pathing.edges WHERE id = %d", (edgeIndex))
		del self.edges[edgeIndex]

	def rm_point(self, pointIndex):
		rm_p = self.points[pointIndex]
		
		for ed in rm_p.edges:
			self.rm_edge(ed.id)

		#will need to remove edge from data base too
		Graphdb.query("DELETE FROM pathing.points WHERE id = %d", (pointIndex))
		del self.Points[pointIndex]

for p in rawpoints:
	dictPoints[p[0]]=POINT(p[0],p[1],p[2],p[3])

for e in rawedges:
	pointa = dictPoints[e[1]]
	pointb = dictPoints[e[2]]
	newEdge = EDGE(e[0], pointa, pointb, e[3]) 
	pointa.edges.append(newEdge)
	pointb.edges.append(newEdge)
	dictEdges[e[0]]=newEdge
	#change vaules to be actual points



#print(Graphdb.query("SELECT * FROM pathing.points")) 
print(dictEdges)
print(dictPoints)
