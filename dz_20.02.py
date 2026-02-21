import flet as ft
from flet import AppView

def main(page: ft.Page):
    page.window.width = 300
    page.window.height = 300

    page.window.min_width = 300
    page.window.min_height = 300

    page.window.max_width = 300
    page.window.max_height = 300

    page.spacing = 20

    page.title = "Вибір шляху"

    t1 = ft.Text(
        "Направо підеш – коня втратиш\n"
        "Наліво підеш – голову втратиш\n"
        "Прямо підеш – життя втратиш\n"
        "Зроби свій вибір.",
        color=ft.Colors.WHITE,
        text_align=ft.TextAlign.CENTER,
        size=17
    )

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    com_text = ft.Text("")

    def left_click(e):
        com_text.value = "Голову втратив? Шкода..."
        com_text.bgcolor = ft.Colors.DEEP_ORANGE_400

    def straight_click(e):
        com_text.value = "Життя втратив? Невесело..."
        com_text.bgcolor = ft.Colors.LIGHT_BLUE

    def right_click(e):
        com_text.value = "Коня втратив? Буває..."
        com_text.bgcolor = ft.Colors.LIGHT_GREEN

    left_button = ft.ElevatedButton(
        "Ліво",
        on_click=left_click,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.RED_700,
    )

    straight_button = ft.ElevatedButton(
        "Прямо",
        on_click=straight_click,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.BLUE_700,
    )

    right_button = ft.ElevatedButton(
        "Право",
        on_click=right_click,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.GREEN_700,
    )

    t_button = ft.Row(
        [left_button, straight_button, right_button],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(
        t1,com_text,t_button)

if __name__ == "__main__":
    ft.run(main, view=AppView.WEB_BROWSER)