Python Encoder and Decoder for Deadfish
==============================

# Overview

Deadfish is a joke programming language.  According to the [esoteric programming language wiki](http://www.esolangs.org), a joke programming language is one that

>is not of any interest except for potential humor value. Generally speaking, it is completely unusable for programming even in theory

One such joke language is Deadfish, which got its name from

>Deadfish was originally going to be called fishheads as programming in this language is like eating raw fish heads. However, due to the limiting features of the language, programming in this language became like eating (and having to smell) dead, rotting fish heads, an experience not often generally considered pleasurable.

Nevertheless, the wiki page for Deadfish contains implementations in 65 different languages including C, C#, C++, Chicken, Clever, COBOL, and Commodore 64 BASIC to name just the C's.

There are many Deadfish interpreters, which are capable of executing deadfish-code and convert a series of `isdo`'s into ascii strings. However, I wasn't able to find any Deadfish *encoder* for generating deadfish programs (that are more sophisticated than hundreds of i's). So here we go.


# Deadfish Language Features

A Deadfish program has a single integer accumulator variable, which is initialized to zero.  The programming language defines only four operations

|cmd| description                                                                               |
|:-:|:------------------------------------------------------------------------------------------|
| i | This increments the accumulator                                                           |
| d | This decrements the accumulator                                                           |
| s | Squares the value in the accumulator                                                      |
| o | Outputs the accumulator                                                                   |

If the accumulator becomes -1 or 256, it is reset to zero.

# Implementation

There are an infinite number of ways to generate any given character. However, for efficiency, we can represent each of 256 possible accumulator states (with reset) as a vertex on a graph, and then edges denoting the various operations.

Note that it doesn't make sense to go beyond 256 by for example squaring 20 -- in order to generate anything useful, we need to decrement back to 256, which would take hundreds of operations. With this insight in mind and with the help of Dynamic Programming, we can simply run BFS on our generated graph, giving us a fast and efficient way to encode any string into Deadfish.

 -- readme adapted from [TryitOnline/deadfish~](https://github.com/TryItOnline/deadfish-)