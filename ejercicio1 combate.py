def calcular_dano(ataque, defensa):
    dano = ataque - defensa
    if dano < 0:
        return 0
    return dano
def aplicar_dano(hp_actual, dano):
    nuevo = hp_actual - dano
    if nuevo < 0:
        return 0
    return nuevo

def mostrar_estado(nombre, hp, hp_max=100):
    print(f"{nombre}: {hp}/{hp_max}")


def realizar_ataque(atacante, defensor, dano):
    print(f"{atacante} ataca a {defensor} por {dano} de dano!")


hp_heroe = 100
hp_enemigo = 50

mostrar_estado("Heroe", hp_heroe)
mostrar_estado("Enemigo", hp_enemigo)

dano = calcular_dano(25, 10)

realizar_ataque("Heroe", "Enemigo", dano)
hp_enemigo = aplicar_dano(hp_enemigo, dano)
mostrar_estado("Enemigo", hp_enemigo)

realizar_ataque("Heroe", "Enemigo", dano)
hp_enemigo = aplicar_dano(hp_enemigo, dano)
mostrar_estado("Enemigo", hp_enemigo)

