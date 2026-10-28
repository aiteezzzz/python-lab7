import csv
import numpy as np
import matplotlib.pyplot as plt

try:

    ukraine_years = []
    ukraine_values = []

    poland_years = []
    poland_values = []

    with open(
            "inflation.csv",
            "r",
            encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            country = row["Country"]
            year = int(row["Year"])
            value = float(row["Inflation"])

            if country == "Ukraine":
                ukraine_years.append(year)
                ukraine_values.append(value)

            elif country == "Poland":
                poland_years.append(year)
                poland_values.append(value)

    # --------------------
    # ГРАФІК
    # --------------------

    plt.figure(figsize=(10, 6))

    plt.plot(
        ukraine_years,
        ukraine_values,
        marker="o",
        label="Ukraine"
    )

    plt.plot(
        poland_years,
        poland_values,
        marker="s",
        label="Poland"
    )

    plt.title(
        "Inflation Dynamics"
    )

    plt.xlabel("Year")
    plt.ylabel("Inflation (%)")

    plt.legend()

    plt.grid(True)

    plt.show()

    # --------------------
    # СТОВПЧАСТА ДІАГРАМА
    # --------------------

    country_input = input(
        "Enter country (Ukraine/Poland): "
    )

    if country_input == "Ukraine":

        years = ukraine_years
        values = ukraine_values

    elif country_input == "Poland":

        years = poland_years
        values = poland_values

    else:

        print("Country not found!")
        exit()

    plt.figure(figsize=(10, 6))

    plt.bar(
        years,
        values
    )

    plt.title(
        f"Inflation in {country_input}"
    )

    plt.xlabel("Year")
    plt.ylabel("Inflation (%)")

    plt.show()

    # --------------------
    # КРУГОВА ДІАГРАМА
    # --------------------

    year_input = int(
        input(
            "Enter year (2015-2023): "
        )
    )

    if year_input not in ukraine_years:

        print("Year not found!")
        exit()

    index = ukraine_years.index(year_input)

    data = [
        ukraine_values[index],
        poland_values[index]
    ]

    labels = [
        "Ukraine",
        "Poland"
    ]

    plt.figure(figsize=(7, 7))

    plt.pie(
        data,
        labels=labels,
        autopct="%1.1f%%"
    )

    plt.title(
        f"Inflation Comparison {year_input}"
    )

    plt.show()

except FileNotFoundError:

    print("File inflation.csv not found!")

except Exception as e:

    print("Error:", e)