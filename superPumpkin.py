import movement

def row():
	dead_pumpkins = []
	
	for i in range(0, get_world_size()):
		movement.check()
		plant(Entities.Pumpkin)
		position = (get_pos_x(), get_pos_y())
		dead_pumpkins.append(position)
		move(East)
	
	while(len(dead_pumpkins) != 0):
		pop_list = []
		for i in range(0, len(dead_pumpkins)):
			x, y = dead_pumpkins[i]
			movement.to(x, y)
			movement.check()
			if (get_entity_type() == Entities.Pumpkin) and can_harvest():
				pop_list.append(i)
			else:
				plant(Entities.Pumpkin)
		while(len(pop_list) != 0):
			dead_pumpkins.pop(pop_list[len(pop_list) - 1])
			pop_list.pop(len(pop_list) - 1)

def main(repeats, thread):
	movement.to(0, 0)
	for count in range(0, repeats):
		for i in range(0, thread):
			move(North)
			spawn_drone(row)
		
		row()
	
	while(num_drones() != 1):
		pass
		
	harvest()