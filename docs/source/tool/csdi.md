# Missing Value Imputation with CSDI
Most of the raw data retrieved from different data sources consist of missing values (NaN values), and the most common method of dealing with missing values is directly dropping them. However, we provide an alternative solution by using the imputation model proposed in the following paper. 

[CSDI: Conditional Score-based Diffusion Models for Probabilistic Time Series Imputation (Yusuke Tashiro, etc.)](https://arxiv.org/abs/2107.03502) *NeurIPS 2021*

CSDI is a diffusion model which generates missing values in raw data by diffusion process using observed values as conditional input. The model is trained by optimizing an unsupervised task: recovery of a certain ratio of masked observed data by using the rest observed data as conditional input. When performing real imputation on datasets, all missing values are imputation targets and all observed values serve as conditional input. Please refer to the original paper if you have any enquiries about the methodology. 

We implement the model into a ready-to-use toolbox for missing value imputation of financial data. Please refer to [CSDI for financial data imputation](https://github.com/ZONG0004/TradeMaster/blob/main/data/CSDI/README.md) for detailed guideline of usage and visualization results. 

