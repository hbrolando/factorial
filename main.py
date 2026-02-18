from nicegui import ui
with ui.card().classes():
    # Suma de dos numeros
    ui.label('FACTORIAL').classes('self-center text-sky-600 font-bold').style('font-size: 50px')
    ui.image(source='https://img.freepik.com/vetores-premium/ilustracao-matematica-ilustracao-de-formas-geometricas_611881-395.jpg?w=2000')
    
    #Funcion factorial
    def factorial():
        try:
            nro = int(textBox1.value or 0)
            if nro <0:
                resultado.text = f'Error numero {nro} es negativo'
            else:
                calc = 1
                for i in range(2, nro +1):
                    calc*=i
                resultado.text = f'Factorial del {nro} = {calc}'
        
        except ValueError:
            resultado.text = "Error ingrese un numero entero"

    #Introducimos nro
    textBox1 = ui.input(placeholder='Ingrese numero').classes('w-full')
    
    #Realizamos la operacion llamando a la funcion
    ui.button("Calcular Factorial", on_click=factorial).classes('self-center w-full')
    
    def limpiar():
        textBox1.value = ''
        resultado.text = ''

    ui.button("limpiar", on_click=limpiar).classes('self-center w-full')
    resultado = ui.label('Resultado: 0')

ui.run()


