import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

WIDTH = 500

WIN = pygame.display.set_mode((WIDTH, WIDTH))

global start_placed 
global end_placed
end_placed = False
start_placed = False

START_COLOUR = BLUE
END_COLOUR = ORANGE
ROWS = 20


class Vertex: 
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value

    def getRow(self):
        return self.row
    
    def getCol(self):
        return self.col
    
    def isVertex(self):
        return self.value
    
    def getDistance(self, v2):
        return abs(self.getRow() - v2.getRow()) + abs(self.getCol() - v2.getCol())
    
    
    # def __eq__(self, other):
    #     return isinstance(other, Vertex) and self.row == other.row and self.col == other.col

class Cell:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def isWall(self):
        return self.color == BLACK
    
    def make_start(self):
        self.color = START_COLOUR

    def make_end(self):
        self.color = ORANGE

    def make_barrier(self):
        self.color = BLACK

    def make_open(self):
        self.color = WHITE

    def make_visited(self):
        self.color = GREEN

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def getRow(self):
        return self.row
    
    def getCol(self):
        return self.col
    
    def isStart(self):
        return self.color == START_COLOUR
    
    def isEnd(self):
        return self.color == ORANGE
    
    def isOpen(self):
        return self.color == WHITE
    
    def isClosed(self):
        return self.color == BLACK
    
    def getColour(self):
        return self.color
    
    def make_visited(self):
        self.color = GREEN

    def make_neighbour(self):
        self.color = RED

    def make_path(self):
        self.color = PURPLE

    def equals(self, other):
        return (self.getRow() == other.getRow()) and (self.getCol() == other.getCol())
    




def djikstra_algo(draw, grid, source, target):
    q = [] 
    get_vertices(grid, q)

    vertexToSource = {vertex: float('inf') for vertex in q}
    prevVertex = {vertex: None for vertex in q}
    path = [] # Stack
	
    vertexToSource[source] = float (0)
    q.append(source)

    source_cell = grid[source.getRow()][source.getCol()]
    target_cell = grid[target.getRow()][target.getCol()]
	

    while(len(q) > 0):
        u = getMinDistVertex(q, vertexToSource)
        spot = grid[u.getRow()][u.getCol()]
        if not spot.equals(source_cell) and not spot.equals(target_cell):
            spot.make_visited()
            draw()
		
        q.remove(u)
        uNeighbours = getNeighboursInQ(u, q)
        for v in uNeighbours:
            alt =  vertexToSource.get(u) + u.getDistance(v)
            spot = grid[v.getRow()][v.getCol()]
            if not spot.equals(source_cell) and not spot.equals(target_cell):
                spot.make_neighbour()
                draw()

            if alt < vertexToSource.get(v) :
                vertexToSource[v] = alt; 
                prevVertex[v] = u; 

        if(u.getRow() == target.getRow() and u.getCol() == target.getCol()):
            getPreviousSet(source, target, u, path, prevVertex) # Recursive function which gets previous vertices set of a given vertex
            break 

    for vertex in path:
        spot = grid[vertex.getRow()][vertex.getCol()]
        if not spot.equals(source_cell) and not spot.equals(target_cell):
            spot.make_path()
            draw()

    return path
    



def getPreviousSet(source, target, vertex, path, prevSet):
    previous = prevSet.get(vertex)
    if previous is None:
        return

    if previous == source:
        path.append(vertex)
        path.append(previous)
        return

    path.append(vertex)
    getPreviousSet(source, target, previous, path, prevSet)

def getNeighboursInQ(vertex, q):
    neighbours = [] 
    
    for v in q: 
        if((vertex.getCol() == v.getCol()) and (abs(vertex.getRow() - v.getRow()) == 1)):
            if(vertex.isVertex()) : neighbours.append(v)
		 
        elif((vertex.getRow() == v.getRow()) and (abs(vertex.getCol() - v.getCol())== 1)):
            if(vertex.isVertex()) : neighbours.append(v); 

    return neighbours 

def get_vertices(grid, q):
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if not grid[i][j].isClosed():
                vertex = Vertex(i, j, grid[i][j])
                q.append(vertex)


def getMinDistVertex(q, vTs):
    minDist = vTs[q[0]]
    closestVertex = q[0]

    for vertex in q: 
        if vTs[vertex] <= minDist:
            minDist = vTs[vertex]
            closestVertex = vertex
			
    return closestVertex



def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			cell = Cell(i, j, gap, rows)
			grid[i].append(cell)

	return grid

def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
	win.fill(WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()
      
def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col


def main(win, width):
    # ROWS = 5
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    board = [[0] * ROWS for _ in range(ROWS)]

    global start_placed, end_placed
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]

                if not start_placed:
                    start = Vertex(spot.getRow(), spot.getCol(), 1)
                    start_cell = spot
                    start_cell.make_start()
                    start_placed = True

                elif not end_placed and spot != start:
                    end = Vertex(spot.getRow(), spot.getCol(), 1)
                    end_cell = spot
                    end_cell.make_end()
                    end_placed = True

                elif spot.equals(start_cell):
                     spot.make_open()
                     start_placed = False
                
                elif spot.equals(end_cell):
                     spot.make_open()
                     end_placed = False
                

                elif start_placed and end_placed:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.make_open()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                            
                    for row in grid:
                        for value in row:
                            if value.isClosed():
                                board[value.getCol()][value.getRow()] = -1
                            else:
                                board[value.getCol()][value.getRow()] = 1
                            
                    djikstra_algo(lambda: draw(win, grid, ROWS, width), grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    start_placed = False
                    end_placed = False
                    board = [[0] * ROWS for _ in range(ROWS)]
                    grid = make_grid(ROWS, width)

    pygame.quit()


main(WIN, WIDTH)

# main(WIN, WIDTH)
# main2()