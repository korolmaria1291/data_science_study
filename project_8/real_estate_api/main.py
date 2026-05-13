import pandas as pd
import numpy as np
import joblib
import ast
import re

from fastapi import FastAPI
from catboost import CatBoostRegressor

app = FastAPI()

# Загружаем модель и артефакты
# Loading the model and artifacts
model = joblib.load("catboost_real_estate.pkl")
model_columns = joblib.load("feature_names.pkl")
bin_encoder = joblib.load("bin_encoder.pkl")
top_cities = joblib.load("top_cities.pkl")
city_freq = joblib.load("city_freq.pkl")
zipcode_freq = joblib.load("zipcode_freq.pkl")

# Загружаем медианы
# Loading medians
sqft_median = joblib.load("sqft_median.pkl")
baths_median = joblib.load("baths_median.pkl")
beds_median = joblib.load("beds_median.pkl")
stories_median = joblib.load("stories_median.pkl")
school_rating_median = joblib.load("school_rating_median.pkl")
year_built_median = joblib.load("year_built_median.pkl")
lotsize_median = joblib.load("lotsize_median.pkl")
parking_median = joblib.load("parking_median.pkl")


# Преобразуем данные
# Transform the data
def preprocess_data(df):
    df = df.copy()
    df = df.drop_duplicates()
    df = df.drop(['mls-id', 'MlsId'], axis=1, errors='ignore')
    df['pool'] = ((df['private pool'].notna()) | (df['PrivatePool'].notna())).astype(int)
    df = df.drop(columns=['private pool', 'PrivatePool'], errors='ignore')
    df['propertyType'] = df['propertyType'].str.lower()
    df['propertyType'] = df['propertyType'].fillna('unknown')
    category_property = {'single_family': 'single|detached',
                         'condo': 'condo',
                         'cooperative': 'coop|cooperative',
                         'townhouse': 'townhome|townhouse',
                         'multi_family': 'multi',
                         'mobile': 'mobile|manufactured|modular',
                         'land': 'land|lot|farm'
                         }
    df['property_type_clean'] = 'other'
    for category, pattern in category_property.items():
        df.loc[df['propertyType'].str.contains(pattern, na=False), 'property_type_clean'] = category
    df.loc[df['propertyType'].isna() | (df['propertyType'] == 'unknown'), 'property_type_clean'] = 'unknown'
    df = df.drop(['propertyType'], axis=1, errors='ignore')
    df['sqft'] = df['sqft'].str.replace(',', '', regex=False).str.extract(r'(\d+)', expand=False).astype(float)
    df['sqft'] = df['sqft'].replace(0, np.nan)
    df['sqft'] = df['sqft'].fillna(sqft_median)

    df = df.drop(['street'], axis=1, errors='ignore')
    df['baths'] = df['baths'].str.replace(',', '', regex=False).str.extract(r'(\d+\.?\d*)', expand=False).astype(float)
    df.loc[df['baths'] > 15, 'baths'] = np.nan
    df['baths_missing'] = df['baths'].isna().astype(int)
    df['baths'] = df['baths'].fillna(baths_median)

    df = df[df['baths'] > 0].reset_index(drop=True)
    mask = df['beds'].str.contains('sqft|acre', case=False, na=False)
    df.loc[mask, 'beds'] = np.nan
    df['beds'] = df['beds'].str.replace(',', '', regex=False).str.extract(r'(\d+\.?\d*)', expand=False).astype(float)
    df.loc[df['beds'] > 20, 'beds'] = np.nan
    df.loc[df['beds'] == 0, 'beds'] = np.nan
    df['beds_missing'] = df['beds'].isna().astype(int)
    df['beds'] = df['beds'].fillna(beds_median)

    df = df[~df['status'].str.contains('rent', case=False, na=False)].reset_index(drop=True)
    category_status = {'pending': 'pending|contract|contingent|option',
                       'sold': 'sold|closed',
                       'distressed': 'foreclosure|auction',
                       'sale': 'sale|active|new|price change|back on market|show|listing extended'
                       }
    df['status'] = df['status'].str.lower()
    df['status_clean'] = 'other'
    for category, pattern in category_status.items():
        df.loc[df['status'].str.contains(pattern, na=False), 'status_clean'] = category
    df.loc[df['status'].isna(), 'status_clean'] = 'unknown'
    df = df.drop(['status'], axis=1, errors='ignore')
    df['fireplace'] = df['fireplace'].str.lower()
    df['has_fireplace'] = 0
    df.loc[df['fireplace'].str.contains('yes|[1-9]|fireplace|gas|wood|room|familyrm|rm', na=False), 'has_fireplace'] = 1
    df = df.drop(['fireplace'], axis=1, errors='ignore')
    df['stories'] = df['stories'].str.lower()
    df['stories'] = df['stories'].str.replace('one', '1', regex=False)
    df['stories'] = df['stories'].str.replace('two', '2', regex=False)
    df['stories'] = df['stories'].str.replace('three', '3', regex=False)
    df['stories'] = df['stories'].str.extract(r'(\d+\.?\d*)', expand=False).astype(float)
    df.loc[df['stories'] == 0, 'stories'] = np.nan
    df.loc[df['stories'] > 10, 'stories'] = np.nan
    df['stories_missing'] = df['stories'].isna().astype(int)
    df['stories'] = df['stories'].fillna(stories_median)

    df = df[df['sqft'] >= 100]

    def process_schools(schools):
        try:
            tree = ast.literal_eval(schools)
        except:
            return np.nan, np.nan, np.nan
        try:
            school_count = len(tree[0]['name'])
        except:
            return np.nan, np.nan, np.nan
        try:
            rating = tree[0]['rating']
        except:
            return np.nan, np.nan, np.nan
        clean_rating = []
        for x in rating:
            try:
                clean_rating.append(float(x.split('/')[0]))
            except:
                continue
        valid_school_count = len(clean_rating)
        if len(clean_rating) == 0:
            average_rating = np.nan
        else:
            average_rating = sum(clean_rating) / len(clean_rating)
        return average_rating, school_count, valid_school_count

    df[['school_rating', 'school_count', 'valid_school_count']] = (
        df['schools'].apply(process_schools).apply(pd.Series))
    df['school_rating_missing'] = df['school_rating'].isna().astype(int)
    df['school_rating'] = (df['school_rating'].fillna(school_rating_median))

    df = df.drop(['schools'], axis=1, errors='ignore')

    def process_home_facts(home_facts):
        try:
            tree = ast.literal_eval(home_facts)
        except:
            return np.nan, np.nan
        facts_dict = {item['factLabel']: item['factValue'] for item in tree['atAGlanceFacts']}
        value = facts_dict.get('Year built')
        if value is None or value == '' or value == '—':
            year_built = np.nan
        else:
            value = str(value).strip()
            match = re.search(r'\d{4}', value)
        if match:
            year_built = int(match.group())
        else:
            year_built = np.nan
        if year_built < 1600 or year_built > 2025:
            year_built = np.nan
        value_2 = facts_dict.get('Remodeled year')
        if value_2 is None or value_2 == '' or value_2 == '—':
            remodeled_year = np.nan
        else:
            value_2 = str(value_2).strip()
            match_2 = re.search(r'\d{4}', value_2)
            if match_2:
                remodeled_year = int(match_2.group())
            else:
                remodeled_year = np.nan
        if remodeled_year < 1600 or remodeled_year > 2026:
            remodeled_year = np.nan
        if not np.isnan(year_built) and not np.isnan(remodeled_year):
            if remodeled_year < year_built or remodeled_year > 2026:
                remodeled_year = np.nan
        return year_built, remodeled_year

    df[['year_built', 'remodeled_year']] = df['homeFacts'].apply(process_home_facts).apply(pd.Series)
    df['year_built_missing'] = df['year_built'].isna().astype(int)
    df['year_built'] = (df['year_built'].fillna(year_built_median))

    df['is_remodeled'] = df['remodeled_year'].notna().astype(int)
    df = df.drop(['remodeled_year'], axis=1, errors='ignore')

    def process_home_facts_2(home_facts):
        try:
            tree = ast.literal_eval(home_facts)
        except:
            return np.nan
        facts_dict = {item['factLabel']: item['factValue'] for item in tree['atAGlanceFacts']}
        value = facts_dict.get('lotsize')
        if value is None or value == '' or value == '—':
            lotsize = np.nan
        else:
            value = str(value).lower().replace(',', '').strip()
            if 'acre' in value:
                match = re.search(r'\d+\.?\d*', value)
                lotsize = float(match.group()) * 43560 if match else np.nan
            else:
                match = re.search(r'\d+', value)
                lotsize = float(match.group()) if match else np.nan
        return lotsize

    df['lotsize'] = df['homeFacts'].apply(process_home_facts_2)
    df.loc[df['lotsize'] > 1e6, 'lotsize'] = np.nan
    df.loc[df['lotsize'] == 0, 'lotsize'] = np.nan
    df['lotsize_missing'] = df['lotsize'].isna().astype(int)
    df['lotsize'] = df['lotsize'].fillna(lotsize_median)

    def process_home_facts_3(home_facts):
        try:
            tree = ast.literal_eval(home_facts)
        except:
            return np.nan
        facts_dict = {item['factLabel']: item['factValue'] for item in tree['atAGlanceFacts']}
        value = facts_dict.get('Heating')
        if value is None or value == '' or value == '—':
            heating = np.nan
        else:
            value = str(value).lower().strip()
            if 'electric' in value:
                heating = 'electric'
            elif 'gas' in value:
                heating = 'gas'
            else:
                heating = 'other'
        value_2 = facts_dict.get('Cooling')
        if value_2 is None or value_2 == '' or value_2 == '—':
            has_cooling = np.nan
        else:
            value_2 = str(value_2).lower()
            if 'no' in value_2:
                has_cooling = 0
            elif 'cool' in value_2 or 'air' in value_2:
                has_cooling = 1
            else:
                has_cooling = np.nan
        value_3 = facts_dict.get('Parking')
        if value_3 is None or value_3 == '' or value_3 == '—':
            parking = np.nan
        else:
            value_3 = str(value_3).lower()
            match = re.search(r'\d+', value_3)
            if match:
                val = float(match.group())
                if val > 20:
                    parking = np.nan
                else:
                    parking = val
            else:
                parking = np.nan
        return heating, has_cooling, parking

    df[['heating', 'has_cooling', 'parking']] = df['homeFacts'].apply(process_home_facts_3).apply(pd.Series)
    df['parking_missing'] = df['parking'].isna().astype(int)
    df['parking'] = df['parking'].fillna(parking_median)

    df['has_cooling_missing'] = df['has_cooling'].isna().astype(int)
    df['has_cooling'] = df['has_cooling'].fillna(0)
    df['heating'] = df['heating'].fillna('unknown')
    df = df.drop(['homeFacts'], axis=1, errors='ignore')
    df['sqft_per_bed'] = df['sqft'] / df['beds']
    df['sqft_per_bath'] = df['sqft'] / df['baths']
    df['sqft_log'] = np.log1p(df['sqft'])
    df['lotsize_log'] = np.log1p(df['lotsize'])
    df = df.drop(['sqft', 'lotsize'], axis=1, errors='ignore')
    type_bin = bin_encoder.transform(df[['state']])
    df = pd.concat([df, type_bin], axis=1)
    df = df.drop(['state'], axis=1, errors='ignore')
    df = pd.get_dummies(df, columns=['property_type_clean', 'status_clean', 'heating'])
    df['city_freq'] = df['city'].map(city_freq)
    df['city'] = df['city'].str.strip()
    df.loc[df['city'].isin(['New York', 'Brooklyn']), 'city'] = 'New York'
    df['city'] = df['city'].where(df['city'].isin(top_cities), 'other')
    df = pd.get_dummies(df, columns=['city'], drop_first=True)
    df['zipcode_freq'] = df['zipcode'].map(zipcode_freq)
    df = df.drop(['zipcode'], axis=1, errors='ignore')
    df = df.reset_index(drop=True)
    bool_cols = df.select_dtypes(include='bool').columns
    df[bool_cols] = df[bool_cols].astype(int)

    return df


# Главная страница
# Home page
@app.get("/")
def home():
    return {"message": "Real Estate Price Prediction API"}


# Predict endpoint
@app.post("/predict")
def predict(data: dict):
    # Превращаем input в dataframe
    # Convert the input to a dataframe
    input_df = pd.DataFrame([data])
    processed_df = preprocess_data(input_df)

    processed_df = processed_df.reindex(columns=model_columns, fill_value=0)

    prediction_log = model.predict(processed_df)[0]
    prediction = np.expm1(prediction_log)

    return {"prediction": float(prediction)}