# Project-6. New York City Taxi Trip Duration

## Оглавление / Table of Contents
1. [Постановка задачи / Statement of the Problem](#1-постановка-задачи--statement-of-the-problem)
2. [Знакомство с данными и базовый анализ / Getting to Know the Data](#2-знакомство-с-данными-и-базовый-анализ--getting-to-know-the-data)
3. [Разведывательный анализ данных (EDA) / Exploratory Data Analysis](#3-разведывательный-анализ-данных-eda--exploratory-data-analysis)
4. [Отбор и преобразование признаков / Feature Selection and Transformation](#4-отбор-и-преобразование-признаков--feature-selection-and-transformation)
5. [Регрессионные модели: линейные модели и деревья / Regression Models](#5-регрессионные-модели-линейные-модели-и-деревья--regression-models)
6. [Ансамблевые методы и прогнозирование / Ensemble Methods and Prediction](#6-ансамблевые-методы-и-прогнозирование--ensemble-methods-and-prediction)
7. [Bonus: XGBoost](#7-bonus-xgboost)

---

## 1. Постановка задачи / Statement of the Problem

**Бизнес-задача / Business problem**  
Необходимо предсказать длительность поездки на такси в Нью-Йорке на основе информации о маршруте, времени поездки и дополнительных внешних данных.
*The goal is to predict the duration of a taxi ride in New York City based on route information, travel time, and additional external data.*

**Техническая задача / Technical task**  
Построить модель машинного обучения для прогнозирования продолжительности поездки (в секундах) и оценить её качество с использованием метрики **RMSLE**.
*Build a machine learning model to predict trip duration (in seconds) and evaluate its quality using the **RMSLE** metric.*

**Цели проекта / Project objectives**
- Провести анализ и очистку данных 
  *Conduct data analysis and cleaning* 
- Выполнить генерацию и отбор признаков  
  *Perform feature generation and selection*
- Обучить и сравнить несколько моделей регрессии  
  *Train and compare multiple regression models*
- Выбрать лучшую модель по значению RMSLE  
  *Select the best model based on RMSLE value*

---

## 2. Знакомство с данными и базовый анализ / Getting to Know the Data

- Ознакомление с датасетом, анализ структуры и типов данных  
  *Exploring the dataset, reviewing its structure and data types*
- Приведение признаков к корректным форматам  
  *Converting features to appropriate data types*
- Подключение дополнительных источников данных и расширение исходного датасета  
  *Loading additional data sources and extending the original dataset*
- Генерация новых признаков  
  *Feature engineering*
- Поиск и удаление выбросов  
  *Detecting and removing outliers*

---

## 3. Разведывательный анализ данных (EDA) / Exploratory Data Analysis

- Исследование сформированного набора данных  
  *Exploring the prepared dataset*
- Выявление закономерностей и формирование гипотез о факторах, влияющих на длительность поездки  
  *Identifying patterns and forming hypotheses about factors affecting trip duration*
- Визуализация данных  
  *Data visualization*

---

## 4. Отбор и преобразование признаков / Feature Selection and Transformation

- Удаление неинформативных и избыточных признаков  
  *Removing uninformative and redundant features*
- Кодирование категориальных признаков  
  *Encoding categorical features*
- Разделение данных на обучающую и валидационную выборки  
  *Splitting the dataset into training and validation sets*
- Отбор **25 наиболее важных признаков** с использованием `SelectKBest`  
  *Selecting the **25 most important features** using SelectKBest*
- Масштабирование числовых признаков  
  *Scaling numerical features*

---


## 5. Регрессионные модели: линейные модели и деревья / Regression Models

- Линейная регрессия и расчёт метрики RMSLE  
  *Linear regression and RMSLE evaluation*
- Полиномиальная регрессия 2-й степени  
  *Second-degree polynomial regression*
- Полиномиальная регрессия с L2-регуляризацией  
  *Polynomial regression with L2 regularization*
- Дерево решений  
  *Decision tree regression*
- Подбор оптимальной глубины дерева  
  *Finding the optimal tree depth*

---

## 6. Ансамблевые методы и прогнозирование / Ensemble Methods and Prediction

- Случайный лес  
  *Random Forest regression*
- Градиентный бустинг над деревьями решений  
  *Gradient Boosting regression*
- Сравнение моделей и выбор лучшей  
  *Model comparison and selection*
- Анализ важности признаков  
  *Feature importance analysis*
- Построение прогноза для тестового набора данных  
  *Prediction on the test dataset*   

---

## 7. Bonus: XGBoost

- Построение модели экстремального градиентного бустинга  
  *Extreme Gradient Boosting (XGBoost) model*
- Оценка качества модели по метрике RMSLE  
  *Model evaluation using RMSLE*

---

## Notebook

Подробнее с ходом работы можно ознакомиться:
*You can find out more about the progress of the work:*

https://github.com/korolmaria1291/data_science_study/blob/main/project_6/Project-6.%20New%20York%20City%20Taxi%20Trip%20Duration.ipynb

---

## Данные / Data

Оригинальный датасет доступен на Kaggle:  
*The original dataset is available on Kaggle:*
**(https://www.kaggle.com/competitions/nyc-taxi-trip-duration/data)**


Дополнительные датасеты, использованные в проекте:  
*Additional datasets used in this project:*
 **(https://drive.google.com/file/d/1lAezKADk8n8LcxH_ESJrhjBcB5L_0dvp/view?usp=drive_link)**
 **(https://drive.google.com/file/d/1eFQsqzY75bZgpvd62zrEtC3Lo-Yk487K/view?usp=drive_link)**
 **(https://drive.google.com/file/d/1MgFjk24__r95aiPvOVy6Bdsl-fk8XvhR/view?usp=drive_link)**
 **(https://drive.google.com/file/d/1NOd3rBQ1PxwG8R1od3T7Bla7TcPqRj63/view?usp=drive_link)**

---

## Используемые инструменты / Tools used

- **Jupyter Notebook**  
- **Python**  
- **pandas, numpy, matplotlib, seaborn**  
- **scikit-learn, XGBoost**  