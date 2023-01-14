Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy
import pandas as pd
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'
import pandas as pd
import matplotlib.pyplot as plt
titanic_data = pd.read_csv('data/train.csv')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    titanic_data = pd.read_csv('data/train.csv')
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\util\_decorators.py", line 211, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\util\_decorators.py", line 331, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 950, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 605, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 1442, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 1735, in _make_engine
    self.handles = get_handle(
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\common.py", line 856, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'data/train.csv'
titanic_data = pd.read_csv('/data/train.csv')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    titanic_data = pd.read_csv('/data/train.csv')
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\util\_decorators.py", line 211, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\util\_decorators.py", line 331, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 950, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 605, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 1442, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 1735, in _make_engine
    self.handles = get_handle(
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\common.py", line 856, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: '/data/train.csv'
titanic_data = pd.read_csv('./data/train.csv')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    titanic_data = pd.read_csv('./data/train.csv')
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\util\_decorators.py", line 211, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\util\_decorators.py", line 331, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 950, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 605, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 1442, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 1735, in _make_engine
    self.handles = get_handle(
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\common.py", line 856, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: './data/train.csv'
titanic_data = pd.read_csv('../data/train.csv')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    titanic_data = pd.read_csv('../data/train.csv')
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\util\_decorators.py", line 211, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\util\_decorators.py", line 331, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 950, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 605, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 1442, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 1735, in _make_engine
    self.handles = get_handle(
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\common.py", line 856, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: '../data/train.csv'
titanic_data = pd.read_csv('train.csv')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    titanic_data = pd.read_csv('train.csv')
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\util\_decorators.py", line 211, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\util\_decorators.py", line 331, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 950, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 605, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 1442, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 1735, in _make_engine
    self.handles = get_handle(
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\common.py", line 856, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'train.csv'
titanic_data = pd.read_csv('/train.csv')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    titanic_data = pd.read_csv('/train.csv')
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\util\_decorators.py", line 211, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\util\_decorators.py", line 331, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 950, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 605, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 1442, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 1735, in _make_engine
    self.handles = get_handle(
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\common.py", line 856, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: '/train.csv'
titanic_data = pd.read_csv('train.csv')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    titanic_data = pd.read_csv('train.csv')
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\util\_decorators.py", line 211, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\util\_decorators.py", line 331, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 950, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 605, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 1442, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 1735, in _make_engine
    self.handles = get_handle(
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\common.py", line 856, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'train.csv'
titanic_data = pd.read_csv('C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκουdata/train.csv')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    titanic_data = pd.read_csv('C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκουdata/train.csv')
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\util\_decorators.py", line 211, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\util\_decorators.py", line 331, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 950, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 605, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 1442, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 1735, in _make_engine
    self.handles = get_handle(
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\common.py", line 856, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκουdata/train.csv'
titanic_data = pd.read_csv('C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/train.csv')
titanic_data
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q

[891 rows x 12 columns]
titanic_data.head()
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]
titanic_data.describe()
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
titanic_data.desccribe()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    titanic_data.desccribe()
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\generic.py", line 5902, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'desccribe'. Did you mean: 'describe'?
titanic_data.describe()
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
import seaborn as sns
sns.heatmap(titanic_data.corr(), cmap="YlGnBu")

Warning (from warnings module):
  File "<pyshell#19>", line 1
FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.
<AxesSubplot: >
list(titanic_data.columns)
['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
titanic_data.drop(['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1)
     PassengerId  Survived  Pclass   Age  SibSp  Parch     Fare
0              1         0       3  22.0      1      0   7.2500
1              2         1       1  38.0      1      0  71.2833
2              3         1       3  26.0      0      0   7.9250
3              4         1       1  35.0      1      0  53.1000
4              5         0       3  35.0      0      0   8.0500
..           ...       ...     ...   ...    ...    ...      ...
886          887         0       2  27.0      0      0  13.0000
887          888         1       1  19.0      0      0  30.0000
888          889         0       3   NaN      1      2  23.4500
889          890         1       1  26.0      0      0  30.0000
890          891         0       3  32.0      0      0   7.7500

[891 rows x 7 columns]
titanic_data
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q

[891 rows x 12 columns]
titanic_data_new = titanic_data.drop(['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1)
titanic_data_new
     PassengerId  Survived  Pclass   Age  SibSp  Parch     Fare
0              1         0       3  22.0      1      0   7.2500
1              2         1       1  38.0      1      0  71.2833
2              3         1       3  26.0      0      0   7.9250
3              4         1       1  35.0      1      0  53.1000
4              5         0       3  35.0      0      0   8.0500
..           ...       ...     ...   ...    ...    ...      ...
886          887         0       2  27.0      0      0  13.0000
887          888         1       1  19.0      0      0  30.0000
888          889         0       3   NaN      1      2  23.4500
889          890         1       1  26.0      0      0  30.0000
890          891         0       3  32.0      0      0   7.7500

[891 rows x 7 columns]
titanic_data_new.describe()
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
titanic_data_new.describe()
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
sns.heatmap(titanic_data_new.corr(), cmap="YlGnBu")
<AxesSubplot: >
plt.show()
from sklearn.model_selection import StratifiedShuffleSplit
split = StratifiedShuffleSplit(n_plit=1, test_size=0.2)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    split = StratifiedShuffleSplit(n_plit=1, test_size=0.2)
TypeError: StratifiedShuffleSplit.__init__() got an unexpected keyword argument 'n_plit'
split = StratifiedShuffleSplit(n_split=1, test_size=0.2)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    split = StratifiedShuffleSplit(n_split=1, test_size=0.2)
TypeError: StratifiedShuffleSplit.__init__() got an unexpected keyword argument 'n_split'
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2)
for train_indices, test_indices = in split.split(titanic_data, titanic_data[["Survived", "Pclass", "Sex"]]):
    
SyntaxError: invalid syntax
for train_indices, test_indices in split.split(titanic_data, titanic_data[["Survived", "Pclass", "Sex"]]):
strat_train_set = titanic_data.loc[train_indices]
SyntaxError: expected an indented block after 'for' statement on line 1
for train_indices, test_indices in split.split(titanic_data, titanic_data[["Survived", "Pclass", "Sex"]]):
strat_train_set = titanic_data.loc[train_indices]
SyntaxError: expected an indented block after 'for' statement on line 1
for train_indices, test_indices in split.split(titanic_data, titanic_data[["Survived", "Pclass", "Sex"]]):
strat_train_set = titanic_data.loc[train_indices]
SyntaxError: expected an indented block after 'for' statement on line 1
for train_indices, test_indices in split.split(titanic_data, titanic_data[["Survived", "Pclass", "Sex"]]):
    strat_train_set = titanic_data.loc[train_indices]
    strat_test_set = titanic_data.loc[test_indices]
strat_test_test
SyntaxError: incomplete input
strat_test_set
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    strat_test_set
NameError: name 'strat_test_set' is not defined
strat_test_set
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    strat_test_set
NameError: name 'strat_test_set' is not defined
for train_indices, test_indices in split.split(titanic_data, titanic_data[["Survived", "Pclass", "Sex"]]):
    strat_train_set = titanic_data.loc[train_indices]
    strat_test_set = titanic_data.loc[test_indices]
strat_test_set
SyntaxError: incomplete input
for train_indices, test_indices in split.split(titanic_data, titanic_data[["Survived", "Pclass", "Sex"]]):
    strat_train_set = titanic_data.loc[train_indices]
    strat_test_set = titanic_data.loc[test_indices]
    strat_test_set

     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
881          882         0       3  ...   7.8958   NaN         S
109          110         1       3  ...  24.1500   NaN         Q
515          516         0       1  ...  34.0208   D46         S
589          590         0       3  ...   8.0500   NaN         S
86            87         0       3  ...  34.3750   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
624          625         0       3  ...  16.1000   NaN         S
705          706         0       2  ...  26.0000   NaN         S
262          263         0       1  ...  79.6500   E67         S
424          425         0       3  ...  20.2125   NaN         S
353          354         0       3  ...  17.8000   NaN         S

[179 rows x 12 columns]
plt.subplot(1,2,1)
<AxesSubplot: >
strat_train_set["Survived"].hist()
<AxesSubplot: >
strat_train_set["Pclass"].hist()
<AxesSubplot: >
plt.subplot(1,2,2,)
<AxesSubplot: >
strat_test_set["Survived"],hist9)
  
SyntaxError: unmatched ')'
strat_test_set["Survived"],hist()
  
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    strat_test_set["Survived"],hist()
NameError: name 'hist' is not defined. Did you mean: 'list'?
strat_test_set["Survived"].hist()
  
<AxesSubplot: >
strat_test_set["Pclass"].hist()
  
<AxesSubplot: >
plt.show()
  
strat_train_set.info()
  
<class 'pandas.core.frame.DataFrame'>
Int64Index: 712 entries, 682 to 379
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  712 non-null    int64  
 1   Survived     712 non-null    int64  
 2   Pclass       712 non-null    int64  
 3   Name         712 non-null    object 
 4   Sex          712 non-null    object 
 5   Age          572 non-null    float64
 6   SibSp        712 non-null    int64  
 7   Parch        712 non-null    int64  
 8   Ticket       712 non-null    object 
 9   Fare         712 non-null    float64
 10  Cabin        161 non-null    object 
 11  Embarked     711 non-null    object 
dtypes: float64(2), int64(5), object(5)
memory usage: 72.3+ KB
from sklearn.base import BaseEstimator, TransformerMixin
  
from sklearn.imputer import SimpleImputer
  
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    from sklearn.imputer import SimpleImputer
ModuleNotFoundError: No module named 'sklearn.imputer'
from sklearn.imputer import SimpleImputer
  
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    from sklearn.imputer import SimpleImputer
ModuleNotFoundError: No module named 'sklearn.imputer'
from sklearn.preprocessing.Imputer import SimpleImputer
  
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    from sklearn.preprocessing.Imputer import SimpleImputer
ModuleNotFoundError: No module named 'sklearn.preprocessing.Imputer'
import sklearn.impute
from sklearn import impute
from sklearn.impute import SimpleImputer
class AgeIMputer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        imputer = SimpleIMputer(strategy="mean")
        X["Age"] = imputer.fit_transform(X[["Age"]])
        return X

    
from sklearn.preprocessing import OneHotEncoder
class FeautureEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        encoder = OneHotEncoder()
        matrix = encoder.fit_transform(X[["Embarked"]]).toarray()

        
from sklearn.preprocessing import OneHotEncoder
class FeautureEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        encoder = OneHotEncoder()
        matrix = encoder.fit_transform(X[["Embarked"]]).toarray()
        
SyntaxError: multiple statements found while compiling a single statement
from sklearn.preprocessing import OneHotEncoder
class FeautureEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        encoder = OneHotEncoder()
        matrix = encoder.fit_transform(X[["Embarked"]]).toarray()
        
SyntaxError: multiple statements found while compiling a single statement
from sklearn.preprocessing import OneHotEncoder
class FeautureEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        encoder = OneHotEncoder()
        
        matrix = encoder.fit_transform(X[["Embarked"]]).toarray()
        
SyntaxError: multiple statements found while compiling a single statement
from sklearn.preprocessing import OneHotEncoder
class FeautureEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        encoder = OneHotEncoder()
        matrix = encoder.fit_transform(X[["Embarked"]]).toarray()
        column_names = ["C", "S", "Q", "N"]
        
SyntaxError: multiple statements found while compiling a single statement
from sklearn.preprocessing import OneHotEncoder
class FeautureEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        encoder = OneHotEncoder()
        matrix = encoder.fit_transform(X[["Embarked"]]).toarray()
        
        
KeyboardInterrupt
column_names = ["C", "S", "Q", "N"]
from sklearn.preprocessing import OneHotEncoder
class FeautureEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        encoder = OneHotEncoder()
        matrix = encoder.fit_transform(X[["Embarked"]]).toarray()
        column_names = ["C", "S", "Q", "N"]
        for i in range(len(matrix.T)):
            
SyntaxError: multiple statements found while compiling a single statement
from sklearn.preprocessing import OneHotEncoder
class FeautureEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        encoder = OneHotEncoder()
        matrix = encoder.fit_transform(X[["Embarked"]]).toarray()
        column_names = ["C", "S", "Q", "N"]
        for i in range(len(matrix.T)):
            X[columns_names[i]] = matrix.T[i]
        matrix = encoder.fit_transform(X[["Sex"]]).toarray()   
        column_names = ["Female", "Male"]
        for i in range(len(matrix.T)):
            X[column_names[i]] = matrix.T[i]
        return X
    
SyntaxError: multiple statements found while compiling a single statement
class FeautureEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        encoder = OneHotEncoder()
        matrix = encoder.fit_transform(X[["Embarked"]]).toarray()
        column_names = ["C", "S", "Q", "N"]
        for i in range(len(matrix.T)):
            X[columns_names[i]] = matrix.T[i]
        matrix = encoder.fit_transform(X[["Sex"]]).toarray()   
        column_names = ["Female", "Male"]
        for i in range(len(matrix.T)):
            X[column_names[i]] = matrix.T[i]
        return X

    
class FeautureDropper(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X.drop(["Emabrked", "Name", "Ticket", "Cabin", "Sex", "N"], axis=1, errors="ignore")

    
from sklearn.pipeline import Pipeline
pipeline = Pipeline("ageimputer", AgeIMputer()), ("featureencoder", FeatureEncoder()), ("featuredropper", FeatureDropper)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    pipeline = Pipeline("ageimputer", AgeIMputer()), ("featureencoder", FeatureEncoder()), ("featuredropper", FeatureDropper)
TypeError: Pipeline.__init__() takes 2 positional arguments but 3 were given
pipeline = Pipeline([("ageimputer", AgeIMputer()), ("featureencoder", FeatureEncoder()), ("featuredropper", FeatureDropper())])
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    pipeline = Pipeline([("ageimputer", AgeIMputer()), ("featureencoder", FeatureEncoder()), ("featuredropper", FeatureDropper())])
NameError: name 'FeatureEncoder' is not defined. Did you mean: 'FeautureEncoder'?
class FeatureEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        encoder = OneHotEncoder()
        matrix = encoder.fit_transform(X[["Embarked"]]).toarray()
        column_names = ["C", "S", "Q", "N"]
        for i in range(len(matrix.T)):
            X[columns_names[i]] = matrix.T[i]
        matrix = encoder.fit_transform(X[["Sex"]]).toarray()   
        column_names = ["Female", "Male"]
        for i in range(len(matrix.T)):
            X[column_names[i]] = matrix.T[i]
        return X

    

pipeline = Pipeline([("ageimputer", AgeIMputer()), ("featureencoder", FeatureEncoder()), ("featuredropper", FeatureDropper())])
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    pipeline = Pipeline([("ageimputer", AgeIMputer()), ("featureencoder", FeatureEncoder()), ("featuredropper", FeatureDropper())])
NameError: name 'FeatureDropper' is not defined. Did you mean: 'FeautureDropper'?
class FeatureDropper(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X.drop(["Emabrked", "Name", "Ticket", "Cabin", "Sex", "N"], axis=1, errors="ignore")

    
pipeline = Pipeline([("ageimputer", AgeIMputer()), ("featureencoder", FeatureEncoder()), ("featuredropper", FeatureDropper())])

strat_train_set = pipeline.fit_transform(strat_train_set)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    strat_train_set = pipeline.fit_transform(strat_train_set)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\pipeline.py", line 438, in fit_transform
    Xt = self._fit(X, y, **fit_params_steps)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\pipeline.py", line 360, in _fit
    X, fitted_transformer = fit_transform_one_cached(
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\joblib\memory.py", line 349, in __call__
    return self.func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\pipeline.py", line 894, in _fit_transform_one
    res = transformer.fit_transform(X, y, **fit_params)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\base.py", line 848, in fit_transform
    return self.fit(X, **fit_params).transform(X)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "<pyshell#72>", line 5, in transform
    imputer = SimpleIMputer(strategy="mean")
NameError: name 'SimpleIMputer' is not defined. Did you mean: 'SimpleImputer'?
class AgeIMputer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        imputer = SimpleImputer(strategy="mean")
        X["Age"] = imputer.fit_transform(X[["Age"]])
        return X

    
strat_train_set = pipeline.fit_transform(strat_train_set)

Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    strat_train_set = pipeline.fit_transform(strat_train_set)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\pipeline.py", line 438, in fit_transform
    Xt = self._fit(X, y, **fit_params_steps)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\pipeline.py", line 360, in _fit
    X, fitted_transformer = fit_transform_one_cached(
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\joblib\memory.py", line 349, in __call__
    return self.func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\pipeline.py", line 894, in _fit_transform_one
    res = transformer.fit_transform(X, y, **fit_params)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\base.py", line 848, in fit_transform
    return self.fit(X, **fit_params).transform(X)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "<pyshell#72>", line 5, in transform
    imputer = SimpleIMputer(strategy="mean")
NameError: name 'SimpleIMputer' is not defined. Did you mean: 'SimpleImputer'?
class AgeImputer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        imputer = SimpleImputer(strategy="mean")
        X["Age"] = imputer.fit_transform(X[["Age"]])
        return X

    
strat_train_set = pipeline.fit_transform(strat_train_set)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    strat_train_set = pipeline.fit_transform(strat_train_set)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\pipeline.py", line 438, in fit_transform
    Xt = self._fit(X, y, **fit_params_steps)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\pipeline.py", line 360, in _fit
    X, fitted_transformer = fit_transform_one_cached(
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\joblib\memory.py", line 349, in __call__
    return self.func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\pipeline.py", line 894, in _fit_transform_one
    res = transformer.fit_transform(X, y, **fit_params)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\base.py", line 848, in fit_transform
    return self.fit(X, **fit_params).transform(X)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "<pyshell#72>", line 5, in transform
    imputer = SimpleIMputer(strategy="mean")
NameError: name 'SimpleIMputer' is not defined. Did you mean: 'SimpleImputer'?
class AgeImputer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        imputer = SimpleImputer(strategy="mean")
        X["Age"] = imputer.fit_transform(X[["Age"]])
        return X

    
    
pipeline = Pipeline([("ageimputer", AgeImputer()), ("featureencoder", FeatureEncoder()), ("featuredropper", FeatureDropper())])
strat_train_set = pipeline.fit_transform(strat_train_set)

Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    strat_train_set = pipeline.fit_transform(strat_train_set)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\pipeline.py", line 438, in fit_transform
    Xt = self._fit(X, y, **fit_params_steps)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\pipeline.py", line 360, in _fit
    X, fitted_transformer = fit_transform_one_cached(
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\joblib\memory.py", line 349, in __call__
    return self.func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\pipeline.py", line 894, in _fit_transform_one
    res = transformer.fit_transform(X, y, **fit_params)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\base.py", line 848, in fit_transform
    return self.fit(X, **fit_params).transform(X)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "<pyshell#100>", line 9, in transform
    X[columns_names[i]] = matrix.T[i]
NameError: name 'columns_names' is not defined. Did you mean: 'column_names'?
class FeatureEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        encoder = OneHotEncoder()
        matrix = encoder.fit_transform(X[["Embarked"]]).toarray()
        column_names = ["C", "S", "Q", "N"]
        for i in range(len(matrix.T)):
            X[column_names[i]] = matrix.T[i]
        matrix = encoder.fit_transform(X[["Sex"]]).toarray()   
        column_names = ["Female", "Male"]
        for i in range(len(matrix.T)):
            X[column_names[i]] = matrix.T[i]
        return X

    
pipeline = Pipeline([("ageimputer", AgeImputer()), ("featureencoder", FeatureEncoder()), ("featuredropper", FeatureDropper())])

strat_train_set = pipeline.fit_transform(strat_train_set)

strat_train_set
     PassengerId  Survived  Pclass        Age  ...    S    Q  Female Male
682          683         0       3  20.000000  ...  0.0  1.0     0.0  1.0
648          649         0       3  29.739808  ...  0.0  1.0     0.0  1.0
677          678         1       3  18.000000  ...  0.0  1.0     1.0  0.0
605          606         0       3  36.000000  ...  0.0  1.0     0.0  1.0
378          379         0       3  20.000000  ...  0.0  0.0     0.0  1.0
..           ...       ...     ...        ...  ...  ...  ...     ...  ...
287          288         0       3  22.000000  ...  0.0  1.0     0.0  1.0
459          460         0       3  29.739808  ...  1.0  0.0     0.0  1.0
108          109         0       3  38.000000  ...  0.0  1.0     0.0  1.0
661          662         0       3  40.000000  ...  0.0  0.0     0.0  1.0
379          380         0       3  19.000000  ...  0.0  1.0     0.0  1.0

[712 rows x 13 columns]
strat_train_set.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 712 entries, 682 to 379
Data columns (total 13 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  712 non-null    int64  
 1   Survived     712 non-null    int64  
 2   Pclass       712 non-null    int64  
 3   Age          712 non-null    float64
 4   SibSp        712 non-null    int64  
 5   Parch        712 non-null    int64  
 6   Fare         712 non-null    float64
 7   Embarked     711 non-null    object 
 8   C            712 non-null    float64
 9   S            712 non-null    float64
 10  Q            712 non-null    float64
 11  Female       712 non-null    float64
 12  Male         712 non-null    float64
dtypes: float64(7), int64(5), object(1)
memory usage: 77.9+ KB
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_data = scaler.fit_transform(X)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    X_data = scaler.fit_transform(X)
NameError: name 'X' is not defined
X = strat_train_set.drop(['Survived'], axis=1)
Y = strat_train_set['Survived']
scaler = StandardScaler()
X_data = scaler.fit_transform(X)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    X_data = scaler.fit_transform(X)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\base.py", line 848, in fit_transform
    return self.fit(X, **fit_params).transform(X)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\preprocessing\_data.py", line 824, in fit
    return self.partial_fit(X, y, sample_weight)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\preprocessing\_data.py", line 861, in partial_fit
    X = self._validate_data(
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\base.py", line 535, in _validate_data
    X = check_array(X, input_name="X", **check_params)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\validation.py", line 877, in check_array
    array = _asarray_with_order(array, order=order, dtype=dtype, xp=xp)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_array_api.py", line 185, in _asarray_with_order
    array = numpy.asarray(array, order=order, dtype=dtype)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\generic.py", line 2070, in __array__
    return np.asarray(self._values, dtype=dtype)
ValueError: could not convert string to float: 'S'
strat_train_set
     PassengerId  Survived  Pclass        Age  ...    S    Q  Female Male
682          683         0       3  20.000000  ...  0.0  1.0     0.0  1.0
648          649         0       3  29.739808  ...  0.0  1.0     0.0  1.0
677          678         1       3  18.000000  ...  0.0  1.0     1.0  0.0
605          606         0       3  36.000000  ...  0.0  1.0     0.0  1.0
378          379         0       3  20.000000  ...  0.0  0.0     0.0  1.0
..           ...       ...     ...        ...  ...  ...  ...     ...  ...
287          288         0       3  22.000000  ...  0.0  1.0     0.0  1.0
459          460         0       3  29.739808  ...  1.0  0.0     0.0  1.0
108          109         0       3  38.000000  ...  0.0  1.0     0.0  1.0
661          662         0       3  40.000000  ...  0.0  0.0     0.0  1.0
379          380         0       3  19.000000  ...  0.0  1.0     0.0  1.0

[712 rows x 13 columns]
from sklearn.preprocessing import StandardScaler
X = strat_train_set.drop(['Survived'], axis=1)
Y = strat_train_set['Survived']
scaler = StandardScaler()
X_data = scaler.fit_transform(X)
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    X_data = scaler.fit_transform(X)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\base.py", line 848, in fit_transform
    return self.fit(X, **fit_params).transform(X)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\preprocessing\_data.py", line 824, in fit
    return self.partial_fit(X, y, sample_weight)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\preprocessing\_data.py", line 861, in partial_fit
    X = self._validate_data(
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\base.py", line 535, in _validate_data
    X = check_array(X, input_name="X", **check_params)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\validation.py", line 877, in check_array
    array = _asarray_with_order(array, order=order, dtype=dtype, xp=xp)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_array_api.py", line 185, in _asarray_with_order
    array = numpy.asarray(array, order=order, dtype=dtype)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\generic.py", line 2070, in __array__
    return np.asarray(self._values, dtype=dtype)
ValueError: could not convert string to float: 'S'

= RESTART: C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py
Traceback (most recent call last):
  File "C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py", line 5, in <module>
    titanic_data = pd.read_csv('C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκουdata/train.csv')
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\util\_decorators.py", line 211, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\util\_decorators.py", line 331, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 950, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 605, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 1442, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\parsers\readers.py", line 1735, in _make_engine
    self.handles = get_handle(
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\common.py", line 856, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκουdata/train.csv'

= RESTART: C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py

= RESTART: C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py

Warning (from warnings module):
  File "C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py", line 9
    sns.heatmap(titanic_data.corr(), cmap="YlGnBu")
FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.
Traceback (most recent call last):
  File "C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py", line 18, in <module>
    split = StratifiedShuffleSplit(n_plit=1, test_size=0.2)
TypeError: StratifiedShuffleSplit.__init__() got an unexpected keyword argument 'n_plit'

= RESTART: C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py

Warning (from warnings module):
  File "C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py", line 9
    sns.heatmap(titanic_data.corr(), cmap="YlGnBu")
FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.

= RESTART: C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py

Warning (from warnings module):
  File "C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py", line 9
    sns.heatmap(titanic_data.corr(), cmap="YlGnBu")
FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.
Traceback (most recent call last):
  File "C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py", line 28, in <module>
    strat_test_set["Survived"],hist()
NameError: name 'hist' is not defined. Did you mean: 'list'?

= RESTART: C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py

Warning (from warnings module):
  File "C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py", line 9
    sns.heatmap(titanic_data.corr(), cmap="YlGnBu")
FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.
<class 'pandas.core.frame.DataFrame'>
Int64Index: 712 entries, 138 to 192
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  712 non-null    int64  
 1   Survived     712 non-null    int64  
 2   Pclass       712 non-null    int64  
 3   Name         712 non-null    object 
 4   Sex          712 non-null    object 
 5   Age          568 non-null    float64
 6   SibSp        712 non-null    int64  
 7   Parch        712 non-null    int64  
 8   Ticket       712 non-null    object 
 9   Fare         712 non-null    float64
 10  Cabin        164 non-null    object 
 11  Embarked     711 non-null    object 
dtypes: float64(2), int64(5), object(5)
memory usage: 72.3+ KB
Traceback (most recent call last):
  File "C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py", line 36, in <module>
    class AgeImputer(BaseEstimator, TransformerMixin):
NameError: name 'BaseEstimator' is not defined

= RESTART: C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py

Warning (from warnings module):
  File "C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py", line 9
    sns.heatmap(titanic_data.corr(), cmap="YlGnBu")
FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.
<class 'pandas.core.frame.DataFrame'>
Int64Index: 712 entries, 590 to 880
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  712 non-null    int64  
 1   Survived     712 non-null    int64  
 2   Pclass       712 non-null    int64  
 3   Name         712 non-null    object 
 4   Sex          712 non-null    object 
 5   Age          573 non-null    float64
 6   SibSp        712 non-null    int64  
 7   Parch        712 non-null    int64  
 8   Ticket       712 non-null    object 
 9   Fare         712 non-null    float64
 10  Cabin        160 non-null    object 
 11  Embarked     710 non-null    object 
dtypes: float64(2), int64(5), object(5)
memory usage: 72.3+ KB
Traceback (most recent call last):
  File "C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py", line 70, in <module>
    pipeline = Pipeline([("ageimputer", AgeIMputer()), ("featureencoder", FeatureEncoder()), ("featuredropper", FeatureDropper())])
NameError: name 'Pipeline' is not defined

= RESTART: C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py

Warning (from warnings module):
  File "C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py", line 9
    sns.heatmap(titanic_data.corr(), cmap="YlGnBu")
FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.
<class 'pandas.core.frame.DataFrame'>
Int64Index: 712 entries, 103 to 313
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  712 non-null    int64  
 1   Survived     712 non-null    int64  
 2   Pclass       712 non-null    int64  
 3   Name         712 non-null    object 
 4   Sex          712 non-null    object 
 5   Age          565 non-null    float64
 6   SibSp        712 non-null    int64  
 7   Parch        712 non-null    int64  
 8   Ticket       712 non-null    object 
 9   Fare         712 non-null    float64
 10  Cabin        161 non-null    object 
 11  Embarked     710 non-null    object 
dtypes: float64(2), int64(5), object(5)
memory usage: 72.3+ KB
Traceback (most recent call last):
  File "C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py", line 70, in <module>
    pipeline = Pipeline([("ageimputer", AgeIMputer()), ("featureencoder", FeatureEncoder()), ("featuredropper", FeatureDropper())])
NameError: name 'AgeIMputer' is not defined. Did you mean: 'AgeImputer'?

= RESTART: C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py

Warning (from warnings module):
  File "C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py", line 9
    sns.heatmap(titanic_data.corr(), cmap="YlGnBu")
FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.
<class 'pandas.core.frame.DataFrame'>
Int64Index: 712 entries, 863 to 541
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  712 non-null    int64  
 1   Survived     712 non-null    int64  
 2   Pclass       712 non-null    int64  
 3   Name         712 non-null    object 
 4   Sex          712 non-null    object 
 5   Age          574 non-null    float64
 6   SibSp        712 non-null    int64  
 7   Parch        712 non-null    int64  
 8   Ticket       712 non-null    object 
 9   Fare         712 non-null    float64
 10  Cabin        164 non-null    object 
 11  Embarked     710 non-null    object 
dtypes: float64(2), int64(5), object(5)
memory usage: 72.3+ KB
strat_train_set = pipeline.fit_transform(strat_train_set)
strat_train_set
     PassengerId  Survived  Pclass        Age  ...    S    Q  Female Male
863          864         0       3  29.778171  ...  0.0  1.0     1.0  0.0
627          628         1       1  21.000000  ...  0.0  1.0     1.0  0.0
157          158         0       3  30.000000  ...  0.0  1.0     0.0  1.0
112          113         0       3  22.000000  ...  0.0  1.0     0.0  1.0
86            87         0       3  16.000000  ...  0.0  1.0     0.0  1.0
..           ...       ...     ...        ...  ...  ...  ...     ...  ...
561          562         0       3  40.000000  ...  0.0  1.0     0.0  1.0
818          819         0       3  43.000000  ...  0.0  1.0     0.0  1.0
2              3         1       3  26.000000  ...  0.0  1.0     1.0  0.0
23            24         1       1  28.000000  ...  0.0  1.0     0.0  1.0
541          542         0       3   9.000000  ...  0.0  1.0     1.0  0.0

[712 rows x 13 columns]
from sklearn.preprocessing import StandardScaler
X = strat_train_set.drop(['Survived'], axis=1)
Y = strat_train_set['Survived']
scaler = StandardScaler()
X_data = scaler.fit_transform(X)
SyntaxError: multiple statements found while compiling a single statement
from sklearn.preprocessing import StandardScaler
X = strat_train_set.drop(['Survived'], axis=1)
X
     PassengerId  Pclass        Age  SibSp  Parch  ...    C    S    Q  Female  Male
863          864       3  29.778171      8      2  ...  0.0  0.0  1.0     1.0   0.0
627          628       1  21.000000      0      0  ...  0.0  0.0  1.0     1.0   0.0
157          158       3  30.000000      0      0  ...  0.0  0.0  1.0     0.0   1.0
112          113       3  22.000000      0      0  ...  0.0  0.0  1.0     0.0   1.0
86            87       3  16.000000      1      3  ...  0.0  0.0  1.0     0.0   1.0
..           ...     ...        ...    ...    ...  ...  ...  ...  ...     ...   ...
561          562       3  40.000000      0      0  ...  0.0  0.0  1.0     0.0   1.0
818          819       3  43.000000      0      0  ...  0.0  0.0  1.0     0.0   1.0
2              3       3  26.000000      0      0  ...  0.0  0.0  1.0     1.0   0.0
23            24       1  28.000000      0      0  ...  0.0  0.0  1.0     0.0   1.0
541          542       3   9.000000      4      2  ...  0.0  0.0  1.0     1.0   0.0

[712 rows x 12 columns]
Y = strat_train_set['Survived']
scaler = StandardScaler()
X_data= scaler.fit_transform(X)
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    X_data= scaler.fit_transform(X)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\base.py", line 848, in fit_transform
    return self.fit(X, **fit_params).transform(X)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\preprocessing\_data.py", line 824, in fit
    return self.partial_fit(X, y, sample_weight)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\preprocessing\_data.py", line 861, in partial_fit
    X = self._validate_data(
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\base.py", line 535, in _validate_data
    X = check_array(X, input_name="X", **check_params)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\validation.py", line 877, in check_array
    array = _asarray_with_order(array, order=order, dtype=dtype, xp=xp)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_array_api.py", line 185, in _asarray_with_order
    array = numpy.asarray(array, order=order, dtype=dtype)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\generic.py", line 2070, in __array__
    return np.asarray(self._values, dtype=dtype)
ValueError: could not convert string to float: 'S'

= RESTART: C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py

Warning (from warnings module):
  File "C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py", line 9
    sns.heatmap(titanic_data.corr(), cmap="YlGnBu")
FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.
<class 'pandas.core.frame.DataFrame'>
Int64Index: 712 entries, 596 to 133
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  712 non-null    int64  
 1   Survived     712 non-null    int64  
 2   Pclass       712 non-null    int64  
 3   Name         712 non-null    object 
 4   Sex          712 non-null    object 
 5   Age          569 non-null    float64
 6   SibSp        712 non-null    int64  
 7   Parch        712 non-null    int64  
 8   Ticket       712 non-null    object 
 9   Fare         712 non-null    float64
 10  Cabin        167 non-null    object 
 11  Embarked     710 non-null    object 
dtypes: float64(2), int64(5), object(5)
memory usage: 72.3+ KB
Traceback (most recent call last):
  File "C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py", line 78, in <module>
    X_data = scaler.fit_transform(X)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\base.py", line 848, in fit_transform
    return self.fit(X, **fit_params).transform(X)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\preprocessing\_data.py", line 824, in fit
    return self.partial_fit(X, y, sample_weight)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\preprocessing\_data.py", line 861, in partial_fit
    X = self._validate_data(
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\base.py", line 535, in _validate_data
    X = check_array(X, input_name="X", **check_params)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\validation.py", line 877, in check_array
    array = _asarray_with_order(array, order=order, dtype=dtype, xp=xp)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_array_api.py", line 185, in _asarray_with_order
    array = numpy.asarray(array, order=order, dtype=dtype)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\generic.py", line 2070, in __array__
    return np.asarray(self._values, dtype=dtype)
ValueError: could not convert string to float: 'S'
strat_train_set.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 712 entries, 596 to 133
Data columns (total 13 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  712 non-null    int64  
 1   Survived     712 non-null    int64  
 2   Pclass       712 non-null    int64  
 3   Age          712 non-null    float64
 4   SibSp        712 non-null    int64  
 5   Parch        712 non-null    int64  
 6   Fare         712 non-null    float64
 7   Embarked     710 non-null    object 
 8   C            712 non-null    float64
 9   S            712 non-null    float64
 10  Q            712 non-null    float64
 11  Female       712 non-null    float64
 12  Male         712 non-null    float64
dtypes: float64(7), int64(5), object(1)
memory usage: 77.9+ KB
strat_train_set = strat_train_set.drop('Embarked', axis=1)
strat_train_set.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 712 entries, 596 to 133
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  712 non-null    int64  
 1   Survived     712 non-null    int64  
 2   Pclass       712 non-null    int64  
 3   Age          712 non-null    float64
 4   SibSp        712 non-null    int64  
 5   Parch        712 non-null    int64  
 6   Fare         712 non-null    float64
 7   C            712 non-null    float64
 8   S            712 non-null    float64
 9   Q            712 non-null    float64
 10  Female       712 non-null    float64
 11  Male         712 non-null    float64
dtypes: float64(7), int64(5)
memory usage: 72.3 KB
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_data = scaler.fit_transform(X)
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    X_data = scaler.fit_transform(X)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_set_output.py", line 142, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\base.py", line 848, in fit_transform
    return self.fit(X, **fit_params).transform(X)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\preprocessing\_data.py", line 824, in fit
    return self.partial_fit(X, y, sample_weight)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\preprocessing\_data.py", line 861, in partial_fit
    X = self._validate_data(
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\base.py", line 535, in _validate_data
    X = check_array(X, input_name="X", **check_params)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\validation.py", line 877, in check_array
    array = _asarray_with_order(array, order=order, dtype=dtype, xp=xp)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\_array_api.py", line 185, in _asarray_with_order
    array = numpy.asarray(array, order=order, dtype=dtype)
  File "C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\generic.py", line 2070, in __array__
    return np.asarray(self._values, dtype=dtype)
ValueError: could not convert string to float: 'S'
from sklearn.preprocessing import StandardScaler

X = strat_train_set.drop(['Survived'], axis=1)
Y = strat_train_set['Survived']
scaler = StandardScaler()
X_data = scaler.fit_transform(X)

= RESTART: C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py

Warning (from warnings module):
  File "C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/titanic_script_script.py", line 9
    sns.heatmap(titanic_data.corr(), cmap="YlGnBu")
FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.
<class 'pandas.core.frame.DataFrame'>
Int64Index: 712 entries, 395 to 330
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  712 non-null    int64  
 1   Survived     712 non-null    int64  
 2   Pclass       712 non-null    int64  
 3   Name         712 non-null    object 
 4   Sex          712 non-null    object 
 5   Age          563 non-null    float64
 6   SibSp        712 non-null    int64  
 7   Parch        712 non-null    int64  
 8   Ticket       712 non-null    object 
 9   Fare         712 non-null    float64
 10  Cabin        159 non-null    object 
 11  Embarked     710 non-null    object 
dtypes: float64(2), int64(5), object(5)
memory usage: 72.3+ KB
<class 'pandas.core.frame.DataFrame'>
Int64Index: 712 entries, 395 to 330
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  712 non-null    int64  
 1   Survived     712 non-null    int64  
 2   Pclass       712 non-null    int64  
 3   Age          712 non-null    float64
 4   SibSp        712 non-null    int64  
 5   Parch        712 non-null    int64  
 6   Fare         712 non-null    float64
 7   C            712 non-null    float64
 8   S            712 non-null    float64
 9   Q            712 non-null    float64
 10  Female       712 non-null    float64
 11  Male         712 non-null    float64
dtypes: float64(7), int64(5)
memory usage: 72.3 KB
>>> from sklearn.ensemble import RandomForestClassifier
>>> from sklearn.model_selection import GridSearch
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    from sklearn.model_selection import GridSearch
ImportError: cannot import name 'GridSearch' from 'sklearn.model_selection' (C:\Users\chris\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\model_selection\__init__.py)
>>> from sklearn.model_selection import GridSearchCV
>>> clf = RandomForestClassifier()
>>> param_grid = {}
>>> param_grid = [{}]
>>> param_grid = [{"n_estimators": [10, 100, 200, 500], "max_depth":[None, 5, 10], "min_samples_split": [2, 3, 4]}]
