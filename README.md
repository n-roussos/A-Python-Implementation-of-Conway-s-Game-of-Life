# A Python Implementation of Conway's Game of Life
This repository contains a GUI implementation of Conway's Game of Life using Python 2.7 and [Tkinter](https://docs.python.org/2/library/tkinter.html). This work was inspired by this [online application](https://playgameoflife.com/).

## A few words about Game of Life
[Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) was designed by John Conway in 1970. This game contains an infinite grid of cells which are either alive (black) or dead (white). The rules are the following:
1. Any live cell with two or three live neighbor survives.
2. Any dead cell with three live neighbors becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

A generation is an iteration of the infinite grid applying the above rules.
These rules are reminiscent of life as:
- Rule #1 is survival. A cell living in local community/neighborhood survives.
- Rule #2 is reproduction. A dead cell becomes alive if it has enough alive neighbors
- Rule #3 is overpopulation/underpopulation. If a cell has too many alive neighbors (overpopulation), it dies. Similarly, if a dead cell has not enough alive neighbors (underpopulation), it remains dead.
 
So, it turns out that Game of Life is not a coincidental name.

## About the application
This application enables the user to not only paint their own patterns/shapes, but also choose from pre-built ones, such as [Gosper Gliding Gun](https://conwaylife.com/wiki/Gosper_glider_gun). Moreover, there are other features such as setting the speed of the simulation etc. The application GUI offers instructions to the user and explains the game's rules (see Application Pics).

## Useful links
1. [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
2. [Life wiki](https://www.conwaylife.com/wiki/Main_Page)
3. [Inventing Game of Life (John Conway) - Numberphile](https://www.youtube.com/watch?v=R9Plq-D1gEk)
4. [Stephen Hawkings The Meaning of Life (John Conway's Game of Life segment)](https://www.youtube.com/watch?v=CgOcEZinQ2I&list=FLwikA_t8e6TSJW-L-lAHkKw)
---

### Author
**Nick Roussos** (Dipl. Eng. Electrical and Computer Engineering Department, Univ. of Patras, Greece)
  - Email: nroussos97 [at] gmail.com
  - [LinkedIn profile](https://www.linkedin.com/in/nick-roussos-205)

