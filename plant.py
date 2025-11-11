import movement

def check():
	if get_ground_type() == Grounds.Grassland:
		till()

	if get_water() < 0.6:
		use_item(Items.Water)

def grass(start_x, start_y, size_x, size_y):
	movement.to(start_x, start_y)
	check()
	
	for i in range(0, size_x * size_y):
		harvest()
		plant(Entities.Grass)
		movement.hamilton(start_x, start_y, size_x, size_y)
		check()

def tree(start_x, start_y, size_x, size_y):
	movement.to(start_x, start_y)
	check()
	
	for i in range(0, size_x * size_y):
		if (can_harvest() == False) and (get_entity_type() == Entities.Tree):
			use_item(Items.Fertilizer)
		harvest()
		if (get_pos_x() + get_pos_y()) % 2 == 0:
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)
		movement.hamilton(start_x, start_y, size_x, size_y)
		check()

def carrot(start_x, start_y, size_x, size_y):
	movement.to(start_x, start_y)
	check()
	
	for i in range(0, size_x * size_y):
		harvest()
		plant(Entities.Carrot)
		movement.hamilton(start_x, start_y, size_x, size_y)
		check()

def pumpkin(start_x, start_y, size_x, size_y):
	movement.to(start_x, start_y)
	check()
	dead_pumpkins = []
	
	for i in range(0, size_x * size_y):
		plant(Entities.Pumpkin)
		position = (get_pos_x(), get_pos_y())
		dead_pumpkins.append(position)
		movement.hamilton(start_x, start_y, size_x, size_y)
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

def sunflower(start_x, start_y, size_x, size_y):
	movement.to(start_x, start_y)
	check()
	sequence = []
	
	for i in range(0, size_x * size_y):
		plant(Entities.Sunflower)
		petal_coordinate = (measure(), get_pos_x(), get_pos_y())
		sequence.append(petal_coordinate)
		movement.hamilton(start_x, start_y, size_x, size_y)
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

def weird_substance(start_x, start_y):
	movement.to(start_x, start_y)
	plant(Entities.Tree)
	use_item(Items.Fertilizer)
	if can_harvest():
		harvest()