from src.loader import load_csv
from src.rdd import RDD
from src.utils import show_results



# Load Amazon Dataset

data = load_csv(
    "D:\\MiniSparkRDD\\Data\\amazon.csv"
)


# Create RDD

amazon_rdd = RDD(data)



# Build Pipeline

result = (

    amazon_rdd


    .filter(

        lambda x:

        "Electronics"
        in
        x["category"]

    )


    .filter(

        lambda x:

        float(x["rating"])
        > 4

    )


    .map(

        lambda x:

        x["product_name"]

    )


    .collect()

)



show_results(result)