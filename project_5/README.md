# Проект 5. Прогнозирование оценки отеля / Project 5. Hotel Rating Prediction (Kaggle: Booking Reviews)

## Оглавление / Table of Contents
- [Исследование данных / Data Exploration](#исследование-данных--data-exploration)
- [Подготовка данных / Data Preparation](#подготовка-данных--data-preparation)
- [Исследовательский анализ данных / Exploratory Data Analysis](#исследовательский-анализ-данных--exploratory-data-analysis)
- [Создание модели предсказания / Creating a Prediction Model](#создание-модели-предсказания--creating-a-prediction-model)
- [Итоговый вывод / Final Project Summary](#итоговый-вывод--final-project-summary)
- [Улучшение качества предсказания с помощью более сильного алгоритма / Improving Prediction Quality with a Stronger Algorithm](#улучшение-качества-предсказания-с-помощью-более-сильного-алгоритма--improving-prediction-quality-with-a-stronger-algorithm)

---

## Исследование данных / Data Exploration
- Ознакомление с датасетом, просмотр структуры и типов данных.  
  *Exploration of the dataset, reviewing structure and data types.*
- Анализ распределений признаков и целевой переменной `average_score`.  
  *Analysis of feature distributions and the target variable `average_score`.*
- Выявление пропусков и потенциальных аномалий.  
  *Identification of missing values and potential anomalies.*

---

## Подготовка данных / Data Preparation
- Очистка данных и работа с пропусками.  
  *Data cleaning and handling missing values.*
- Приведение типов признаков к корректным форматам.  
  *Converting feature types to correct formats.*
- Удаление дубликатов и ненужных колонок.  
  *Removing duplicates and unnecessary columns.*

---

## Исследовательский анализ данных / Exploratory Data Analysis
- Обработка признаков и создание новых признаков.  
  *Feature engineering and creation of new features.*
- Кодирование категориальных признаков (Label / One-Hot Encoding).  
  *Encoding categorical features (Label / One-Hot Encoding).*
- Масштабирование числовых признаков.  
  *Scaling numerical features.*
- Работа с текстовыми признаками (TF-IDF / CountVectorizer).  
  *Processing text features (TF-IDF / CountVectorizer).*
- Анализ корреляционной матрицы и удаление ненужных признаков.  
  *Correlation matrix analysis and removal of low-informative features.*

---

## Создание модели предсказания / Creating a Prediction Model
- Разделение выборки на обучающую и тестовую.  
  *Splitting dataset into training and test sets.*
- Выбор **20 наиболее важных признаков** с помощью SelectKBest.  
  *Selection of the **20 most important features** using SelectKBest.*
- Обучение модели **RandomForestRegressor** на выбранных признаках.  
  *Training a **RandomForestRegressor** on selected features.*
- Оценка модели с помощью метрики: MAPE.  
  *Evaluation using metric: MAPE.*

---

## Итоговый вывод / Final Project Summary
- Проведен полный анализ данных и их подготовка для модели.  
  *Complete data analysis and preparation for modeling were performed.*
- Выявлены и закодированы значимые признаки, проведена работа с текстом.  
  *Significant features were identified and encoded; text features were processed.*
- Построена базовая модель RandomForestRegressor с улучшенной метрикой за счёт EDA и отбора признаков.  
  *A baseline RandomForestRegressor model was trained with improved metrics through EDA and feature selection.*
- Получены результаты, соответствующие заданию Kaggle.  
  *Results meet the requirements of the Kaggle competition.*

---

## Улучшение качества предсказания с помощью более сильного алгоритма / Improving Prediction Quality with a Stronger Algorithm
- Проведен эксперимент с **CatBoost**, который может напрямую работать с категориальными и текстовыми признаками.  
  *An experiment with **CatBoost** was conducted, which can directly handle categorical and text features.*
- Эксперимент показал возможность дальнейшего улучшения метрики.  
  *The experiment demonstrated the possibility of further improving metrics.*
- Этот шаг **не является обязательной частью задания**, а демонстрирует навыки работы с более сложными алгоритмами.  
  *This step is **not part of the mandatory assignment** but demonstrates skills in using more advanced algorithms.* 

Подробнее с ходом работы можно ознакомиться в [PROJECT-5. EDA + Feature Engineering. Kaggle competition](https://github.com/korolmaria1291/data_science_study/blob/main/project_4/Project_4_ML.ipynb)

## Используемые инструменты

- **Jupyter Notebook**  
- **Python**  
- **pandas, numpy, matplotlib, seaborn**  
- **scikit-learn, CatBoost**  
- **NLTK / nltk.sentiment.vader**