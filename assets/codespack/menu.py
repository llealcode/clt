import flet as ft


class MenuBottom(ft.BottomAppBar):
    
    def __init__(self, page):

        super().__init__(
            content=ft.Row(
                controls=[
                    BotoesMenu(texto='Horas', icone=ft.icons.TIMER_ROUNDED, estado='ativo'),
                    BotoesMenu(texto='Férias', icone=ft.icons.BEACH_ACCESS_ROUNDED, estado='inativo'),
                    BotoesMenu(texto='Rescisão', icone=ft.icons.POWER_OFF_ROUNDED, estado='inativo'),
                    BotoesMenu(texto='13º', icone=ft.icons.MONETIZATION_ON_ROUNDED, estado='inativo')
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            ),
            bgcolor=ft.colors.BLACK45,
            height=page.height*0.12
        )


class BotoesMenu(ft.IconButton):

    def __init__(self, texto, icone, estado):
        self.texto = texto
        self.icone = icone
        self.estado = estado

        super().__init__(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Icon(name=self.icone, color=ft.colors.WHITE if not self.estado=='ativo' else ft.colors.GREEN),
                        ft.Text(value=self.texto, color=ft.colors.WHITE)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        )


class UpperAppBar(ft.AppBar):

    def __init__(self, page):

        super().__init__(
            leading=ft.Icon(ft.icons.WALLET_TRAVEL),
            leading_width=40,
            title=ft.Text("Cálculos trabalhistas"),
            center_title=False,
            bgcolor=ft.colors.with_opacity(opacity=0.3, color=ft.colors.BLACK)
        )
