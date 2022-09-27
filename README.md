# fhnw-ds-cdl1
Activity recognition based on phone sensors.

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

