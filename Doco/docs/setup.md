# __Maze Setup__

## Installing and importing

> First in 'CMD' run the command
```py
pip install Pyamaze
```

> In your new python file enter the following code:

```py
def main():

	# A test print to make sure the program is running as expected
	print("test")
	from pyamaze import maze, COLOR, agent, textLabel



if __name__ == '__main__':
	main()
```

## Creating a maze

> Paste the following code into the main method to generate a 5 x 5 maze.
```py
    m = maze(5, 5)
    m.CreateMaze(loopPercent=100, theme=COLOR.dark)
    a = agent(m, shape='arrow', footprints=True)
```

### Adding Labels


```py
    # labels
    l1 = textLabel(m, 'Total Cells', m.rows*m.cols)
```

## Traverse the maze
> Paste the following code into the main method to have the agent traverse our maze and then hit 'run'.

```py
    m.tracePath({a: m.path}, delay=100, kill=True, showMarked=True)
    m.run()
    print(f'Maze Map ({m.maze_map}')
```

### Output
> A UI should have popped up like the screenshot below.

![MazeTest](Assets\maze.png)

> The console should have also logged something similar to this.

![MazeLog](Assets\123.png)

> The successfully traveresed map

![MazeTest](Assets\Mazetest.png)