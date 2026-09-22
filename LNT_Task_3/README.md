
# Task 3: Dataset Preparation and Preprocessing for Deep Learning

### Objective:

To prepare image or text datasets for deep learning applications through preprocessing and featuretransformation technique

### Deliverables:

1. Preprocessed dataset.
   [raw dataset](LNT_Task_3/Datasets/raw_dataset_titanic.csv)
2. Cleaned dataset.
   [clean dataset](LNT_Task_3/Datasets/clean_dataset_titanic.csv)
3. #### EDA report.
   
   **Key Findings:**

-Strongest Predictors of Survival:

  -Title & Sex: Being female ('Mrs', 'Miss') was the single most significant advantage. Our engineered Title feature captures this nuance better than Sex alone, also showing that young boys ('Master') had a much higher survival rate than adult men ('Mr').
  -Passenger Class: There was a clear survival hierarchy: 1st > 2nd > 3rd class.
  -Age: Children and infants had a higher survival rate.

-Other Influential Factors:

  -Family Size: Traveling in a small family (2-4 members) increased survival chances, while traveling alone or in a very large family decreased them.
  -Fare/Cabin: Having a cabin (and thus paying a higher fare) was strongly correlated with survival, acting as a proxy for wealth and passenger class.
  -Port of Embarkation: Passengers from Cherbourg ('C') had a higher survival rate, possibly because a higher proportion of them were in 1st class.
  
These insights are fundamental for the next step in the data science pipeline: building a predictive machine learning model to forecast survival.


5. Visualization outputs.
   
   a. Univariate analysis
   
   ![](LNT_Task_3/Visualization_outputs/univariate_analysis.png)
   ![](LNT_Task_3/Visualization_outputs/univariate_analysis.png)
   
   b. Bivariate analysis
   
   ![](LNT_Task_3/Visualization_outputs/bivariate feature v survival.png)
   ![](LNT_Task_3/Visualization_outputs/age by survival.png)
   
   c. Catplots
   
   ![](LNT_Task_3/Visualization_outputs/survival by pclass and sex.png)
   ![](LNT_Task_3/Visualization_outputs/survival rate by family size.png)
   ![](LNT_Task_3/Visualization_outputs/survival rate by title.png)
   
   d. Boxplot
   
   ![](LNT_Task_3/Visualization_outputs/boxplot ticket fare.png)
   
   e. Violin plot
   
   ![](LNT_Task_3/Visualization_outputs/survival by age n sex.png)
   
   f. Confusion matrix
   
   ![](LNT_Task_3/Visualization_outputs/correlation matrix.png)

   
7. Documentation of preprocessing steps.
   [documentation](LNT_Task_3/LNT_Task_3 1.ipynb)


### Project Conclusion

This project successfully implemented and cleaned a dataset for deep learning task.

This end-to-end EDA has provided a deep understanding of the Titanic dataset. Our analysis confirms the "women and children first" narrative and highlights the stark social inequalities of the time. Through feature engineering, we've created even more powerful predictors for a potential machine learning model. Lastly, the dataset has been split into train-valid-test split and is ready to be used via a deep learning model.

