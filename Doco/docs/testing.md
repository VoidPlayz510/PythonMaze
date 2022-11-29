# __Unittesting__

> If you want to test whether or not the agent(path follower) is
> in the correct start location, end location refer to below.


## Setup

> In our old code add the following
```py
import unittest

class TestPositionsMaze(unittest.TestCase):
	    def test_startPos(self):
        self.assertEqual("xe", "xe")
```

## Start Test

> Next add the following to the start test
```py
        m = maze(5, 5)
        start = (m.rows, m.cols)

        m.CreateMaze(saveMaze=True)
        path = DFS(m)
        a = agent(m, footprints=True)
        self.assertEqual(a.position, start)
        print('start ' f'{start}', 'position' f'{a.position}')
        # m.tracePath({a: path}, delay=100, showMarked=True, kill=True)
        # Test maze
```

## End Test
> For testing the end position add the following to the end test
```py
    def test_endPos(self):
        m = maze(5, 5)
        end = (1, 1)

        m.CreateMaze(saveMaze=True)
        path = DFS(m)
        a = agent(m, footprints=True)
        m.tracePath({a: path}, delay=100, showMarked=True, kill=True)
        m.run()
        self.assertEqual(a.position, end)
        print('end ' f'{end}', 'position' f'{a.position}')

        # Test maze
```

## __Output__

> If the tests were successfull you should see the following result(s)
![EndResult](Assets\yay.png)