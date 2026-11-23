"""
Fase 5 - Evaluación Final POA
Curso: Fundamentos de Programación - Código 213022
Problema 4: Conteo de títulos populares y actuales en una videoteca digital

El programa cuenta los títulos que cumplen simultáneamente:
- Calificación mayor o igual al umbral definido.
- Año de lanzamiento mayor o igual al año límite establecido.
"""

# Matriz: [Título, Año de lanzamiento, Calificación (1 a 10), Género]
videoteca = [
    ["Horizonte Azul", 2022, 9.1, "Ciencia ficción"],
    ["La última estación", 2018, 8.7, "Drama"],
    ["Código perdido", 2021, 8.4, "Suspenso"],
    ["Rutas del tiempo", 2020, 7.8, "Aventura"],
    ["El jardín secreto", 2023, 9.5, "Fantasía"],
    ["Noche de verano", 2019, 7.2, "Romance"],
    ["Misión orbital", 2024, 8.2, "Ciencia ficción"],
    ["Voces lejanas", 2021, 6.9, "Drama"]
]

# Criterios definidos para el análisis
CALIFICACION_MINIMA = 8.0
ANIO_LIMITE = 2020


def contar_titulos_destacados(matriz, calificacion_minima, anio_limite):
    """
    Cuenta títulos que cumplen simultáneamente los dos criterios:
    calificación >= calificacion_minima y año >= anio_limite.
    """
    contador = 0

    for titulo in matriz:
        anio = titulo[1]
        calificacion = titulo[2]

        if calificacion >= calificacion_minima and anio >= anio_limite:
            contador += 1

    return contador


def mostrar_resultados(matriz, calificacion_minima, anio_limite):
    """Muestra los títulos evaluados y el total que cumple ambos criterios."""
    print("=" * 78)
    print("             INFORME DE POPULARIDAD Y ACTUALIDAD DE LA VIDEOTECA")
    print("=" * 78)
    print(f"Criterios: calificación mínima = {calificacion_minima:.1f} | año mínimo = {anio_limite}")
    print("-" * 78)
    print(f"{'Título':<24}{'Año':>8}{'Calificación':>16}{'Género':>22}{'Cumple':>10}")
    print("-" * 78)

    for titulo in matriz:
        nombre = titulo[0]
        anio = titulo[1]
        calificacion = titulo[2]
        genero = titulo[3]

        cumple = calificacion >= calificacion_minima and anio >= anio_limite
        estado = "Sí" if cumple else "No"

        print(f"{nombre:<24}{anio:>8}{calificacion:>16.1f}{genero:>22}{estado:>10}")

    total = contar_titulos_destacados(matriz, calificacion_minima, anio_limite)

    print("-" * 78)
    print(f"Total de títulos que cumplen ambos criterios: {total}")
    print("=" * 78)


if __name__ == "__main__":
    mostrar_resultados(videoteca, CALIFICACION_MINIMA, ANIO_LIMITE)
