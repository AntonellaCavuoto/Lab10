from model.model import Model

myModel = Model()
myModel.buildGraph(2000)
# print("N nodi", myModel.getNumNodes(), "; N Edges:", myModel.getNumEdges())
myModel.getInfoNodi()

# print(myModel.getStati())

stato = "United States of America"
# n1 = (myModel.getDFSNodesFromTree(stato))
# n2 = (myModel.getDFSNodesFromEdges(stato))
#
# if n1 == n2:
#     print (True)

