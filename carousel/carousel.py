import flet as ft


def main(page: ft.Page):
    page.title = 'Carousel'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horiz_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE

    def key_left(e):
        carousel.scroll_to(delta=-300, duration=300, curve=ft.AnimationCurve.LINEAR)
        carousel.update()

    def key_right(e):
        carousel.scroll_to(delta=300, duration=300, curve=ft.AnimationCurve.DECELERATE)
        carousel.update()

    layout = ft.Container(
        shadow=ft.BoxShadow(blur_radius=100),
        content=ft.Column(
            controls=[
                carousel := ft.Row(
                    scroll=ft.ScrollMode.HIDDEN,
                    controls=[
                        ft.Image(
                            src=f'https://picsum.photos/250/300?{num}',
                        )for num in range(10)
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                   controls=[
                       ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_LEFT, on_click=key_left),
                       ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_RIGHT, on_click=key_right),
                   ]
                )
            ]
        )
    )

    page.add(layout)


ft.app(target=main)