# Classes criadas
from assets.codespack.page_home import ViewHome
from assets.codespack.menu import MenuBottom, UpperAppBar

# Bibliotecas do python
import flet as ft


def layout_page(page):

    # Localidade e idioma da página
    page.locale_configuration = ft.LocaleConfiguration(supported_locales=[ft.Locale('pt', 'BR')], current_locale=ft.Locale('pt', 'BR'))

    # Posicionamento    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.maximizable = False
    page.window.resizable = True
    page.window.center()
    page.update()

    # Espaçamento e margens
    page.padding = 0
    page.spacing = 0

    # Temas e cores
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(thumb_color=ft.colors.BLUE_800)
    )

    # Fontes
    page.fonts={
        'OpenSans' : r'assets\fonts\OpenSans.ttf',
        'Sevillana' : r'assets\fonts\Sevillana.ttf'
    }

    # rotas
    class ViewsPage(ft.View):

        def __init__(self, rota, conteudo):
            self.rota = rota
            self.conteudo = conteudo

            super().__init__(
                route=self.rota,
                controls=[self.conteudo],
                padding=0,
                spacing=0,
                bottom_appbar=MenuBottom(page=page),
                appbar=UpperAppBar(page=page)
            )


    def mudar_rota(e):
        page.views.clear()
        page.views.append(ViewsPage(rota=page.route, conteudo=ViewHome(page=page)))       
    
        page.update()


    page.on_route_change = mudar_rota
    page.go('/')

    # Overlay
    # page.bottom_appbar = MenuBottom()
