import movement

def initialize():
	clear()
	for i in range(0, get_world_size() ** 2):
		movement.hamilton(0, 0, get_world_size())

def check():
	if get_ground_type() == Grounds.Grassland:
		till()

	if get_water() < 0.6:
		use_item(Items.Water)

def default(start_x, start_y, size):
	movement.to(start_x, start_y)
	
	for i in range(0, size ** 2):
		check()
		if can_harvest():
			harvest()
	
		x, y = get_pos_x(), get_pos_y()

		if (x + y) % 2 == 1:
			if (x + y) % 4 == 3:
				plant(Entities.Tree)
			else:
				plant(Entities.Carrot)
		else:
			plant(Entities.Grass)
	
		movement.hamilton(start_x, start_y, size)

def tree(start_x, start_y, size):
	movement.to(start_x, start_y)
	check()
	
	for i in range(0, size ** 2):
		if (can_harvest() == False) and (get_entity_type() == Entities.Tree):
			use_item(Items.Fertilizer)
		harvest()
		if (get_pos_x() + get_pos_y()) % 2 == 0:
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)
		movement.hamilton(start_x, start_y, size)
		check()

def pumpkin(start_x, start_y, size):
	movement.to(start_x, start_y)
	check()
	dead_pumpkins = []
	
	for i in range(0, size ** 2):
		plant(Entities.Pumpkin)
		position = (get_pos_x(), get_pos_y())
		dead_pumpkins.append(position)
		movement.hamilton(start_x, start_y, size)
		check()
	
	while(len(dead_pumpkins) != 0):
		pop_list = []
		for i in range(0, len(dead_pumpkins)):
			x, y = dead_pumpkins[i]
			movement.to(x, y)
			check()
			if (get_entity_type() == Entities.Pumpkin) and can_harvest():
				pop_list.append(i)
			else:
				plant(Entities.Pumpkin)
		while(len(pop_list) != 0):
			dead_pumpkins.pop(pop_list[len(pop_list) - 1])
			pop_list.pop(len(pop_list) - 1)
	
	harvest()

def sunflower(start_x, start_y, size):
	movement.to(start_x, start_y)
	check()
	sequence = []
	
	for i in range(0, size ** 2):
		plant(Entities.Sunflower)
		petal_coordinate = (measure(), get_pos_x(), get_pos_y())
		sequence.append(petal_coordinate)
		movement.hamilton(start_x, start_y, size)
		check()
		
	while(len(sequence) != 0):
		max_petal = 0
		for i in range(0, len(sequence)):
			petal, x, y = sequence[i]
			if petal > max_petal:
				max_petal, pop_i = petal, i
				target_x, target_y = x, y
		movement.to(target_x, target_y)
		check()
		sequence.pop(pop_i)
		if can_harvest() == False:
			use_item(Items.Fertilizer)
		harvest()

def cactus(start_x, start_y, size):
	movement.to(start_x, start_y)
	check()
	
	for i in range(0, size ** 2):
		plant(Entities.Cactus)
		movement.hamilton(start_x, start_y, size)
		check()

	for row in range(0, size):
		row_y = start_y + row
		left = 0
		right = size - 1
		
		while left < right:
			flag = False
			
			for j in range(left, right):
				movement.to(start_x + j, row_y)
				if measure() > measure(East):
					swap(East)
					flag = True
			right -= 1
	
			for j in range(right, left, -1):
				movement.to(start_x + j, row_y)
				if measure(West) > measure():
					swap(West)
					flag = True
			left += 1
			
			if flag == False:
				break
	
	for column in range(0, size):
		column_x = start_x + column
		top = 0
		bottom = size - 1
		
		while top < bottom:
			flag = False
			
			for j in range(top, bottom):
				movement.to(column_x, start_y + j)
				if measure() > measure(North):
					swap(North)
					flag = True
			bottom -= 1
			
			for j in range(bottom, top, -1):
				movement.to(column_x, start_y + j)
				if measure(South) > measure():
					swap(South)
					flag = True
			top += 1
			
			if flag == False:
				break
	
	harvest()

def weird_substance(start_x, start_y):
	movement.to(start_x, start_y)
	plant(Entities.Tree)
	use_item(Items.Fertilizer)
	if can_harvest():
		harvest()