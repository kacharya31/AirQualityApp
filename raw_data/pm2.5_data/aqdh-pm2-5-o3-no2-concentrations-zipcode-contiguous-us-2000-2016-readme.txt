December 2022

Daily and Annual PM2.5, O3, and NO2 Concentrations at ZIP Codes for the Contiguous U.S., v1 (2000-2016)


PURPOSE

To provide daily and annual Fine Particulate Matter (PM2.5), Ozone (O3), and Nitrogen Dioxide (NO2) concentrations data at ZIP Codes for the contiguous U.S. for research in environmental epidemiology, environmental justice, and health equity by linking with ZIP Code-level demographic and medical data sets, and for other related research.


DESCRIPTION

The Daily and Annual PM2.5, O3, and NO2 Concentrations at ZIP Codes for the Contiguous U.S., 2000-2016, v1.0 data set contains daily and annual concentration predictions for Fine Particulate Matter (PM2.5), Ozone (O3), and Nitrogen Dioxide (NO2) pollutants at ZIP Code-level for the years 2000 to 2016. Ensemble predictions of three machine-learning models were implemented (Random Forest, Gradient Boosting, and Neural Network) to estimate the daily PM2.5, O3, and NO2 at the centroids of 1km x 1km grid cells across the contiguous U.S. for 2000 to 2016. The predictors included air monitoring data, satellite aerosol optical depth, meteorological conditions, chemical transport model simulations, and land-use variables. The ensemble models demonstrated excellent predictive performance with 10-fold cross-validated R-squared values of 0.86 for PM2.5, 0.86 for O3, and 0.79 for NO2. These high-resolution, well-validated predictions allow for estimates of ZIP Code-level pollution concentrations with a high degree of accuracy. For general ZIP Codes with polygon representations, pollution levels were estimated by averaging the predictions of grid cells whose centroids lie inside the polygon of that ZIP Code; for other ZIP Codes such as Post Offices or large volume single customers, they were treated as a single point and predicted their pollution levels by assigning the predictions using the nearest grid cell. The polygon shapes and points with latitudes and longitudes for ZIP Codes were obtained from Esri and the U.S. ZIP Code Database and were updated annually. The data include about 31,000 general ZIP Codes with polygon representations, and about 10,000 ZIP Codes as single points. The aggregated ZIP Code-level, daily predictions are applicable in research such as environmental epidemiology, environmental justice, health equity, and political science, by linking with ZIP Code-level demographic and medical data sets, including national inpatient care records, medical claims data, census data, U.S. Census Bureau American Community Survey (ACS), and Area Deprivation Index (ADI). The data are particularly useful for studies on rural populations who are under-represented due to the lack of air monitoring sites in rural areas. Compared with the 1km grid data, the ZIP Code-level predictions are much smaller in size and are manageable in personal computing environments. This greatly improves the inclusion of scientists in different fields by lowering the key barrier to participation in air pollution research. The units are μg/m^3 for PM2.5 and ppb for O3 and NO2.


ACCESSING THE DATA

The data may be downloaded at https://sedac.ciesin.columbia.edu/data/set/aqdh-pm2-5-o3-no2-concentrations-zipcode-contiguous-us-2000-2016/data-download


DATA FORMAT

This archive contains the data in RDS and CSV (tabular) formats.
Note: If users open the CSV files in Excel, ZIP Codes starting with 0, 00, 000, or 0000 will be missing those numbers. It is suggested to open the CSV files with a text editor.

The data files are compressed zipfiles. Downloaded files need to be uncompressed in a single folder using either WinZip (Windows file compression utility) or similar application. Users should expect an increase in the size of downloaded data after decompression. 


DATA UNITS

The unit for PM2.5 is micrograms (one-millionth of a gram) per cubic meter air (µg/m^3). The unit for O3 and NO2 is parts per billion (ppb). 


SPATIAL EXTENT

Contiguous United States, ZIP Codes.


DISCLAIMER

CIESIN follows procedures designed to ensure that data disseminated by CIESIN are of reasonable quality. If, despite these procedures, users encounter apparent errors or misstatements in the data, they should contact SEDAC User Services at ciesin.info@ciesin.columbia.edu. Neither CIESIN nor NASA verifies or guarantees the accuracy, reliability, or completeness of any data provided. CIESIN provides this data without warranty of any kind whatsoever, either expressed or implied. CIESIN shall not be liable for incidental, consequential, or special damages arising out of the use of any data provided by CIESIN.


USE CONSTRAINTS

This work is licensed under the Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0). Users are free to use, copy, distribute, transmit, and adapt the work for commercial and non-commercial purposes, without restriction, as long as clear attribution of the source is provided.


CITATION(S)

Data Set:

Yaguang Wei1, Xiaoshi Xing2, Alexandra Shtein1, Edgar Castro1, Carolynne Hultquist2,3, Mahdieh Danesh Yazdi1,4, Longxiang Li1, and Joel Schwartz1. 2022. Daily and Annual PM2.5, O3, and NO2 Concentrations at ZIP Codes for the Contiguous U.S., 2000-2016, v1.0. Palisades, New York: NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/9yp5-hz11. Accessed DAY MONTH YEAR.

1 Harvard T.H. Chan School of Public Health, Boston, MA, United States
2 The Center for International Earth Science Information Network (CIESIN), Columbia University, Palisades, NY, United States
3 School of Earth and Environment, University of Canterbury, Christchurch, New Zealand
4 Stony Brook University, New York, United States

Scientific Publication: 

Wei, Y., X. Qui, M. D. Yazdi, A. Shtein, L. Shi, J. Yang, A. A. Peralta, B. A. Coull, and J. Schwartz. 2022. The Impact of Exposure Measurement Error on the Estimated Concentration–Response Relationship between Long-Term Exposure to PM2.5 and Mortality. Environmental Health Perspectives, 130(7): 077006. https://doi.org/10.1289/EHP10389.


REFERENCES

Wei, Y., X. Qiu, M. B. Sabath, M. D. Yazdi, K. Yin, L. Li, A. A. Peralta, C. Wang, P. Koutrakis, A. Zanobetti, F. Dominici,  and J. D. Schwartz. 2022. Air Pollutants and Asthma Hospitalization in the Medicaid Population. American Journal of Respiratory and Critical Care Medicine, 205(9):1075–1083. https://doi.org/10.1164/rccm.202107-1596OC.

Jbaily, A., X. Zhou, J. Liu, T.-H. Lee, L. Kamareddine, S. Verguet and F. Dominici. 2022. Air pollution exposure disparities across US population and income groups. Nature, 601:228–233. https://doi.org/10.1038/s41586-021-04190-y.

Qiu X, Y. Wei, M. Weisskopf, A. Spiro, L. Shi, E. Castro, B. Coull, P. Koutrakis, and J. Schwartz. 2022. Air pollution, climate conditions and risk of hospital admissions for psychotic disorders in U.S. residents. Environmental Research, 216(Part 2):114636. https://doi.org/10.1016/j.envres.2022.114636.


ACKNOWLEDGEMENTS

The ZIP code polygon and point data from Esri ArcGIS Data and Maps, 2000 to 2016, were provided by Jeff Blossom, Center for Geographic Analysis, Harvard University. This work was made possible by the National Institutes of Health (NIH) grants R01ES032418 and ES-000002. This work was also supported by the U.S. Environmental Protection Agency (EPA) grants RD-8358720 and RD-83587201-0. The contents are solely the responsibility of the grantee and do not necessarily represent the official views of the U.S. EPA. Further, the U.S. EPA does not endorse the purchase of any commercial products or services mentioned in the publication.

