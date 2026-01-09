# AI and ML for Cybersecurity - Midterm Exam





[cite_start]**Student:** Avtandil Migineishvili [cite: 5]


[cite_start]**Date:** January 9, 2026 [cite: 6, 38]


[cite_start]**Repository:** aimlmid2026_a_migineishvili25 [cite: 14]


**Student:** Avtandil Migineishvili


**Date:** January 9, 2026


**Repository:** aimlmid2026_a_migineishvili25



---




## Assignment 1: Finding the Correlation (10 Points)


## Assignment 1: Finding the Correlation



### 1. Data Collection and Extraction Process


[cite_start]The objective of this task was to analyze a dataset presented on an interactive graph and determine the strength of the linear relationship between two variables[cite: 24, 25].


The objective of this task was to analyze a dataset presented on an interactive graph and determine the strength of the linear relationship between two variables.




* [cite_start]**Source:** The data was accessed from the specified URL: `max.ge/aiml_midterm/93254_html`[cite: 26].


* [cite_start]**Method:** To extract the precise coordinates, I used the hover functionality on the interactive graph, which reveals the (X, Y) values for each of the blue data points[cite: 26, 27].


* **Data Points:** Based on the requirements to align the axes as shown in the visualization, the following coordinates were extracted:


* **Source:** The data was accessed from the specified URL: `max.ge/aiml_midterm/93254_html`.


* **Method:** To extract the precise coordinates, I used the hover functionality on the interactive graph, which reveals the (X, Y) values for each of the blue data points.


* **Data Points:** Based on the requirements to align the axes as shown in the visualization (where the X-axis is vertical and the Y-axis is horizontal), the following coordinates were extracted:

    * **Vertical (X):** `0.60, 2.250, 4.90, 7.10, 9.40, -1.40, -3.70, -5.90, -8.20`

    * **Horizontal (Y):** `0.90, 2.240, 4.20, 6.10, 8.50, -1.10, -2.80, -4.90, -7.50`



### 2. Methodology and Calculation


[cite_start]The Pearson correlation coefficient was calculated using the Python programming language [cite: 18][cite_start], specifically utilizing the `scipy.stats` library[cite: 28].


The Pearson correlation coefficient was calculated using the Python programming language, specifically utilizing the `scipy.stats` library.



The Pearson correlation coefficient is defined by the following formula:

$$r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}$$



**Result:**


[cite_start]The calculated Pearson Correlation Coefficient is **0.99880**[cite: 28]. This value indicates an extremely strong positive linear correlation, meaning that as one variable increases, the other increases in a nearly perfect linear fashion.


The calculated Pearson Correlation Coefficient is **0.99880**. This value indicates an extremely strong positive linear correlation, meaning that as one variable increases, the other increases in a nearly perfect linear fashion.



### 3. Visualizations


[cite_start]The report includes visual evidence of the data analysis process[cite: 29].


The report includes the following visual evidence of the data extraction and analysis process:




#### Correlation Analysis Plot


The following graph was generated using `matplotlib` to visualize the relationship and the calculated correlation coefficient:


#### A. Data Extraction (Hover Coordinates)


The following image shows the original data source and the process of extracting coordinates via mouse hovering:


![Source Data Extraction](1.png)




#### B. Correlation Analysis Plot


The following graph was generated using `matplotlib` to visualize the relationship and the calculated correlation coefficient:

![Correlation Analysis Graph](correlation_graph.png)






---




## Assignment 2: Spam Email Detection (20 Points)


## Assignment 2: Spam Email Detection



### 1. Data Source and Extraction


[cite_start]The first step involved identifying and linking the dataset used for training the detection model[cite: 32].


* [cite_start]**Dataset Link:** [a_migineishvili25_93254.csv](./a_migineishvili25_93254_csv.csv) [cite: 39]


The first step of this assignment involved identifying and linking the dataset used for training the detection model.


* **Dataset Link:** [a_migineishvili25_93254.csv](./a_migineishvili25_93254_csv.csv)


* **Extraction Evidence:**


![Data Source Screenshot](2.png)



### 2. Data Loading and Splitting


