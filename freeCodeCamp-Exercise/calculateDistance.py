def calDist(startDirection, commands):
    mypoint = {'x':0, 'y':0}
    currentDir = startDirection
    for command in commands:
        if currentDir== "left":
            if command[0] == 'L':
                mypoint["y"] += -1 * command[1]
                currentDir = "down"
            elif command[0] == 'R':
                mypoint["y"] += 1 * command[1]
                currentDir = "up"
        elif currentDir == "down":
            if command[0] == 'L':
                mypoint["x"] += 1 * command[1]
                currentDir = "right"
            elif command[0] == 'R':
                mypoint["x"] += -1 * command[1]
                currentDir = "left"
        elif currentDir == "right":
            if command[0] == 'L':
                mypoint["y"] += 1 * command[1]
                currentDir = "up"
            elif command[0] == 'R':
                mypoint["y"] += -1 * command[1]
                currentDir = "down"
        elif currentDir == "up":
            if command[0] == 'L':
                mypoint["x"] += -1 * command[1]
                currentDir = "left"
            elif command[0] == 'R':
                mypoint["x"] += 1 * command[1]
                currentDir = "right"
    return (mypoint['x'] ** 2 + mypoint['y'] ** 2) ** 0.5

if __name__ == "__main__":
    # sample commands inputs from the meeting
    commands = [("L",2), ("R",3),("L",4),("L",6)]
    #commands = [("L",1), ("L",1),("L",1),("L",1)]
    # directions are always "up", "down", "left", or "right"
    direction = "up"
    distance = calDist(direction, commands)
    print(distance)