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

---

## Assignment 2: Spam Email Detection
*(You can add your specific results for Assignment 2 here once the model is trained)*
