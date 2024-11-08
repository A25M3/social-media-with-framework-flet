from flet import *
from dummyData import Users

def post(post):
    user = next((u for u in Users if u["id"] == post["userId"]), {})

    post_top = Row(
        controls=[
            Row(
                controls=[
                    Image(
                        src=user["profilePicture"],
                        width=40,
                        height=40,
                        fit=ImageFit.COVER,
                        border_radius=20,
                    ),

                    Column(
                        controls=[
                            Text(user["username"]),
                            Text(post["date"], size=12, color="grey")
                        ],
                        spacing=2
                    )
                ], alignment=MainAxisAlignment.CENTER
            ),

            IconButton(icon=icons.MORE_VERT)
        ], alignment=MainAxisAlignment.SPACE_BETWEEN
    )

    post_text = Container() if post.get("desc") is None else Text(post["desc"])
    post_center = Column(
                    controls=[
                        post_text,
                        Image(
                            src=post["photo"],
                            width=460,
                            height=330,
                            fit=ImageFit.COVER,
                        ),
                    ]
                )

    post_bottom = Row(
        controls=[
            Row(
                controls=[
                   IconButton(icon=icons.FAVORITE, icon_color="pink"),
                   IconButton(icon=icons.THUMB_UP, icon_color="blue"),
                   Text(str(post["like"]) + " people like this")
                ], alignment=MainAxisAlignment.CENTER
            ),

            Text(str(post["comment"]) + " comments")
        ], alignment=MainAxisAlignment.SPACE_BETWEEN
    )
    post_container = Container(
        content=Column(controls=[
            post_top,
            post_center,
            post_bottom
            ]),
        height=475,
        bgcolor="#3AC0C0C0",
        border_radius=10,
        padding=padding.only(left=20, top=10, right=20, bottom=10),
        margin=margin.only(bottom=10),
    )

    return post_container