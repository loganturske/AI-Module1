###
# Logan Turske
###
import operator
import math
class Node():
	"""A node class that will consist of all theinformation pertaining to a node in a graph for path finding """

	def __init__(self, parent=None, position=None):
		self.parent = parent
		self.position = position

		self.g = 0
		self.h = 0
		self.f = 0

	def __eq__(self, other):
		return self.position == other.position
		
full_world = [
  ['.', '.', '.', '.', '.', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', '.', '.', '.', '.', '*', '*', '*', '*', '*', '*', '*', '*', '*', '.', '.', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '.', '.'], 
  ['.', '.', '.', '.', 'x', 'x', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'x', 'x', 'x', '#', '#', '#', 'x', 'x', '#', '#'], 
  ['.', '.', '.', '.', '#', 'x', 'x', 'x', '*', '*', '*', '*', '~', '~', '*', '*', '*', '*', '*', '.', '.', '#', '#', 'x', 'x', '#', '.'], 
  ['.', '.', '.', '#', '#', 'x', 'x', '*', '*', '.', '.', '~', '~', '~', '~', '*', '*', '*', '.', '.', '.', '#', 'x', 'x', 'x', '#', '.'], 
  ['.', '#', '#', '#', 'x', 'x', '#', '#', '.', '.', '.', '.', '~', '~', '~', '~', '~', '.', '.', '.', '.', '.', '#', 'x', '#', '.', '.'], 
  ['.', '#', '#', 'x', 'x', '#', '#', '.', '.', '.', '.', '#', 'x', 'x', 'x', '~', '~', '~', '.', '.', '.', '.', '.', '#', '.', '.', '.'], 
  ['.', '.', '#', '#', '#', '#', '#', '.', '.', '.', '.', '.', '.', '#', 'x', 'x', 'x', '~', '~', '~', '.', '.', '#', '#', '#', '.', '.'], 
  ['.', '.', '.', '#', '#', '#', '.', '.', '.', '.', '.', '.', '#', '#', 'x', 'x', '.', '~', '~', '.', '.', '#', '#', '#', '.', '.', '.'], 
  ['.', '.', '.', '~', '~', '~', '.', '.', '#', '#', '#', 'x', 'x', 'x', 'x', '.', '.', '.', '~', '.', '#', '#', '#', '.', '.', '.', '.'], 
  ['.', '.', '~', '~', '~', '~', '~', '.', '#', '#', 'x', 'x', 'x', '#', '.', '.', '.', '.', '.', '#', 'x', 'x', 'x', '#', '.', '.', '.'], 
  ['.', '~', '~', '~', '~', '~', '.', '.', '#', 'x', 'x', '#', '.', '.', '.', '.', '~', '~', '.', '.', '#', 'x', 'x', '#', '.', '.', '.'], 
  ['~', '~', '~', '~', '~', '.', '.', '#', '#', 'x', 'x', '#', '.', '~', '~', '~', '~', '.', '.', '.', '#', 'x', '#', '.', '.', '.', '.'], 
  ['.', '~', '~', '~', '~', '.', '.', '#', '*', '*', '#', '.', '.', '.', '.', '~', '~', '~', '~', '.', '.', '#', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', '.', 'x', '.', '.', '*', '*', '*', '*', '#', '#', '#', '#', '.', '~', '~', '~', '.', '.', '#', 'x', '#', '.', '.', '.'], 
  ['.', '.', '.', 'x', 'x', 'x', '*', '*', '*', '*', '*', '*', 'x', 'x', 'x', '#', '#', '.', '~', '.', '#', 'x', 'x', '#', '.', '.', '.'], 
  ['.', '.', 'x', 'x', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'x', 'x', 'x', '.', '.', 'x', 'x', 'x', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', 'x', 'x', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'x', 'x', 'x', 'x', '.', '.', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', 'x', 'x', 'x', '*', '*', '*', '*', '*', '*', '*', '*', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', '.', 'x', 'x', 'x', '*', '*', '*', '*', '*', '*', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '~', '~', '~', '~'], 
  ['.', '.', '#', '#', '#', '#', 'x', 'x', '*', '*', '*', '*', '*', '.', 'x', '.', '.', '.', '.', '.', '~', '~', '~', '~', '~', '~', '~'], 
  ['.', '.', '.', '.', '#', '#', '#', 'x', 'x', 'x', '*', '*', 'x', 'x', '.', '.', '.', '.', '.', '.', '~', '~', '~', '~', '~', '~', '~'], 
  ['.', '.', '.', '.', '.', '.', '#', '#', '#', 'x', 'x', 'x', 'x', '.', '.', '.', '.', '#', '#', '.', '.', '~', '~', '~', '~', '~', '~'], 
  ['.', '#', '#', '.', '.', '#', '#', '#', '#', '#', '.', '.', '.', '.', '.', '#', '#', 'x', 'x', '#', '#', '.', '~', '~', '~', '~', '~'], 
  ['#', 'x', '#', '#', '#', '#', '.', '.', '.', '.', '.', 'x', 'x', 'x', '#', '#', 'x', 'x', '.', 'x', 'x', '#', '#', '~', '~', '~', '~'], 
  ['#', 'x', 'x', 'x', '#', '.', '.', '.', '.', '.', '#', '#', 'x', 'x', 'x', 'x', '#', '#', '#', '#', 'x', 'x', 'x', '~', '~', '~', '~'], 
  ['#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '#', '#', '#', '.', '.', '.', '.', '#', '#', '#', '.', '.', '.']]

test_world = [
  ['.', '*', '*', '*', '*', '*', '*'],
  ['.', '*', '*', '*', '*', '*', '*'],
  ['.', '*', '*', '*', '*', '*', '*'],
  ['.', '.', '.', '.', '.', '.', '.'],
  ['*', '*', '*', '*', '*', '*', '.'],
  ['*', '*', '*', '*', '*', '*', '.'],
  ['*', '*', '*', '*', '*', '*', '.'],
]

# left down right up
cardinal_moves = [(0,-1), (1,0), (0,1), (-1,0)]

# left down right up
cardinal_move_graphics = ["<", "v", ">", "^"]

# These are the costs associated with each marker on the world map
costs = { '.': 1, '*': 3, '#': 5, '~': 7}

def get_cost_to_move(node, world, costs):
	""" 
	This will return the cost it would be to move onto that particular tile given the cost symbol it has.

	node - the node you wish to move onto
	world - the entire world map
	costs - a dictonary of the costs accociated with symbols of the world map

	 """
	return costs[world[node.position[0]][node.position[1]]]


def get_children(node, world, moves):
	""" 
	This function will return all the positions available to the current node given the world map.

	node - the current node you wish to get the children of
	world - the entire world map
	moves - the moves that can be made in this universe, a list of tuples
	"""

	# The list that will hold all of the positions to return
	ret = []

	# Iterate through all of the moves you could make
	for move in moves:
		# The next handful of lines will make sure you are not going out of bounds of the world map
		if node.position[0] == 0 and move[0] == -1:
			continue
		if node.position[1] == 0 and move[1] == -1:
			continue
		if node.position[0] == len(world)-1 and move[0] == 1:
			continue
		if node.position[1] == len(world[0])-1 and move[1] == 1:
			continue 
		# Get the position by adding the tuples together
		pos = tuple(map(operator.add, move, node.position))
		# If you are an 'x' you are impassable and wont be apart of the children
		if world[pos[0]][pos[1]] == 'x':
			continue

		ret.append(pos)
	return ret


# heuristic function
def heuristic(node_pos, goal_node_pos):
	"""
	This is the heuristic function, currently euclidean distance in the grid world

	node_pos - a tuple with the position of the current node
	goal_node_pos - a tuple with the position of the goal node
	"""
	return math.sqrt((goal_node_pos[1] - node_pos[1])**2 + (goal_node_pos[0] - node_pos[0])** 2 )

def a_star_search( world, start, goal, costs, moves, heuristic):
	"""
	This is the main A* Search algorithm function. It will preform the A* algorithm. Uses a custom Node class found at the top of the file

	world - a 2D list containing the entire world map
	start - a tuple containing the start position
	goal - a tuple containing the goal position you wish to reach
	costs - a dictonary of the costs accociated with symbols of the world map
	moves - the moves that can be made in this universe, a list of tuples
	heuristic - not used right now due to me wanting to use the function

	"""
	# Initialize goal node
	goal_node = Node(None, goal)
	goal_node.h = 0
	goal_node.g  = goal_node.f = 0

	# Initialize start node
	start_node = Node(None, start)
	start_node.h = heuristic(start_node.position, goal_node.position)
	start_node.g = 0
	start_node.f = start_node.g + start_node.h
	
	# Create two lists "open" and "closed" that will be used to house the nodes for evaluating
	open_list = []
	closed_list = []

	# Add the starting node to the open list
	open_list.append(start_node)

	# Iterate while the open list still has nodes in it
	while len(open_list) > 0:
		# Sort the open list by the node's F(x) values
		open_list.sort(key=lambda x: x.f)

		# Pop the node with the lowest F(x) from the open list
		current = open_list.pop(0)

		# If you found the goal node, build the path back to the start by iterating through the parents
		if current == goal_node:
			arr = []
			while current is not None:
				arr.append(current.position)
				current = current.parent
			return arr[::-1]

		# Add the current node to the closed list because you are about to be done evaluating it
		closed_list.append(current)

		# Get all of the positions of your children that are viable to move to
		children = get_children(current, world, moves)
		# For each of the viable children
		for child in children:
			# If the child is in the closed list, you are done
			found = False
			for node in closed_list:
				if node.position == child:
					found = True
					continue
			if found == True:
				continue

			# If the child is in the open list
			found = False
			for node in open_list:
				if node.position == child:
					found = True
					# See if moving to that node will be better
					new_g = current.g + get_cost_to_move(node, world, costs)
					if node.g > new_g:
						# If it is, set the node to the new and improved g value and set its parent to the current node
						node.g = new_g
						node.parent = current
			# If you did not find the child
			if found == False:
				# Make a new node for the child and put it in the open list
				new_child = Node(current, child)
				new_child.g = current.g + get_cost_to_move(new_child, world, costs)
				new_child.h = heuristic(child, goal_node.position)
				open_list.append(new_child)

	return None

def pretty_print_solution( world, path, start):
	"""
	This function will replce the world with the path you found with directions

	world - the entire world
	path - the path you want to change
	start - the start position
	"""

	# Go through the path and replace the symbol with the corresponding direction iterating in the path	
	prev_step = start
	for i, step in enumerate(path[:-1]):
		index = 0
		for move in cardinal_moves:
			if tuple(map(operator.add, move, step)) == path[i+1]:
				world[step[0]][step[1]] = cardinal_move_graphics[index]
			index +=1
		prev_step = step

	world[path[-1][0]][path[-1][1]] = "G"
	for row in world:
		print(row)

if __name__ == "__main__":
	print("A* solution for test world")
	test_path = a_star_search(test_world, (0, 0), (6, 6), costs, cardinal_moves, heuristic)
	print(test_path)
	pretty_print_solution( test_world, test_path, (0, 0))

	print("A* solution for full world")
	full_path = a_star_search(full_world, (0, 0), (26, 26), costs, cardinal_moves, heuristic)
	print(full_path)
	pretty_print_solution(full_world, full_path, (0, 0))