# # A/B Testing Analysis of Two Landing Page Variants

## Оглавление / Table of Contents
1. [Постановка задачи / Statement of the Problem](#1-постановка-задачи--statement-of-the-problem)
2. [Анализ данных и их предобработка / Data analysis and preprocessing](#2-анализ-данных-и-их-предобработка--data-analysis-and-preprocessing)
3. [Первичный анализ результатов A/B-тестирования / Initial analysis of A/B testing results](#3-первичный-анализ-результатов-а-в-тестирования--initial-analysis-of-a-b-testing-results)
4. [Анализ данных на предмет стабилизации метрик / Data analysis for metric stabilization](#4-анализ-данных-на-предмет-стабилизации-метрик--data-analysis-for-metric-stabilization)
5. [Статистический анализ результатов A/B-тестирования / Statistical analysis of A/B testing results](#5-статистический-анализ-результатов-а-в-тестировния--statistical-analysis-of-a-b-testing-results)
6. [Общий вывод по результатам A/B-теста / General conclusion based on the A/B test results](#6-общий-вывод-по-результатам-а-в-теста--general-conclusion-based-on-the-a-b-test-result)

---

## 1. Постановка задачи / Statement of the Problem

**Бизнес-задача / Business problem**  
Туристическая фирма планирует запустить новую акцию, чтобы продать как можно больше туров. Команда разработала два варианта посадочной страницы официального сайта и провела A/B-тестирование. В результате эксперимента были собраны данные.
*A travel agency plans to launch a new promotion to sell as many tours as possible. The team developed two landing page variations for the official website and conducted A/B testing. The experiment yielded the following data.*

**Задача**: проанализировать эффективность обоих вариантов посадочной страницы сразу по двум критериям — **конверсии покупки** и **ежедневному среднему чеку**.
*Task: Analyze the effectiveness of both landing page variants based on two criteria at once: **purchase conversion** and **average daily check**.*

Нужно убедиться, что A/B-тестирование было проведено корректно, проверить факт стабилизации метрик и обоснованно ответить на ключевой вопрос турагентства: какой вариант посадочной страницы более предпочтителен по метрикам конверсии и ежедневного среднего чека?
*We need to ensure that the A/B testing was conducted correctly, verify that the metrics have stabilized, and provide a sound answer to the travel agency's key question: which landing page variation is more preferable based on conversion and average daily check metrics?*

Компания предлагает следующие варианты туров:

- Таиланд — 100 000 рублей;
- Турция — 60 000 рублей;
- Мальдивы — 200 000 рублей;
- Санкт-Петербург — 10 000 рублей;
- Камчатка — 150 000 рублей.

*The company offers the following tour options:

- Thailand — 100,000 rubles;
- Turkey — 60,000 rubles;
- Maldives — 200,000 rubles;
- St. Petersburg — 10,000 rubles;
- Kamchatka - 150,000 rubles.*

---

## 2. Анализ данных и их предобработка / Data analysis and preprocessing

- Ознакомление с датасетом, анализ структуры и типов данных  
  *Exploring the dataset, reviewing its structure and data types*
- Проверка корректности эксперимента:
  *Verifying the correctness of the experiment:*
  - сбалансированность распределения выборки в группах А и В
   *balanced distribution of the sample in groups A and B*
  - наличие повторяющихся пользователей в двух группах
   *presence of duplicate users in two groups*

---

## 3. Первичный анализ результатов A/B-тестирования / Initial analysis of A/B testing results

- Рассчет конверсии и среднего чека в каждой из групп 
  *Calculation of conversion and average check in each group*
- Сравнение вариантов A/B по покупательской способности каждого из туров
  *Comparison of A/B options based on the purchasing power of each tour*
- Визуализация данных  
  *Data visualization*
- Вывод по результатам
  *Conclusion on the results*

---

## 4. Анализ данных на предмет стабилизации метрик / Data analysis for metric stabilization

- Рассчет ежедневной конверсии и ежедневного среднего чека по группам 
  *Calculation of daily conversion and daily average check by groups*
- Рассчет кумулятивных показателей 
  *Calculation of cumulative indicators*
- Визуализация графиков кумулятивной конверсии по дням в каждой группе и кумулятивного среднего чека по дням в каждой группе
  *Visualization of graphs of cumulative conversion by days in each group and cumulative average check by days in each group*
- Вывод по результатам
  *Conclusion on the results*

---

## 5. Статистический анализ результатов A/B-тестирования / Statistical analysis of A/B testing results

- Определение статистической разницы между конверсиями в группах А и B
  *Determining the statistical difference between conversions in groups A and B*
- Определение статистической разницы между ежедневными средними чеками в группах А и B
  *Determining the statistical difference between the daily average receipts in groups A and B*
- Построение 95 % доверительные интервалы для конверсий в каждой из групп,
разницы конверсий в группах и ежедневного среднего чека в каждой из групп 
  *Constructing 95% confidence intervals for conversions in each group,
  the difference in conversions between groups, and the daily average order value in each group*
- Вывод по результатам
  *Conclusion on the results* 

---

## 6. Общий вывод по результатам A/B-теста / General conclusion based on the A/B test results

- В ходе A/B-тестирования не было выявлено статистически значимых различий в конверсии между группами A и B: доверительные интервалы пересекаются, а результаты статистического теста не дают оснований отвергнуть нулевую гипотезу.

В то же время средний чек в группе B оказался статистически значимо выше, чем в группе A: доверительные интервалы не пересекаются, а результаты t-теста подтверждают наличие различий.

Таким образом, второй вариант посадочной страницы является более предпочтительным, так как он обеспечивает более высокий средний доход с пользователя.  
  *The A/B testing revealed no statistically significant differences in conversion rates between Groups A and B: the confidence intervals overlap, and the statistical test results provide no basis to reject the null hypothesis.

  However, the average order value in Group B was statistically significantly higher than in Group A: the confidence intervals do not overlap, and the t-test results confirm the differences.

  Therefore, the second landing page variant is preferable, as it yields a higher average revenue per user.*

---

## Notebook

Подробнее с ходом работы можно ознакомиться:
*You can find out more about the progress of the work:*

https://github.com/korolmaria1291/data_science_study/blob/main/project_9

---

## Данные / Data

Оригинальный датасет:  
*The original dataset:*
**(https://github.com/korolmaria1291/data_science_study/blob/main/project_9/ab_data_tourist.csv)**

---

## Используемые инструменты / Tools used

- **Jupyter Notebook**  
- **Python**  
- **pandas, numpy, matplotlib, seaborn**  
- **scipy**  