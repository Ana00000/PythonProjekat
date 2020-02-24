class Vertex:
    def __init__(self, path, links):
        self._path = path
        self._links = links

    def get_path(self):
        return self._path

    def get_links(self):
        return self._links

class Edge:

    def __init__(self, start, end, value):
            self._start = start
            self._end = end
            self._value = value

    def get_end(self):
        return self._end

class Graph:


    def __init__(self, directed=True):
        self._out = {}
        self._in = {}

    def vertex_count(self):
        return len(self._out)

    def vertices(self):
        return self._out.keys()

    def edge_count(self):
        suma = 0
        for v in self._out:
            suma += len(self._out[v])
        return suma

    def edges(self):
        result = []
        for item in self._out.values():
            result.append(item.values())
        return result

    def get_edge(self, u, v):
        self._validate_vertex(u)
        self._validate_vertex(v)
        for item in self._out[u]:
            if item.destination() == v:
                return item

    def get_vertex(self, putanja):
        for v in self._out.keys():
            if v.get_path() == putanja:
                return v

        return None   # ako nije pronasao

    def degree(self, v, out=False):     # vraca ulazne ivice
        self._validate_vertex(v)
        if out:
            return len(self._out[v])
        else:
            return len(self._in[v])

    def incident_edges(self, v, out=False):   # vraca samo ulazne ivice
        self._validate_vertex(v)
        if out:
            return self._out[v]
        else:
            return self._in[v]

    def insert_vertex(self, path, links):
        v = Vertex(path, links)
        self._out[v] = {}
        self._in[v] = {}
        return v

    def insert_edge(self, u, v, x=None):
        self._validate_vertex(u)
        self._validate_vertex(v)
        line = Edge(u, v, x)
        self._out[u][v] = line
        self._in[v][u] = line
        # print("Edge je insertovan")

    def remove_vertex(self, v):
        lista_out = self._out[v].values()

        for edge in lista_out:
            self._in[edge.destination()].remove(edge)

        lista_in = self._in[v].values()

        for edge in lista_in:
            self._out[edge.destination()].remove(edge)

        del self._out[v]
        del self._in[v]

    def remove_edge(self, e):
        for item in self._out.values():
            if e in item:
                item.remove(e)

        for item in self._in.values():
            if e in item:
                item.remove(e)

    def _validate_vertex(self, v):
        if not isinstance(v, Vertex):
            raise TypeError('Vertex expected')

        if v not in self._out:
            raise ValueError('Vertex does not belong to this graph.')