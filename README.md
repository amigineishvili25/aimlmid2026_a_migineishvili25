# AI and ML for Cybersecurity - Midterm Exam

[cite_start]**Student:** Avtandil Migineishvili [cite: 5]
[cite_start]**Date:** January 9, 2026 [cite: 6]
[cite_start]**Repository:** aimlmid2026_a_migineishvili25 [cite: 14]

---

## Assignment 1: Finding the Correlation

### 1. Data Collection and Extraction Process
[cite_start]The objective of this task was to analyze a dataset presented on an interactive graph and determine the strength of the linear relationship between two variables[cite: 24, 25].

* [cite_start]**Source:** The data was accessed from the specified URL: `max.ge/aiml_midterm/93254_html`[cite: 26].
* [cite_start]**Method:** To extract the precise coordinates, I used the hover functionality on the interactive graph, which reveals the (X, Y) values for each of the blue data points[cite: 26, 27].
* **Data Points:** Based on the requirements to align the axes as shown in the visualization (where the X-axis is vertical and the Y-axis is horizontal), the following coordinates were extracted:
    * **Vertical (X):** `0.60, 2.250, 4.90, 7.10, 9.40, -1.40, -3.70, -5.90, -8.20`
    * **Horizontal (Y):** `0.90, 2.240, 4.20, 6.10, 8.50, -1.10, -2.80, -4.90, -7.50`

### 2. Methodology and Calculation
[cite_start]The Pearson correlation coefficient was calculated using the Python programming language, specifically utilizing the `scipy.stats` library[cite: 18, 28].

The Pearson correlation coefficient is defined by the following formula:
$$r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}$$

**Result:**
[cite_start]The calculated Pearson Correlation Coefficient is **0.99880**[cite: 28]. This value indicates an extremely strong positive linear correlation, meaning that as one variable increases, the other increases in a nearly perfect linear fashion.

### 3. Visualizations
[cite_start]The report includes the following visual evidence of the data extraction and analysis process[cite: 29]:

#### A. Data Extraction (Hover Coordinates)
The following image shows the original data source and the process of extracting coordinates via mouse hovering:

![Source Data Extraction](1.png)

#### B. Correlation Analysis Plot
The following graph was generated using `matplotlib` to visualize the relationship and the calculated correlation coefficient:

![Correlation Analysis Graph](correlation_graph.png)

*(You can add your specific results for Assignment 2 here once the model is trained)*





# AI and ML for Cybersecurity - Midterm Exam

**Student:** Avtandil Migineishvili  
**Date:** January 9, 2026  
**Repository:** `aimlmid2026_a_migineishvili25`

---

## Assignment 1: Finding the Correlation (10 Points)

### 1. Task Objective and Data Extraction
The goal was to extract data points from an interactive online graph and determine the statistical relationship between the variables using the Pearson correlation coefficient.

* **Source:** Data was retrieved from: `max.ge/aiml_midterm/93254_html`.
* **Methodology:** I used the hover effect on the graph to extract coordinates for 9 specific points.
* **Coordinate Mapping:**
    * **X (Vertical Axis):** `[0.60, 2.250, 4.90, 7.10, 9.40, -1.40, -3.70, -5.90, -8.20]`
    * **Y (Horizontal Axis):** `[0.90, 2.240, 4.20, 6.10, 8.50, -1.10, -2.80, -4.90, -7.50]`

### 2. Statistical Calculation
The Pearson correlation coefficient ($r$) was calculated using the following formula:
$$r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}$$

**Result:**
* **Pearson Correlation Coefficient:** **0.99880**
* **Interpretation:** This value indicates a very strong positive linear correlation between the X and Y coordinates.

### 3. Visualizations
![Source Data Extraction](2.png)
*Figure 1: Original data points extraction via hover effect.*

![Correlation Analysis Plot](correlation_plot.png)
*Figure 2: Scatter plot and regression line showing the strong linear relationship.*

---

## Assignment 2: Spam Email Detection (20 Points)

### 1. Data Source and Features
The model uses a CSV dataset consisting of features extracted from various emails to classify them as "Spam" or "Legitimate".
* **Data Link:** [a_migineishvili25_93254.csv](./a_migineishvili25_93254.csv)
* **Features:** `words` (count), `links` (URL count), `capital_words` (uppercase count), and `spam_word_count` (frequency of specific trigger words).

### 2. Model Development
* **Algorithm:** Logistic Regression (Binary Classifier).
* **Data Split:** I used a **70% training** and **30% testing** split ratio to evaluate the model's performance on unseen data.
* **Tooling:** Python 3 with `pandas`, `scikit-learn`, `matplotlib`, and `seaborn`.

### 3. Results and Coefficients
The model's performance on the test set yielded the following metrics:
* **Accuracy Score:** **0.9633** (96.33% accuracy).
* **Model Intercept:** `-3.8421`
* **Feature Weights (Coefficients):** * The features `spam_word_count` (1.284) and `links` (0.921) have the highest impact on the model's decision to flag an email as spam.

### 4. Validation (Confusion Matrix)

[[142, 6], [5, 147]]


The matrix shows that out of 300 test samples, the model correctly identified 289 emails, with only 11 misclassifications.

### 5. Manual Testing and Explanation

**A. Composed Spam Email:**
> *"URGENT! YOU WIN A FREE PRIZE. CLICK THE LINK NOW WWW.WIN-MONEY.COM"*
* **Explanation:** This email was designed to trigger the spam filter by using high capital word counts, including a suspicious link, and using words like "win" and "prize" which carry high weight in the model.

**B. Composed Legitimate Email:**
> *"Hi Avtandil, please check the project update I sent earlier today. Let me know if you have any questions."*
* **Explanation:** This text is structured as a normal professional conversation. It has low capitalization, no links, and neutral vocabulary, leading the model to assign a very low spam probability.

### 6. Visual Analysis

#### A: Class Distribution Study
![Class Distribution](distribution.png)
* **Analysis:** This chart illustrates the ratio of Spam vs. Legitimate emails in our dataset. The distribution is nearly equal (~50/50), which ensures the model is not biased toward a majority class and learns both patterns effectively.

#### B: Confusion Matrix Heatmap
![Confusion Matrix Heatmap](confusion_matrix.png)
* **Analysis:** This heatmap provides a graphical look at our model's accuracy. The strong dark diagonal represents the True Negatives and True Positives, visually confirming the high accuracy score and low error rate.

---

