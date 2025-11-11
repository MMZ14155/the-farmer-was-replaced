import movement

def maze(start_x, start_y, size, rounds=1):
	clear()
	center_x = start_x + size // 2
	center_y = start_y + size // 2
	movement.to(center_x, center_y)
	
	substance = size * (2 ** (num_unlocked(Unlocks.Mazes) - 1))
	if num_items(Items.Weird_Substance) < substance * rounds:
		return substance * rounds
	
	entity_type = get_entity_type()
	if entity_type != Entities.Hedge and entity_type != Entities.Treasure and measure() == None:
		plant(Entities.Bush)
		while(can_harvest() == False):
			use_item(Items.Fertilizer)
		use_item(Items.Weird_Substance, substance)
	
	directions = [North, East, South, West]
	current_dir = 0

	while True:
		if get_entity_type() == Entities.Treasure:
			harvest()
			break
			
		right_dir = (current_dir + 1) % 4
		
		if can_move(directions[right_dir]):
			move(directions[right_dir])
			current_dir = right_dir
		elif can_move(directions[current_dir]):
			move(directions[current_dir])
		else:
			left_dir = (current_dir - 1) % 4
			move(directions[left_dir])
			current_dir = left_dir
	
	return 0

def snake(size):
	clear()
	movement.to(0, 0)
	change_hat(Hats.Dinosaur_Hat)
	flag = 1
	
	while(flag == 1):
		flag = movement.hamilton(0, 0, size, size)
	
	change_hat(Hats.Straw_Hat)