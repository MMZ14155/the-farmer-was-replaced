import movement

def check():
	if get_ground_type() == Grounds.Grassland:
		till()

	if get_water() < 0.6:
		use_item(Items.Water)

def start():
	for i in range(0, get_world_size()):
		check()
		plant(Entities.Cactus)
		move(East)

def row():
	y = get_pos_y()
	left = 0
	right = get_world_size() - 1
		
	while left < right:
		flag = False
		
		for j in range(left, right):
			movement.to(j, y)
			if measure() > measure(East):
				swap(East)
				flag = True
		right -= 1
	
		for j in range(right, left, -1):
			movement.to(j, y)
			if measure(West) > measure():
				swap(West)
				flag = True
		left += 1
			
		if flag == False:
			break

def column():
	x = get_pos_x()
	top = 0
	bottom = get_world_size() - 1
		
	while top < bottom:
		flag = False
			
		for j in range(top, bottom):
			movement.to(x, j)
			if measure() > measure(North):
				swap(North)
				flag = True
		bottom -= 1
		
		for j in range(bottom, top, -1):
			movement.to(x, j)
			if measure(South) > measure():
				swap(South)
				flag = True
		top += 1
		
		if flag == False:
			break