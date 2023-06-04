# Chapter 8: Computing the ETH Price

Now let's get back to how you're going to compute the ETH price. The way we'll go about it is to calculate the **average** of the set of responses.

While calculating the average is not complicated, bear in mind that this method can make your contract vulnerable to attacks if a few oracles decide to manipulate the price. This is not an easy problem, and the solution is beyond the scope of this lesson. One way to solve this would be to **remove the outliers by using quartiles and interquartile ranges**. You can refer to <a href="https://www.mathsisfun.com/data/quartiles.html" target=_new>Quartiles page</a> from the **"Math is Fun website"** for more details. Since we're building an oracle for demo purposes, we're going to accept this tradeoff of using an algorithm that is simple to implement, knowing that it isn't totally secure.

To calculate the average of the set of responses, you'll have to use a `for` loop.

As an example, the syntax for calculating the sum of all the elements of an array is as follows:

```Solidity
uint sum = 0;
for (uint f=0; f < myArray.length; f++) {
    sum +=  myArray[f];
}
```

In this example, `f` is a variable that contains the current item from `myArray`. The code in the body of the `for` loop uses `f` to calculate `sum`.


## Put It to the Test

Let's write a `for` loop that iterates through all the responses for a particular `id`, and calculates their sum. Then, you'll divide that by `numResponses` to get the average.

1. Initialize a `uint` called `computedEthPrice` and set it equal to `0`.

2. Declare a `for` loop that starts from `uint f=0` and goes up through `f < requestIdToResponse[_id].length`.

3. Inside the `for` loop, use `+=` to add `requestIdToResponse[_id][f].ethPrice`  to `computedEthPrice`.

4. Calculate the average by dividing `computedEthPrice` to `numResponses`. Store the result in `computedEthPrice`.
