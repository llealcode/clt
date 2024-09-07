import flet as ft


def layout_page(page):

    # Localidade e idioma da página
    page.locale_configuration = ft.LocaleConfiguration(supported_locales=[ft.Locale('pt', 'BR')], current_locale=ft.Locale('pt', 'BR'))

    # Posicionamento    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.maximizable = False
    page.window.resizable = False
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
    