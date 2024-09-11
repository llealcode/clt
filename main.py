from assets.codespack import settings

import flet as ft

def main(page: ft.Page):

    settings.layout_page(page=page)

    page.update()

    
    

ft.app(target=main)
