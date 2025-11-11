def check():
	if get_ground_type() == Grounds.Grassland:
		till()

	if get_water() < 0.6:
		use_item(Items.Water)

def hamilton(start_x, start_y, size_x, size_y):
	x, y = get_pos_x(), get_pos_y()
	
	if x == start_x and y < start_y + size_y - 1:
		flag = move(North)
	elif x == start_x + size_x - 1 and y > start_y:
		flag = move(South)
	elif y == start_y:
		flag = move(West)
	else:
		if (x + start_x) % 2 == 0:
			if y == start_y + size_y - 1:
				flag = move(East)
			else:
				flag = move(North)
		else:
			if y == start_y + 1:
				flag = move(East)
			else:
				flag = move(South)
	
	return flag

def to(x, y):	
	while(get_pos_x() != x):
		if get_pos_x() < x:
			move(East)
		else:
			move(West)
	while(get_pos_y() != y):
		if get_pos_y() < y:
			move(North)
		else:
			move(South)