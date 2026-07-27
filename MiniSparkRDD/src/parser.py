# src/parser.py


def clean_price(value):

    if value is None:
        return 0


    value = value.replace(
        "₹",
        ""
    )


    value = value.replace(
        ",",
        ""
    )


    return float(value)



def clean_percentage(value):

    if value is None:
        return 0


    value = value.replace(
        "%",
        ""
    )


    return float(value)



def clean_rating(value):

    try:

        return float(value)

    except:

        return 0