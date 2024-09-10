import flet as ft


class MenuBottom(ft.BottomAppBar):
    
    def __init__(self, page):

        super().__init__(
            content=ft.Row(
                controls=[
                    BotoesMenu(texto='Horas', icone=ft.icons.TIMER_ROUNDED),
                    BotoesMenu(texto='Férias', icone=ft.icons.BEACH_ACCESS_ROUNDED),
                    BotoesMenu(texto='Rescisão', icone=ft.icons.POWER_OFF_ROUNDED),
                    BotoesMenu(texto='13º', icone=ft.icons.MONETIZATION_ON_ROUNDED)
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            ),
            bgcolor=ft.colors.BLACK45,
            height=page.height*0.12
        )


class BotoesMenu(ft.IconButton):

    def __init__(self, texto, icone):
        self.texto = texto
        self.icone = icone

        super().__init__(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Icon(name=self.icone, color=ft.colors.WHITE),
                        ft.Text(value=self.texto, color=ft.colors.WHITE)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        )
