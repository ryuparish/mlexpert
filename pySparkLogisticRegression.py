from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler


def predict_cancellations(user_interaction_df):
    # Making a vector assembler which will put all of the values found in this list of columns
    # into a single column.
    assembler = VectorAssembler(
        inputCols=["month_interaction_count", "week_interaction_count", "day_interaction_count"], outputCol="features"
    )

    # Transforming the user_interaction_df into the dataframe with the transformed column
    features_df = assembler.transform(user_interaction_df)
    # The features_df also contains the other columns in the user_interaction_df that 
    # are untouched. We then change the name of the "cancelled_within_week" to "label"
    # because the LogisticRegression model expects a label column along with a features column.
    features_df = features_df.withColumn("label", features_df["cancelled_within_week"])

    # Creating and training the model
    lr_model = LogisticRegression(maxIter=10, threshold=0.6, elasticNetParam=1, regParam=0.1)
    trained_lr_model = lr_model.fit(features_df)

    # Making the predictions and then selecting our desired values fron the prediction matrix
    predictions_df = trained_lr_model.transform(features_df)
    predictions_df = predictions_df.select(["user_id", "rawPrediction", "probability", "prediction"])

    return predictions_df

