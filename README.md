**Students Performance in Exams**

**Description:**
This data set consists of the marks secured by the students in various subjects.

The data has 1000 observations of student exam scores and over 8 column. And we can see that there are no Nan values or missing values in any columns or rows.

We can see that our dataset contains only two dtypes (object & int64). Meanwhile, there are two categories of data: categorical and numeric. Hence, all the columns falling into these need to be explored.

we are trying to understand which factors may affect the student's performance. In order to discover correlations between factors, we will classify the scores into several unique groups.

Let's pay attention that dataset consists of five independent variables which are:

gender: sex of students (male, female) race/ethnicity: race of students (A-E groups) parental level of education: parents' final education lunch: having lunch before test (standard, free/reduced) test preparation course: having completed the preparation course before the test (none,completed)

**Observation:**
Test preparation courses do have an effect on the total scores of the exam. For students that have completed the course, around 75% scores higher than the median of those who did not have a prep course.

Some major factors contributing test scores include, lunch type (really meaning family income) and test prep completion status. Additionally, females with parental education levels of bachelor or master's degrees perform well on the tests. For males, parental education levels of master's also perform well on the tests

Most effective method to increase exam score is still by completing the prep course

Writing scores are correlated with reading scores more than those correlated with math scores.


