import flet as ft


class AlertaCalculoHorasExtras(ft.AlertDialog):

    def __init__(self, titulo: str):

        super().__init__(
            modal=False,
            bgcolor=ft.colors.BLACK26,
            title=ft.Text(value=titulo, color=ft.colors.WHITE, weight=ft.FontWeight.W_500, size=14),
            content=ft.Container(
                bgcolor=ft.colors.GREY,
                height=200,
                width=200
            )
        )
