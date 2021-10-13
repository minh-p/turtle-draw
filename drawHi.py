from SimpleTurtle import SimpleTurtle

drawer = SimpleTurtle()
drawer.alter([
    ["right", 90],
    ["forward", 100],
    ["backward", 50],
    ["left", 90],
    ["forward", 50],
    ["right", 90],
    ["forward", 50],
    ["backward", 100],
    ["left", 90],
    ["penup"],
    ["forward", 50],
    ["right", 90],
    ["pendown"],
    ["forward", 100],
    ["penup"],
    ["left", 90],
    ["forward", 90],
 ])
drawer.exitonclick()
