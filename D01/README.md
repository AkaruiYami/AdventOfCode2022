# Day 1

## Preparation

First, we read the input data as a single string. Then we split this string for every 2 newlinew (`"\n\n"`). We will get a list of string that represents the elves inventory data as such:

```
['6471\n1935\n1793\n3843\n6059\n6736\n6101\n3133\n6861\n1330\n1962\n5538\n6760', '5212\n2842\n3684\n6198\n6198\n3440\n2179\n1432\n5647\n5324\n6331\n4061\n1167\n1821', ...]
```

now, using list comprehension, we can process these data into sum of calories that each of the elf has in their inventory. To do that, we replace newline character (`"\n"`) from their data string to plus symbol (`"+"`) and evaluate those string using `eval()` function.

The other way we can do for this is, we split each string data by the newline character (`"\n"`) and give them to `sum()` function. Either way, works to find the total calories each elf has.

This information will be stored in `elves` variable.

## Part 1

For part 1, we just find the mazimum value by using `max()` function.

## Part 2

We sort the `elves` list in descending order. Then we just find the the total summation of the first 3 elements from that list using index slicing and `sum()` function.

[<sup>< main page](../README.md#My-Attempt-in-AoC-2022)
