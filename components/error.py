from flet import *
from components.costumButton import *
def error(page, message, btnLabel,route,btnIcon,iconColor):
    error_container = Column(
        controls=[
            Row(
                controls=[
                    Image(
                        src="../assets/error.png",
                        width=300,
                        height=400
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
            ),
            Row(
                controls=[
                    Text(message),
                    costumButton(btnLabel,page,route,btnIcon,iconColor),
                ],
                alignment=MainAxisAlignment.SPACE_AROUND
            )
        ]
    )

    return error_container