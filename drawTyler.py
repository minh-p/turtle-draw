from SimpleTurtle import SimpleTurtle

turtleDrawer = SimpleTurtle()
drawing = turtleDrawer.stateChange

# Go backward to create space
turtleDrawer.alter([
    ["penup"],
    ["backward", 400]
])

# T
turtleDrawer.alter([
    ["pendown"],
    ["forward", 100],
    ["penup"],
    ["backward", 50],
    ["pendown"],
    ["right", 90],
    ["forward", 100],
    ["penup"]
])

# Spacing
turtleDrawer.alter([["backward", 100], ["left", 90], ["forward", 100]])

# Y
turtleDrawer.alter([
    ["pendown"],
    ["right", 45],
    ["forward", 50],
    ["left", 90],
    ["forward", 50],
    ["penup"],
    ["backward", 50],
    ["right", 135],
    ["pendown"],
    ["forward", 60]
])

# create space
turtleDrawer.alter([
    ["penup"],
    ["left", 90],
    ["forward", 100]
])

# L
turtleDrawer.alter([
    ["pendown"],
    ["forward", 50],
    ["penup"],
    ["backward", 50],
    ["pendown"],
    ["left", 90],
    ["forward", 100]
])

# create space
turtleDrawer.alter([
    ["penup"],
    ["right", 90],
    ["forward", 100]
])

# E
turtleDrawer.alter([
    ["pendown"]
])

for _ in range(2):
    turtleDrawer.alter([
        ["forward", 50],
        ["penup"],
        ["backward", 50],
        ["right", 90],
        ["pendown"],
        ["forward", 50],
        ["left", 90]
    ])

turtleDrawer.alter([["forward", 50]])

# create space
turtleDrawer.alter([
    ["penup"],
    ["forward", 80],
    ["left", 90],
])

# R
turtleDrawer.alter([
    ["pendown"],
    ["forward", 100],
    ["right", 90],
    ["forward", 50],
    ["right", 135],
    ["forward", 60],
    ["left", 90],
    ["forward", 80]
])

turtleDrawer.exitonclick()
pri
