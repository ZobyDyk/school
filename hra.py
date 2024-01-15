import turtle

def nastavit_okno(nazev, barva_pozadi, sirka, vyska):
    okno = turtle.Screen()
    okno.title(nazev)
    okno.bgcolor(barva_pozadi)
    okno.setup(sirka, vyska)
    return okno

def vytvorit_palku(x, y):
    palka = turtle.Turtle()
    palka.speed(0)
    palka.shape("square")
    palka.color("skyblue")
    palka.shapesize(stretch_wid=5, stretch_len=1)
    palka.penup()
    palka.goto(x, y)
    return palka

def vytvorit_micek():
    micek = turtle.Turtle()
    micek.speed(0)
    micek.shape("circle")
    micek.color("violet")
    micek.penup()
    micek.goto(0, 0)
    return micek

def pohyb_palky(palka, smer):
    y = palka.ycor()
    y += smer
    if y > 250:
        y = 250
    elif y < -250:
        y = -250
    palka.sety(y)

def priradit_klavesy(okno, leva_palka, prava_palka):
    okno.listen()
    okno.onkeypress(lambda: pohyb_palky(leva_palka, 20), 'w')
    okno.onkeypress(lambda: pohyb_palky(leva_palka, -20), 's')
    okno.onkeypress(lambda: pohyb_palky(prava_palka, 20), 'Up')
    okno.onkeypress(lambda: pohyb_palky(prava_palka, -20), 'Down')

def vytvorit_skore_tabuli():
    skore_tabule = turtle.Turtle()
    skore_tabule.speed(0)
    skore_tabule.color("white")
    skore_tabule.penup()
    skore_tabule.hideturtle()
    skore_tabule.goto(0, 260)
    skore_tabule.write("Levá: 0  Pravá: 0", align="center", font=("Courier", 24, "normal"))
    return skore_tabule

# Skóre
skore_leva = 0
skore_prava = 0

def main():
    global skore_leva, skore_prava
    okno = nastavit_okno("Lojzova a Dominikova hra", "black", 800, 600)
    leva_palka = vytvorit_palku(-350, 0)
    prava_palka = vytvorit_palku(350, 0)
    micek = vytvorit_micek()
    skore_tabule = vytvorit_skore_tabuli()

    smer_micku_x = 5
    smer_micku_y = 5

    priradit_klavesy(okno, leva_palka, prava_palka)

    while True:
        okno.update()

        # Pohyb míčku
        micek.setx(micek.xcor() + smer_micku_x)
        micek.sety(micek.ycor() + smer_micku_y)

        # Hranice
        if micek.ycor() > 290 or micek.ycor() < -290:
            smer_micku_y *= -1

        # Kontrola, zda míček přesáhl pálku a aktualizace skóre
        if micek.xcor() > 390:
            skore_leva += 1
            skore_tabule.clear()
            skore_tabule.write("Levá: {}  Pravá: {}".format(skore_leva, skore_prava), align="center", font=("Courier", 24, "normal"))
            micek.goto(0, 0)
            smer_micku_x *= -1

        elif micek.xcor() < -390:
            skore_prava += 1
            skore_tabule.clear()
            skore_tabule.write("Levá: {}  Pravá: {}".format(skore_leva, skore_prava), align="center", font=("Courier", 24, "normal"))
            micek.goto(0, 0)
            smer_micku_x *= -1

        # Bourání s pálkou
        if (micek.xcor() > 340 and micek.xcor() < 350) and (micek.ycor() < prava_palka.ycor() + 50 and micek.ycor() > prava_palka.ycor() - 50) \
        or (micek.xcor() < -340 and micek.xcor() > -350) and (micek.ycor() < leva_palka.ycor() + 50 and micek.ycor() > leva_palka.ycor() - 50):
            smer_micku_x *= -1

if __name__ == "__main__":
    main()