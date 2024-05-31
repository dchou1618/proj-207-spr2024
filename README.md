# proj-207-spr2024

# Data Sources
(1) [Electricity Transformer Datasets](https://github.com/zhouhaoyi/ETDataset)

(2) [Weather dataset](https://drive.google.com/drive/folders/1ohGYWWohJlOlb2gsGTeEq3Wii2egnEPR) from [AAAI paper "Informer"](https://drive.google.com/drive/folders/1ohGYWWohJlOlb2gsGTeEq3Wii2egnEPR)

(3) Specific variables of interest: From the paper, "measuring six power load features and 'oil temperature', the chosen target value for univariate forecasting". We conduct benchmarking on model performance on the `OT` column from the electricity ETT datasets. Similarly, for the weather dataset, the paper mentions that 'wet bulb' was used as the target variable for univariate forecasting, so we inspect either the web bulb farenheit or celsius column. For now, we are working with the `WetBulbCelsius` column.

## Plan

(1) Estimate univariate time series of the two datasets using traditional methods, such as arima, sarima, or possibly farima given the oil temperature data appears to exhibit long-range dependence, and run arima.sim for simulated predictions.

(2) Benchmark CoST against some other deep learning frameworks (time permitting) for univariate data.

(3) Rerun CoST to get metric estimates on local machine, testing the reproducibility of the representation learning and prediction function estimation - *reproducibility as in regenerating metrics using the original author's code and data*.
