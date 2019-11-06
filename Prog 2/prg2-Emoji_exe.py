from graphics import *

jan = GraphWin('Emoji triste com a vida', 900, 500)
centro = Point(450, 250)
circ = Circle(centro, 100)
circ.setFill('yellow')
circ.draw(jan)

globuloesquerdo = Circle(centro, 20)
globuloesquerdo.setFill('white')
globuloesquerdo.move(-30, -10)
globuloesquerdo.draw(jan)

globulodireito = globuloesquerdo.clone()
globulodireito.move(60, 0)
globulodireito.draw(jan)

olhoesquerdo = Circle(centro, 10)
olhoesquerdo.setFill('black')
olhoesquerdo.move(-30, -10)
olhoesquerdo.draw(jan)

olhodireito = olhoesquerdo.clone()
olhodireito.move(60, 0)
olhodireito.draw(jan)

lagrima = Circle(centro, 7)
lagrima.setFill('lightblue')
lagrima.move(40, 10)
lagrima.draw(jan)

lagrima1 = Circle(centro, 5)
lagrima1.setFill('lightblue')
lagrima1.move(45, 30)
lagrima1.draw(jan)

lagrima2 = Circle(centro, 3)
lagrima2.setFill('lightblue')
lagrima2.move(45, 45)
lagrima2.draw(jan)

lagrima3 = Circle(centro, 6)
lagrima3.setFill('lightblue')
lagrima3.move(45, 20)
lagrima3.draw(jan)

linha = Line(Point(275, 100), Point(200, 100))
linha.move(215, 200)
linha.draw(jan)

input("Tecle Enter para finalizar")
