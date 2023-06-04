# Chapter 1: Getting set up

Both Ethereum and zkSync “speak” a language called JSON-RPC that is not human-readable. Luckily, they provide libraries that hide all the complexity below the surface, so you only need to know a bit of JavaScript.

> ☞ If you are not comfortable with **JavaScript**, consider going through a tutorial elsewhere before starting this lesson.

## Initialize your Node.js project

Each Node.js project must contain at least one `package.json` file, usually located in the root directory of your project. This file identifies the project and lists the packages your project depends on, making your build reproducible.

You can create a `package.json` file by using a text editor, but the quickest way is to run the `npm init` command and pass it the `-y` flag as follows:

```shell
npm init -y
```

What is the `-y` flag, you ask?

The `-y` flag specifies that you want to accept all the defaults `npm` suggests based on information extracted from the current directory.

## Install dependencies

We assume that `npm` and `node` are installed on your computer, and now we want you to install `ethers` and `zksync`.

The syntax for installing a package using `npm` looks like this:

```shell
npm install <package-name>
```

## Put It to the Test

1. The first thing you would want to do is to initialize your new project and accept all the defaults. If you can't remember the syntax for doing this, check the example from above. But first, try to do it without peeking.

2. Now, let's use the `npm install` command to install **ethers** and **zksync**.
  > Note: It shouldn't matter the order in which you specify the packages you want to install but, since our command-line interpreter is pretty basic, it won't consider the answer correct unless you're specifying **_ethers first_**.
