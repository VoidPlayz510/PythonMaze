def main():
    # Test class to ensure that the program will run anything before jumping into code.
    print("x")
    # Define variables and any needed external classes for the project
    # ---- <IMPORT FUNCTIONS & LIBRARIES> ----
    from pyamaze import maze, COLOR, agent, textLabel
    # ---- <LOAD AND OPEN> ----

    # define size
    m = maze(5, 5)

    # create maze shapes and loops
    m.CreateMaze(loopPercent=100, theme=COLOR.dark)

    a = agent(m, shape='arrow', footprints=True)

    # labels
    l1 = textLabel(m, 'Total Cells', m.rows*m.cols)

    # debug maze ui as dictionary path
    m.tracePath({a: m.path}, delay=100, kill=True, showMarked=True)

    # compile and run
    m.run()
    print(f'Maze Map ({m.maze_map}')


if __name__ == '__main__':
    main()
