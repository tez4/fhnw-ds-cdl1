# fhnw-ds-cdl1
Activity recognition based on phone sensors.

## Reports

- [Planning](Planung.md)
- [Preprocessing and Model training](VSR_Report_SensorBasedActivityRecognition_NZu_JGr_HS22.pdf)
- [Decision tree models](https://wandb.ai/cdl1/CDL1/reports/Decision-tree-models-for-Human-sensor-activity-classification--VmlldzozMzAwNTg3?accessToken=f3m76hy7vl4slbxmxiyq9du07rk045c1nzsgutcb0vjy58ew3c98hy1up6ly6a3s)
- [Sequential Deep Learning Models](https://api.wandb.ai/report/cdl1/h26lu1my)

## Jupyter Notebooks

- [Visualizations and Data Exploration](visualizations.ipynb)
- [Preprocessing](preprocessing.ipynb)
- [Logistic Regression](model_logistic_regression.ipynb)
- [Decision Tree and Random Forest](model_decision_tree.ipynb)
- [RNN and CNN](model_NN.ipynb)

## Installation

In this project, we are using Pipenv for dependency management. Thus, you need the `pipenv` CLI tool installed on your computer:

```
pip install pipenv
```

As soon this package is installed, you can install all required packages for this project by executing the following command inside the root project folder:

```
pipenv install
```

If you need another dependency, not yet defined in the `Pipfile`, you can install it using this command and it will also be added to the dependency list.

```
pipenv install <package>
```

Now, to run the Python scripts, you will need to select the right kernel (name should start with `fhnw-ds-cdl1`) or if you are executing them using the CLI, you can switch to the virtual environment with the installed dependencies by running this command:

```
pipenv shell
```

Afterwards you can use the default command to create a juptyer instance:
```
jupyter notebook
```

Or if that does not work you can try the following command:
```
pipenv run jupyter notebook
```

