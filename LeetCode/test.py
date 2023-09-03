def is_opened(number):
    
    door_state = [0 for _ in range(number+1)] 

    for entrance in range(1, number, 1):
        
        opened_doors = [entrance*(idx+1) for idx in range(number//entrance)] 
        # when entrance = 7, opened_doors = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
        for door in opened_doors:
            door_state[door] += 1 
        
    opened = [] 
    for state in door_state:
        if state % 2 == 1: # door is open 
            opened.append(True)
        else: # door is closed 
            opened.append(False)

    return opened[1:]

if __name__ == "__main__":
    
    opened_doors = is_opened(50)
    print(opened_doors)
    
    
    # 