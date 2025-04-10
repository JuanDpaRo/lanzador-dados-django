import random
from django.shortcuts import render

def lanzar_dados(request):
    resultados = []
    dados_visuales = []
    cantidad = 0

    caras = {
        1: "⚀",
        2: "⚁",
        3: "⚂",
        4: "⚃",
        5: "⚄",
        6: "⚅"
    }

    if request.method == 'POST':
        print("POST recibido")
        cantidad = int(request.POST.get('cantidad', 1))
        resultados = [random.randint(1, 6) for _ in range(cantidad)]
        dados_visuales = [caras[num] for num in resultados]

    return render(request, 'dados/lanzador.html', {
        'resultados': resultados,
        'dados_visuales': dados_visuales,
        'cantidad': cantidad
    })

