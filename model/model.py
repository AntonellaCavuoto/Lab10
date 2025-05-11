import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = DAO.getAllCountries()
        self._idMap = {}
        for c in self._nodes:
            self._idMap[c.CCode] = c

    def buildGraph(self, anno):
        self.addNodes(anno)
        self.addAllEdges(anno)

    def addNodes(self, anno):
        confini = DAO.getNodi(anno)

        for c in confini:
            self._graph.add_node(self._idMap[c.state1no])
            self._graph.add_node(self._idMap[c.state2no])

    def addAllEdges(self, anno):
        confini = DAO.getArchi(anno)

        for c in confini:
            self._graph.add_edge(self._idMap[c.state1no], self._idMap[c.state2no])

    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)

    def getInfoNodi(self):
        list = []
        for n in self._idMap.values():
            if n not in self._graph.nodes():
                list.append((n, 0))
            else:
                list.append((n, self._graph.degree(n)))
        sortedList = sorted(list, key=lambda x: x[
            0])  # prendo il primo elemento della tupla (country) che ha __lt__ per il nome
        return sortedList

    def getInfoConn(self):
        return nx.number_connected_components(self._graph)

    def getStati(self):
        list = []
        for s in self._idMap.values():
            list.append(s.StateNme)

        sortedList = sorted(list, key=lambda x: x[0])
        return sortedList

    def getDFSNodesFromEdges(self, stato):
        source = None
        for s in self._idMap.values():
            if s.StateNme == stato:
                source = s

        archi = nx.dfs_edges(self._graph, source)
        res = []
        for u, v in archi:
            res.append(v)

        return res

    # def getDFSNodesFromTree(self, stato):
    #     source = None
    #     for s in self._idMap.values():
    #         if s.StateNme == stato:
    #             source = s
    #     tree = nx.dfs_tree(self._graph, source)
    #     nodi = list(tree.nodes())
    #
    #     return nodi[1:]

    # def getDFSNodesFromEdges1(self, stato):
    #     source = None
    #     for s in self._idMap.values():
    #         if s.StateNme == stato:
    #             source = s
    #
    #     tree = nx.dfs_tree(self._graph, source)
    #     a = list(tree.nodes)
    #     a.remove(source)
    #     return a

