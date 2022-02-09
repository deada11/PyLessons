names = ["David", "John", "Annabelle", "Johnathan", "Veronica"]

print(
    list(
        filter(
            lambda x: len(x) > 5, names
        )
    )
)
