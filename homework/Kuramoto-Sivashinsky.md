1.  Write a pseudospectral solver for the Kuramoto-Sivashinsky equation:

$$
u_t + u_{xx} + u_{xxxx} + uu_x = 0.
$$

You will want to use some approach that allows you to take $\Delta t = O(\Delta x$.

2.  Investigate solutions of this equation, with different initial conditions and different sizes of the spatial domain.  Are there steady states?  Traveling waves?  Are the solutions periodic in time?
See if you can find solutions that are not periodic in time, or solutions that seem periodic for a long time but then exhibit non-periodic behavior.

Some hints:
- It may be more helpful to look at the solution as a 2-dimensional `pcolor` plot (with axes $x$ and $t$) instead of as an animation.
- 256 or perhaps 512 points in space is usually enough to resolve the solution
- If you don't see interesting behavior, keep increasing the overall spatial domain size and/or the final time.  You might need to simulate up to e.g. $t=1000$ to see some behaviors.
