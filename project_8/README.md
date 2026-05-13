# Real estate project. Housing price forecasting model for a real estate agency

## Оглавление / Table of Contents
1. [Постановка задачи / Statement of the Problem](#1-постановка-задачи--statement-of-the-problem)
2. [Знакомство с данными, очистка и предобработка данных/ Getting to Know the Data, Data cleaning and preprocessing](#2-знакомство-с-данными-очистка-и-предобработка-данных--getting-to-know-the-data-data-cleaning-and-preprocessing)
3. [Разведывательный анализ данных (EDA) / Exploratory Data Analysis](#3-разведывательный-анализ-данных-eda--exploratory-data-analysis)
4. [Feature Engineering](#4-feature-engineering)
5. [Анализ факторов, влияющих на стоимость недвижимости / Analyzing factors affecting real estate value](#5-анализ-факторов-влияющих-на-стоимость-недвижимости--analyzing-factors-affecting-real-estate-value)
6. [Построение и обучение моделей / Building and training models](#6-построение-и-обучение-моделей--building-and-training-models)
7. [Оценка качества моделей и выбор финальной / Assessing model quality and selecting the final model](#7-оценка-качества-моделей-и-выбор-финальной--assessing-model-quality-and-selecting-the-final-model)
8. [Производительность моделей / Model Performance](#8-производительность-моделей--model-performance)
9. [Разработка прототипа веб-сервиса / Developing a web service prototype](#9-разработка-прототипа-веб-сервиса--developing-a-web-service-prototype)
10. [Структура проекта / Project structure](#10-структура-проекта--project-structure)

---

## 1. Постановка задачи / Statement of the Problem

**Бизнес-задача / Business problem**  
 Разработать инструмент, позволяющий агентству недвижимости более точно и быстро оценивать рыночную стоимость объектов, что способствует: сокращению времени сделки, снижению риска недооценки или переоценки недвижимости,повышению конкурентоспособности агентства.
*Develop a tool that allows real estate agencies to more accurately and quickly assess the market value of properties, thereby reducing transaction times, reducing the risk of undervaluation or overvaluation of real estate, and increasing the agency's competitiveness.*

**Техническая задача / Technical task**  
Разработать и внедрить модель машинного обучения для прогнозирования стоимости недвижимости на основе доступных характеристик объекта.
*Develop and implement a machine learning model to predict real estate prices based on available property characteristics.*

---

## 2. Знакомство с данными, очистка и предобработка данных/ Getting to Know the Data, Data cleaning and preprocessing

- Ознакомление с датасетом, анализ структуры и типов данных  
  *Exploring the dataset, reviewing its structure and data types*
- Преобразование, очистка и анализ данных
  *Data transformation, cleaning and analysis*
- Датасет содержит большое количество шумных и неоднородных данных, поэтому потребовалась масштабная предобработка и трансформация признаков.
  *The dataset contains a large amount of noisy and heterogeneous data, so extensive preprocessing and feature transformation were required.*  

---

## 3. Разведывательный анализ данных (EDA) / Exploratory Data Analysis

- Исследование сформированного набора данных, нахождение выбросов, избавление от них и логарифмирование целевой переменной  
  *Examination of the generated data set, finding outliers, getting rid of them and taking the logarithm of the target variable*
- Анализ зависимости признаков от целевой переменной. Путем формулирования и проверки гипотез, анализ важности признаков.
  *Analysis of the dependence of features on the target variable. By formulating and testing hypotheses, analyzing the importance of features.*
- Визуализация данных  
  *Data visualization*

---

## 4. Feature Engineering

- Признаки 'homeFacts' и 'schools' представляют собой сложную встроенную структуру. Путем парсинга достаем из них всю важную информацию. Создаем новые признаки и удаляем ненужные.
  *The 'homeFacts' and 'schools' features represent a complex built-in structure. We parse them to extract all the important information. We create new features and remove unnecessary ones.*
- Кодирование категориальных признаков 
  *Encoding categorical features*

--- 

## 5. Анализ факторов, влияющих на стоимость недвижимости / Analyzing factors affecting real estate value

- Корреляционный анализ числовых признаков с целевой переменной 
  *Correlation analysis of numerical features with the target variable*
- Анализ бинарных признаков с целевой переменной  
  *Binary feature analysis with a target variable*
- Анализ булевых признаков с целевой переменной 
  *Boolean feature analysis with target variable*
- Визуализация данных  
  *Data visualization*

---

## 6. Построение и обучение моделей / Building and training models

- Построение базовой модели линейной регрессии и оценка качества модели с использованием метрик MAE, RMSE и коэффициента детерминации R2.
  *Construction of a basic linear regression model and evaluation of the model quality using the MAE, RMSE and R2 metrics.*
- Построение моделей **Random Forest**, **Gradient Boosting**, **XGBoost Regression**, **CatBoost Regression** и оценка качества моделей с использованием метрик MAE, RMSE и коэффициента детерминации R2.
  *Construction of **Random Forest**, **Gradient Boosting**, **XGBoost Regression**, **CatBoost Regression** models and evaluation of the quality of the models using the MAE, RMSE and R2 metrics.*
- Подбор гиперпараметров для **Gradient Boosting**, используя **RandomizedSearchCV**. Подбор гиперпараметров для **CatBoost Regression**, используя **Optuna**.
  *Hyperparameter selection for **Gradient Boosting** using **RandomizedSearchCV**. Hyperparameter selection for **CatBoost Regression** using **Optuna**.*

---

## 7. Оценка качества моделей и выбор финальной / Assessing model quality and selecting the final model

- Сравнение метрик всех моделей для определения финальной модели
  *Comparison of metrics of all models to determine the final model*
- Анализ важности признаков финальной модели и визуализация
  *Feature importance analysis of the final model and visualization*
- Вывод о качестве модели
  *Conclusion on the quality of the model*

---

## 8. Производительность моделей / Model Performance

| Model | MAE Train | MAE Test | RMSE Train | RMSE Test | R² Train | R² Test |
|---|---|---|---|---|---|---|
| **CatBoost Regression** | 0.104 | 0.201 | 0.173 | 0.308 | 0.843 | **0.850** |
| Gradient Boosting | 0.176 | 0.218 | 0.257 | 0.322 | 0.896 | 0.837 |
| XGB Regression | 0.217 | 0.240 | 0.315 | 0.348 | 0.953 | 0.809 |
| Random Forest | 0.171 | 0.239 | 0.259 | 0.356 | 0.895 | 0.801 |
| Polynomial + Lasso | 0.320 | 0.320 | 0.443 | 0.443 | 0.692 | 0.691 |
| Linear Regression | 0.407 | 0.407 | 0.542 | 0.540 | 0.540 | 0.542 |
| Lasso | 0.413 | 0.412 | 0.551 | 0.549 | 0.525 | 0.526 |

- В качестве окончательной модели для развертывания была выбрана **CatBoost Regression**, поскольку она продемонстрировала наилучший баланс между точностью прогнозирования и способностью к обобщению на тестовом наборе данных.
  *The final model selected for deployment was **CatBoost Regression**, as it demonstrated the best balance between prediction accuracy and generalization ability on the test dataset.*

---

## 9. Разработка прототипа веб-сервиса / Developing a web service prototype

- Подготовка артефактов, создание функции для обработки "сырых" данных, сериализация обученной финальной модели, сохранение признаков модели.
  *Preparing artifacts, creating a function for processing raw data, serializing the trained final model, saving model features.*
- Создание REST API с использованием FastAPI
  *Creating a REST API using FastAPI*
- Тестирование эндпоинта `/predict` через Swagger UI
  *Testing the `/predict` endpoint via Swagger UI*
- Получение предсказаний стоимости недвижимости на новых данных
  *Generating real estate price predictions for new data*
- Реализация API и демонстрация работы веб-сервиса
  *Implementing the API and demonstrating how the web service works*

---

## 10. Структура проекта / Project structure

```text
project_8/
│
├── real_estate_project.ipynb
├── demonstration_of_fastapi_1.jpeg
├── demonstration_of_fastapi_2.jpeg
├── README.md
│
├── real_estate_api/
│   ├── main.py
│   ├── requirements.txt
│   ├── catboost_real_estate.pkl
│   ├── feature_names.pkl
│   ├── bin_encoder.pkl
│   ├── top_cities.pkl
│   ├── city_freq.pkl
│   ├── baths_median.pkl
│   ├── beds_median.pkl
│   ├── lotsize_median.pkl
│   ├── parking_median.pkl
│   ├── school_rating_median.pkl
│   ├── sqft_median.pkl
│   ├── stories_median.pkl
│   ├── year_built_median.pkl
│   └── zipcode_freq.pkl
```

---

## Notebook

Файл обученной модели 'catboost_real_estate.pkl' не включен в репозиторий из-за ограничений GitHub по размеру файлов.
*The trained model file 'catboost_real_estate.pkl' is not included in the repository due to GitHub file size limitations.*

Подробнее с ходом работы можно ознакомиться:
*You can find out more about the progress of the work:*

https://github.com/korolmaria1291/data_science_study/blob/main/project_8/real_estate_project.ipynb

---

## Данные / Data

Оригинальный датасет:  
*The original dataset:*
**(https://drive.google.com/file/d/11-ZNNIdcQ7TbT8Y0nsQ3Q0eiYQP__NIW/view?usp=share_link?)**

---

## Используемые инструменты / Tools used

- **Jupyter Notebook**  
- **Python**  
- **pandas, numpy, matplotlib, seaborn, plotly, scipy, joblib**  
- **scikit-learn, xgboost, catboost, optuna**  
- **fastapi, uvicorn, category_encoders**