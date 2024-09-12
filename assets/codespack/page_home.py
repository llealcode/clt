import flet as ft


class Titulo(ft.Text):

    def __init__(self, texto: str):
        self.texto = texto

        super().__init__(
            value=self.texto,
            weight=ft.FontWeight.BOLD,
            size=20,
            color=ft.colors.with_opacity(opacity=0.70, color=ft.colors.WHITE)
        )


class SubTitulo(ft.Text):

    def __init__(self, texto: str):
        self.texto = texto

        super().__init__(
            value=self.texto,
            weight=ft.FontWeight.BOLD,
            size=12,
            color=ft.colors.with_opacity(opacity=0.70, color=ft.colors.WHITE)
        )


class TxtCampo(ft.Column):

    def __init__(self, texto, prefix=None):
        self.texto = texto
        self.prefix = prefix
        
        super().__init__(
            controls=[
                ft.Text(value=self.texto, size=13, color=ft.colors.WHITE),
                ft.TextField(
                    height=45,
                    prefix_text=self.prefix,
                    content_padding=ft.padding.symmetric(horizontal=10),
                    border_radius=ft.border_radius.all(3),
                    border_width=0.5,
                    #border_color=ft.colors.GREY_500,
                    border_color=ft.colors.ORANGE_500,
                    focused_border_width=1,
                    focused_border_color=ft.colors.GREEN_400,
                    text_align=ft.TextAlign.START,
                    keyboard_type=ft.KeyboardType.NUMBER,
                    cursor_color=ft.colors.GREY_300,
                    cursor_width=0.7
                )
            ],
            spacing=7
        )


class BotaoCalcular(ft.ElevatedButton):

    def __init__(self, controles: list):
        self.resultado = controles[0]
        self.salario = controles[1]
        self.jornada = controles[2]
        self.horas = controles[3]
        self.adicional = controles[4]

        def calcular(e):

            salario = float(self.salario.controls[1].value)
            jornada = int(self.jornada.controls[1].value)
            horas = int(self.horas.controls[1].value)
            adicional = int(self.adicional.controls[1].value)

            soma = float(((salario/jornada)*horas)*(1+(adicional/100)))
            total = str(f'{soma:.2f}').replace('.', ',')

            self.resultado.value = f'Total: R$ {total}'
            self.resultado.color = ft.colors.GREEN
            self.resultado.update()            

        super().__init__(
            text='Calcular',
            icon=ft.icons.CALCULATE_ROUNDED,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.GREEN,
                color=ft.colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=5),
            ),
            width=370,
            height=45,
            on_click=calcular
        )


class Resultado(ft.Text):

    def __init__(self, valor=0):
        
        super().__init__(
            value=valor,
            size=30,
            color=ft.colors.TRANSPARENT,
            weight=ft.FontWeight.BOLD
        )

        self.valor=valor


class ViewHome(ft.Container):

    def __init__(self, page):

        self.resultado = Resultado()
        self.salario = TxtCampo(texto='Salário bruto', prefix='R$ ')
        self.jornada = TxtCampo(texto='Jornada mensal')
        self.horas = TxtCampo(texto='Horas extras')
        self.adicional = TxtCampo(texto='% adicional', prefix='% ')

        self.controles = [self.resultado, self.salario, self.jornada, self.horas, self.adicional]

        super().__init__(
            content=ft.Column(
                controls=[
                    ft.Row(controls=[Titulo(texto='Cálculo de hora extra')]),
                    ft.Row(controls=[SubTitulo(texto='Valor total a receber em extras ao final do mês')]),
                    ft.Container(content=self.salario, margin=ft.margin.only(top=40)),
                    ft.Container(content=self.jornada, margin=ft.margin.only(top=20)),
                    ft.Container(content=self.horas, margin=ft.margin.only(top=20)),
                    ft.Container(content=self.adicional, margin=ft.margin.only(top=20)), 
                    ft.Row(controls=[ft.Container(content=BotaoCalcular(self.controles), margin=ft.margin.only(top=30))], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[ft.Container(content=self.resultado, margin=ft.margin.only(top=50))], alignment=ft.MainAxisAlignment.CENTER)
                ],
                spacing=0
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.with_opacity(opacity=0.10, color=ft.colors.WHITE12),
            padding=ft.padding.symmetric(vertical=10, horizontal=20),
            height=page.height*0.88
    )
