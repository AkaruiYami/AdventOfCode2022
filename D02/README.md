# Day 2

## Preparation

For this puzzle, we will have a `MOVE_MAP` that will correspond to our movement `rock`, `paper`, `scissors`, and the outcome `lose`, `draw`, `win`.

For both part 1 and 2, we need to find 2 things which are: - outcome score - move score / shape score

After getting those 2 things, we can calculate the total score

## Part 1

In this part, the 2nd element of `MOVE_MAP` represent our movement which is `X = rock`, `Y = paper`, and `Z = scissors`. We need to determine if we are lose, draw, or win base on the combination of opponent's movement and our movement.

First, we can check for draw because it is the easiest one among other two. To check for draw, we just need to compare the index of opponent's movement within MOVE_MAP[0] and our movement within MOVE_MAP[1]. We can use `index()` method to get the index of the corresponding move.

-   A is at index 0 inside MOVE_MAP[0]
-   B is at index 1 inside MOVE_MAP[0]
-   C is at index 2 inside MOVE_MAP[0]
-   X is at index 0 inside MOVE_MAP[1]
-   Y is at index 1 inside MOVE_MAP[1]
-   Z is at index 2 inside MOVE_MAP[1]

To do that, we will rotate our `MOVE_MAP[1]` so the position of each items will match winning pair with `MOVE_MAP[0]`.

Winning Pair:

| Opponent | Our |
| -------- | --- |
| A        | Y   |
| B        | Z   |
| C        | X   |

Base on table above, we need to rotate our `MOVE_MAP[1]` to the left by 1.

```
MOVE_MAP[1] = X, Y, Z
--- rotate MOVE_MAP[1] to the left by 1 ---
MOVE_MAP[1] = Y, Z, X
```

Now, if we combine MOVE_MAP[0] and MOVE_MAP[1] together, we will get winning pair:

```python
winning_pair = zip(MOVE_MAP[0], MOVE_MAP[1])
# produce: winning_pair = (A, Y), (B, Z), (C, X)
```

Now, after checking for draw and win conditions, if both of the check failed, then the remaining can be consider as losing.

After getting the outcome score, we now can look for move score which is very straight forward. We just need to return the index of our movement + 1.

## Part 2

For part 2, getting the outcome score is very simple. Since now, `X = lose`, `Y = draw`, and `Z = win`. We can just get the index of those elements and return the index times 3 because:

| Element | Index | Index \* 3 |
| ------- | ----- | ---------- |
| X       | 0     | 0          |
| Y       | 1     | 3          |
| Z       | 2     | 6          |

Then, we need to get the move score. First, we check. If it is draw, then we will return the index of opponent's move + 1 because in order to draw, we need to use the exact same move that opponent use.

After that, we check if we need to win in that round. If it is true, we will rotate the MOVE_MAP[0] by 1 to the right.

```
MOVE_MAP[0] = A, B, C
MOVE_MAP[0] = C, A, B
```

The reason why we rotate the movement set to the right instead of left is because, we need to find the index of winning movement. Therefore, if opponent use `A`, then the index of winning position will be `1` which is where `B` is at in the original MOVE_MAP[0]. So, by rotating the movement set to the right by 1, `A` will now relocate to `B`'s position and if we find the index of `A` using `index()` method, we will get `1`.

|          | Rock | Paper | Scissors |
| -------- | ---- | ----- | -------- |
| Opponent | A    | B     | C        |
| Our      | C    | A     | B        |

After finding the index, we will return index + 1 in order to get the score for that movement.

When both draw and win check failed, we can consider the remaining input as losing. For losing, we need to rotate MOVE_MAP[0] by 1 to the left. After getting the index, we then return index + 1 as well.

[<sup>< main page](../README.md#My-Attempt-in-AoC-2022)
