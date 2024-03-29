using MTH229
using Plots


f(x) = sin(x)/x
c, δ = 0, pi/2
plot(f, c - δ, c + δ)


g(x) = (x^2 - 3x + 2) / (x^2 - 6x + 5)
c1 = 2
g(c1)

###################################
# lim       x^2 - 3x + 2
# x -> 2    ------------
#           x^2 - 6x + 5
######################################
c1, δ1 = 1, 3
plot(g, c1 - δ1, c1 + δ1)


cosf(x) = (x^2 - 3x + 2) / (x^2 - 6x + 5)
c2 = 2
cosf(c1)

###################################
# lim       cos(x) - 1
# x -> 0    ------------
#                x
###################################
c2, δ2 = 0, pi/2
plot(g, c2 - δ2, c2 + δ2)


trying(x) = (x^2 - 3x + 2)

###################################
# lim       x^2 - 3x + 2
# x -> 2 
######################################
c3, δ3 = 2, 1
plot(trying, c3 - δ3, c3 + δ3)

sd(x) = (x - 1)/(x^2 + x -2)

lim(sd, 1)
limit(sd, 1)

plot(sd, 1 - 1, 1 + 1)