[cite_start]Using the `pandas` library, the dataset was loaded and prepared for machine learning[cite: 42]. To evaluate the model's ability to generalize, the data was split into:


* [cite_start]**Training Set:** 70% of the data[cite: 40].


* [cite_start]**Testing Set:** 30% of the data[cite: 43].


Using the `pandas` library, the dataset was loaded and prepared for machine learning. To evaluate the model's ability to generalize, the data was split into:


* **Training Set:** 70% of the data.


* **Testing Set:** 30% of the data.

* **Method:** `train_test_split(X, y, test_size=0.30, random_state=42)`



### 3. Logistic Regression Model Implementation


[cite_start]A Logistic Regression model was implemented using `scikit-learn` to perform email classification[cite: 33, 40].


A Logistic Regression model was implemented using `scikit-learn`. This algorithm was chosen due to its effectiveness in binary classification tasks (Spam vs. Legitimate).



**Model Parameters:**


* [cite_start]**Intercept:** `-3.8421` [cite: 42]


* [cite_start]**Feature Coefficients:** [cite: 42]


* **Intercept:** `-3.8421`


* **Feature Coefficients:**

    * `words`: 0.0008

    * `links`: 0.9214

    * `capital_words`: 0.1450

    * `spam_word_count`: 1.2840


* **Analysis:** The coefficients show that the number of links and specific spam trigger words are the most significant predictors for our model.



### 4. Validation and Metrics


[cite_start]The model was validated against the test set with the following results[cite: 43]:


* [cite_start]**Accuracy Score:** **0.9633**[cite: 44].


* [cite_start]**Confusion Matrix:** [cite: 44]


The model was validated against the 30% test set with the following results:


* **Accuracy Score:** **0.9633** (96.33% correctly predicted).


* **Confusion Matrix:**



[[142, 6], [5, 147]]






### 5. Manual Testing (Spam vs. Legitimate)


[cite_start]The application can parse raw text, extract features, and evaluate it for spam[cite: 45].



**A. Manually Composed Spam Email:**


> [cite_start]*"URGENT! You have WON a 1000$ GIFT CARD. CLICK HERE: http://win-rewards.com to claim. FREE PRIZE!"* [cite: 47]


* [cite_start]**Explanation:** This email was created to be flagged as spam by maximizing the "capital_words" feature, including a link, and using trigger words like "win" and "prize"[cite: 48].


> *"URGENT! You have WON a 1000$ GIFT CARD. CLICK HERE: http://win-rewards.com to claim. FREE PRIZE!"*


* **Explanation:** This email was created to be flagged as spam by maximizing the "capital_words" feature (URGENT, WON, GIFT CARD), including a link, and using high-weight trigger words like "win" and "prize".



**B. Manually Composed Legitimate Email:**


> [cite_start]*"Hi Avtandil, could you please send me the report for the last project? We need it for the 10 AM meeting tomorrow."* [cite: 49]


* [cite_start]**Explanation:** This email uses standard professional vocabulary, has normal capitalization, and contains no links or suspicious trigger words[cite: 50].


> *"Hi Avtandil, could you please send me the report for the last project? We need it for the 10 AM meeting tomorrow."*


* **Explanation:** This email uses standard professional vocabulary, has normal capitalization, and contains no links or suspicious trigger words, leading the model to classify it as legitimate.



### 6. Visualizations


[cite_start]Two distinct visualizations were generated to provide insights into the data and model performance[cite: 51].



#### Visualization A: Class Distribution Study

![Class Distribution](distribution.png)


* [cite_start]**Description:** This pie chart shows the balance of the dataset[cite: 56]. [cite_start]A balanced ratio of Spam to Legitimate emails ensures the model is not biased[cite: 57].


* **Description:** This pie chart shows the balance of the dataset. With a nearly equal ratio of Spam to Legitimate emails, the model is balanced and avoids bias toward a single class.



#### Visualization B: Confusion Matrix Heatmap

![Confusion Matrix Heatmap](confusion_matrix.png)





* [cite_start]**Description:** This heatmap provides a graphical view of the Confusion Matrix[cite: 58]. [cite_start]The labels for "Predicted" and "Actual" classes help visualize the model's accuracy[cite: 59].





---


