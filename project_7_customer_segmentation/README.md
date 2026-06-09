# Project-7. Segmentation of online gift shop customers

## Оглавление / Table of Contents
1. [Постановка задачи / Statement of the Problem](#1-постановка-задачи--statement-of-the-problem)
2. [Знакомство с данными и базовый анализ / Getting to Know the Data](#2-знакомство-с-данными-и-базовый-анализ--getting-to-know-the-data)
3. [Разведывательный анализ данных (EDA) / Exploratory Data Analysis](#3-разведывательный-анализ-данных-eda--exploratory-data-analysis)
4. [Моделирование и оценка качества моделей / Modeling and quality assessment of models](#4-моделирование-и-оценка-качества-моделей--modeling-and-analysis-assessment-of-models)
5. [Интерпретация результатов кластеризации / Interpretation of clustering results](#5-интерпретация-результатов-кластеризации--interpretation-of-clustering)
6. [Выводы и определение сегментации клиентов / Conclusions and definition of customer segmentation](#6-выводы-и-определение-сегментации-клиентов--conclusions-and-definition-of-customer-segmentation)
7. [Результаты / Results](#7-результаты--results)

---

## 1. Постановка задачи / Statement of the Problem

**Бизнес-задача / Business problem**  
Произвести сегментацию существующих клиентов онлайн магазина, проинтерпретировать эти сегменты и определить стратегию взаимодействия с ними.
*Segment existing online store customers, interpret these segments, and determine a strategy for interacting with them.*

**Техническая задача / Technical task**  
Построить модель кластеризации клиентов на основе их покупательской способности, частоты заказов и срока давности последней покупки, определить профиль каждого из кластеров.
*Build a customer clustering model based on their purchasing power, order frequency, and the time since their last purchase, and determine the profile of each cluster.*

**Цели проекта / Project objectives**
- Произвести предобработку исходного набора данных о транзакциях
  *Preprocess the original transaction dataset* 
- Провести разведывательный анализ данных и выявить основные закономерности  
  *Conduct exploratory data analysis and identify key patterns*
- Сформировать набор данных о характеристиках каждого из уникальных клиентов 
  *Create a data set of characteristics for each unique customer*
- Построить несколько моделей машинного обучения, решающих задачу кластеризации клиентов, определить количество кластеров и проинтерпретировать их 
  *Build several machine learning models to solve the problem of customer clustering, determine the number of clusters and interpret them*
- Спроектировать процесс предсказания категории интересов клиента и протестировать вашу модель на новых клиентах 
  *Design a customer interest category prediction process and test your model on new customers*

---

## 2. Знакомство с данными и базовый анализ / Getting to Know the Data

- Ознакомление с датасетом, анализ структуры и типов данных  
  *Exploring the dataset, reviewing its structure and data types*
- Преобразование, очистка и анализ данных
  *Data transformation, cleaning and analysis*

---

## 3. Разведывательный анализ данных (EDA) / Exploratory Data Analysis

- Исследование сформированного набора данных  
  *Exploring the prepared dataset*
- Выявление закономерностей и исследование транзакций для извлечения максимум понятной информации из исходных данных
  *Pattern detection and transaction analysis to extract maximum insights from raw data*
- Визуализация данных  
  *Data visualization*
- Построение RFM-таблицы и поиск RFM-выбросов
  *Building an RFM table and finding RFM outliers*

---

## 4. Моделирование и оценка качества моделей / Modeling and quality assessment of models

- Кластеризация на основе RFM-характеристик  
  *Clustering based on RFM characteristics*
- Стандартизирование данных, использование pipeline  
  *Data standardization, pipeline use*
- Подбор оптимального количества кластеров с помощью коэффициента силуэта для 3-х разных моделей моделей: **KMeans**, **AgglomerativeClustering**, **GaussianMixture** 
  *Selecting the optimal number of clusters using the silhouette coefficient for three different models: **KMeans**, **AgglomerativeClustering**, **GaussianMixture**
- Выбор наилучшей модели на основе метрик качества кластеризации:
- **Calinski–Harabasz Index**
- **Davies–Bouldin Index**
  *Selection of the best model based on clustering quality metrics:
- **Calinski–Harabasz Index**
- **Davies–Bouldin Index*** 

---


## 5. Интерпретация результатов кластеризации / Interpretation of clustering results

- Визуализация кластеров в виде 3D-диаграммы
  *Visualization of clusters as a 3D chart*
  (**https://github.com/korolmaria1291/data_science_study/blob/main/project_7/RFM%20Clusters%20of%20Customers.png**)
- Построение профиля кластеров **Radar Chart** 
  *Building a cluster profile **Radar Chart***
  (**https://github.com/korolmaria1291/data_science_study/blob/main/project_7/%D0%A1luster%20profile.png**)

---

## 6. Выводы и определение сегментации клиентов / Conclusions and definition of customer segmentation

- Общий вывод о проделанной работе  
  *General conclusion on the work done*
- Определение сегментации клиентов
  *Defining customer segmentation*

---

## 7. Результаты / Results

Наилучшие результаты кластеризации были достигнуты с использованием алгоритма KMeans с 3 кластерами.

Были выделены три сегмента клиентов:

**Кластер 0 — Лояльные клиенты**
- высокая частота покупок
- высокие общие расходы
- недавняя активность

**Кластер 1 — Неактивные клиенты**
- большой промежуток времени с последней покупки
- низкая частота покупок
- низкие общие расходы

**Кластер 2 — Постоянные клиенты**
- умеренная покупательская активность
- средние расходы

*The best clustering performance was achieved using **KMeans with 3 clusters**.

Three customer segments were identified:

**Cluster 0 — Loyal customers**
- high purchase frequency
- high total spending
- recent activity

**Cluster 1 — Inactive customers**
- long time since last purchase
- low purchase frequency
- low total spending

**Cluster 2 — Regular customers**
- moderate purchasing activity
- average spending*

---

## Notebook

Подробнее с ходом работы можно ознакомиться:
*You can find out more about the progress of the work:*

https://github.com/korolmaria1291/data_science_study/blob/main/project_7/PROJECT-7.%20Segmentation%20of%20online%20gift%20shop%20customers.ipynb

---

## Данные / Data

Оригинальный датасет:  
*The original dataset:*
**(https://github.com/korolmaria1291/data_science_study/blob/main/project_7/data.csv)**

---

## Используемые инструменты / Tools used

- **Jupyter Notebook**  
- **Python**  
- **pandas, numpy, matplotlib, seaborn, plotly**  
- **scikit-learn**  