def clean_titanic(df):
    # The original data set won't get mutated
    df = df.copy()

    # Drop deck column
    df = df.drop(columns=["deck"])

    # Fill age column missing values with the age median
    df["age"] = df["age"].fillna(value=df["age"].median())

    # Fill embarked and embark_town missing values with each column first mode
    df["embarked"] = df["embarked"].fillna(value=df["embarked"].mode()[0])
    df["embark_town"] = df["embark_town"].fillna(value=df["embark_town"].mode()[0])

    # Returns the edited df
    return df