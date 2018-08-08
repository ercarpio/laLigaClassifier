# Predicting the outcome of Football Matches using SVM and Random Forests

This project aims to predict the outcome of football matches of the Spanish League by using SVM and Random Forests approaches.

## Data collection
The input data for these models is gathered using python web scrappers. The three source websites used in this project are:
- [bdfutbol.com](http://www.bdfutbol.com)
- [sofifa.com](http://www.sofifa.com)
- [fifaindex.com](http://www.fifaindex.com)

## Support Vector Machines
The SVM approach used in this project uses the LIBSVM python library. Python scripts are provided to perform the preprocessing of the input data. A trained model was able to achieve a 54.32% accuracy on a validation dataset, a value that is on par with the accuracy achieved by betting sites like Bet365, Bet & Win, and Pinnacle Sports.

## Random Forests
An implementation of a Random Forest approach was done in Java. This implementation includes methods to perform parameter tunning and feature selection. A RF model was able to achieve a 53.22% accuracy on a validation set, a value 1% lower than the benchmark websites mentioned above.

The figure below shows the results obtained on a validation data set.

![misc/figure.PNG]