import pandas as pd
import inflection
import streamlit as st

COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
}


COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
}


def rename_columns(dataframe):
    df1 = dataframe.copy()

    cols_old = list(df1.columns)
    cols_old = list(map(inflection.titleize, cols_old))
    cols_old = [col.replace(" ", "") for col in cols_old]
    cols_new = list(map(inflection.underscore, cols_old))

    df1.columns = cols_new

    return df1


def country_name(country_id):
    return COUNTRIES[country_id]


def color_name(color_code):
    return COLORS[color_code]


def create_price_type(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"


def adjust_columns_order(dataframe):
    df1 = dataframe.copy()

    new_cols_order = [
        "restaurant_id",
        "restaurant_name",
        "country",
        "city",
        "address",
        "locality",
        "locality_verbose",
        "longitude",
        "latitude",
        "cuisines",
        "price_type",
        "average_cost_for_two",
        "currency",
        "has_table_booking",
        "has_online_delivery",
        "is_delivering_now",
        "aggregate_rating",
        "rating_color",
        "color_name",
        "rating_text",
        "votes",
    ]

    return df1.loc[:, new_cols_order]


@st.cache_data
def process_data(file_path):
    df1 = pd.read_csv(file_path)

    df1 = rename_columns(df1)
    df1 = df1.dropna()

    df1["price_type"] = df1["price_range"].apply(create_price_type)
    df1["country"] = df1["country_code"].apply(country_name)
    df1["color_name"] = df1["rating_color"].apply(color_name)

    df1["cuisines"] = df1["cuisines"].apply(
        lambda x: x.split(",")[0]
    )

    df1 = df1.drop(
        df1[df1["cuisines"] == "Drinks Only"].index
    )

    df1 = df1.drop(
        df1[df1["cuisines"] == "Mineira"].index
    )

    df1 = df1.drop_duplicates()
    df1 = adjust_columns_order(df1)

    return df1
