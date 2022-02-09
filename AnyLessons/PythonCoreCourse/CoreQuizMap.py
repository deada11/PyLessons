birth_years = [1995, 2004, 2019, 1988, 1977, 1902]

print(
    list(
        map(
            lambda x: (2050 - x), birth_years)
    )
)
