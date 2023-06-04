# Chapter 12: Update balances

Great! You now know how to display Bob's initial balance. But every time Bob gets paid, his balance will increase. How can you make it so that the application displays the balance every time it gets updated? The short answer is that you can't because the zkSync protocol doesn’t have a proper mechanism for notifications yet.

However, instead of waiting for the zkSync protocol to push a notification every time the balance gets updated, you can regularly poll for changes, by making your application "sleep💤" for a predetermined interval of time between each call to the function that reads Bob's balance. For this, you'll use the `setInterval` function. The following example calls the `doSomething` function, with a delay of SLEEP_INTERVAL milliseconds between each function call:

```JavaScript
const SLEEP_INTERVAL = process.env.SLEEP_INTERVAL || 5000 // Expressed in milliseconds
setInterval(async () => {
 doSomething()
}, SLEEP_INTERVAL)
```

Next, we'd want to provide a way for Bob to gracefully shut down the application. This can be done by catching the `SIGINT` handler like this:

```JavaScript
process.on( 'SIGINT', () => {
 // Gracefully shut down the application
})
```

> In this tutorial, you won't use any specific instructions to gracefully shut down the application, but this may come in handy for when you'll build your own application.

That's about everything we wanted to teach you in this lesson. Time for you to write some code!

## Put it to the test

We've gone ahead and filled in almost everything, you just need to put in the finishing touch.

1. Call the `utils.displayZkSyncBalance` function. It takes two parameters: `bobZkSyncWallet` and `ethers`. Don't forget that's an `async` function, meaning that you must prepend the `await` keyword to the function call.

This concludes the shopkeeper application - well done!
