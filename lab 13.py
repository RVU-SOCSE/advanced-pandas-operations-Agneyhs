Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Importing required libraries
>>> import pandas as pd
>>> # Creating the employee_details DataFrame
>>> employee_details = pd.DataFrame({
... 'EmployeeID': [101, 102, 103, 104, 105],
... 'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
... 'Department': ['HR', 'Engineering', 'Engineering', 'HR', 'Marketing']
... })
>>> # Creating the employee_salaries DataFrame
>>> employee_salaries = pd.DataFrame({
...   'EmployeeID': [101, 102, 103, 104, 105],
...   'Salary': [50000, 70000, 80000, 55000, 60000]
...   })
>>> # Creating the sales_region_1 DataFrame
>>> sales_region_1 = pd.DataFrame({
...     'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
...     'Region': ['North', 'North', 'North', 'North', 'North'],
...     'Sales': [250, 300, 200, 400, 350]
...     })
>>> # Creating the sales_region_2 DataFrame
>>> sales_region_2 = pd.DataFrame({
...     'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
...     'Region': ['South', 'South', 'South', 'South', 'South'],
...     'Sales': [300, 320, 280, 360, 310]
...     })
>>> # Display the datasets
>>> print("Employee Details:")
Employee Details:
>>> print(employee_details)
   EmployeeID     Name   Department
0         101    Alice           HR
1         102      Bob  Engineering
2         103  Charlie  Engineering
3         104    David           HR
4         105      Eva    Marketing
>>> print("\nEmployee Salaries:")

Employee Salaries:
print(employee_salaries)
   EmployeeID  Salary
0         101   50000
1         102   70000
2         103   80000
3         104   55000
4         105   60000
print("\nSales Region 1:")

Sales Region 1:
print(sales_region_1)
        Date Region  Sales
0 2024-01-01  North    250
1 2024-01-02  North    300
2 2024-01-03  North    200
3 2024-01-04  North    400
4 2024-01-05  North    350
print("\nSales Region 2:")

Sales Region 2:
print(sales_region_2)
        Date Region  Sales
0 2024-01-01  South    300
1 2024-01-02  South    320
2 2024-01-03  South    280
3 2024-01-04  South    360
4 2024-01-05  South    310
# Grouping by department and calculating average salary
avg_salary_per_dept = employee_details.merge(employee_salaries,
on='EmployeeID').groupby('Department')['Salary'].mean()
print("\nAverage Salary per Department:")

Average Salary per Department:
print(avg_salary_per_dept)
Department
Engineering    75000.0
HR             52500.0
Marketing      60000.0
Name: Salary, dtype: float64
# Merging two DataFrames on the EmployeeID column
merged_data = pd.merge(employee_details, employee_salaries, on='EmployeeID',
how='inner')
print("\nMerged Employee Data:")

Merged Employee Data:
print(merged_data)
   EmployeeID     Name   Department  Salary
0         101    Alice           HR   50000
1         102      Bob  Engineering   70000
2         103  Charlie  Engineering   80000
3         104    David           HR   55000
4         105      Eva    Marketing   60000
# Importing required libraries
import pandas as pd
# Creating the stock_prices DataFrame with 'Date' as the index
stock_prices = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
  'Price': [150, 155, 152, 158, 160]
    })
stock_prices.set_index('Date', inplace=True)
# Creating the market_volume DataFrame with 'Date' as the index
market_volume = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Volume': [1000, 1100, 1050, 1150, 1200]
    })
market_volume.set_index('Date', inplace=True)
# Display the datasets
print("Stock Prices Data:")
Stock Prices Data:
print(stock_prices)
            Price
Date             
2024-01-01    150
2024-01-02    155
2024-01-03    152
2024-01-04    158
2024-01-05    160
print("\nMarket Volume Data:")

Market Volume Data:
print(market_volume)
            Volume
Date              
2024-01-01    1000
2024-01-02    1100
2024-01-03    1050
2024-01-04    1150
2024-01-05    1200
# Performing the join operation
# Joining market_volume to stock_prices based on their index
joined_data = stock_prices.join(market_volume, how='inner')
print("\nJoined Stock Prices and Market Volume Data:")

Joined Stock Prices and Market Volume Data:
print(joined_data)
            Price  Volume
Date                     
2024-01-01    150    1000
2024-01-02    155    1100
2024-01-03    152    1050
2024-01-04    158    1150
2024-01-05    160    1200
# Concatenating DataFrames vertically
consolidated_sales = pd.concat([sales_region_1, sales_region_2], axis=0)
print("\nConsolidated Sales Data:")

Consolidated Sales Data:
print(consolidated_sales)
        Date Region  Sales
0 2024-01-01  North    250
1 2024-01-02  North    300
2 2024-01-03  North    200
3 2024-01-04  North    400
4 2024-01-05  North    350
0 2024-01-01  South    300
1 2024-01-02  South    320
2 2024-01-03  South    280
3 2024-01-04  South    360
4 2024-01-05  South    310

================================================= RESTART: C:/Users/RVUW243/Documents/agney.py/prog14.py advanced visualisation with seaborn.py ================================================
Traceback (most recent call last):
  File "C:/Users/RVUW243/Documents/agney.py/prog14.py advanced visualisation with seaborn.py", line 4, in <module>
    df = pd.read_csv(r"C:\Users\RVUW243\Desktop\14prog_5ds_salaries (1).xlsx")
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1922, in _make_engine
    return mapping[engine](f, **self.options)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\c_parser_wrapper.py", line 95, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas/_libs/parsers.pyx", line 568, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas/_libs/parsers.pyx", line 657, in pandas._libs.parsers.TextReader._get_header
  File "pandas/_libs/parsers.pyx", line 868, in pandas._libs.parsers.TextReader._tokenize_rows
  File "pandas/_libs/parsers.pyx", line 885, in pandas._libs.parsers.TextReader._check_tokenize_status
  File "pandas/_libs/parsers.pyx", line 2076, in pandas._libs.parsers.raise_parser_error
  File "<frozen codecs>", line 325, in decode
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xac in position 11: invalid start byte

= RESTART: C:/Users/RVUW243/Documents/agney.py/prog14.py advanced visualisation with seaborn.py
Traceback (most recent call last):
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\compat\_optional.py", line 158, in import_optional_dependency
    module = importlib.import_module(name)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1324, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'fsspec'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:/Users/RVUW243/Documents/agney.py/prog14.py advanced visualisation with seaborn.py", line 4, in <module>
    df = pd.read_csv(r"C://Users//RVUW243//Desktop//14prog_5ds_salaries (1).xlsx")
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\common.py", line 772, in get_handle
    ioargs = _get_filepath_or_buffer(
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\common.py", line 429, in _get_filepath_or_buffer
    fsspec = import_optional_dependency("fsspec")
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\compat\_optional.py", line 161, in import_optional_dependency
    raise ImportError(msg) from err
ImportError: `Import fsspec` failed.  Use pip or conda to install the fsspec package.

= RESTART: C:/Users/RVUW243/Documents/agney.py/prog14.py advanced visualisation with seaborn.py

= RESTART: C:/Users/RVUW243/Documents/agney.py/prog 14 advanced visualization with seaborn.py(b).py
Traceback (most recent call last):
  File "C:/Users/RVUW243/Documents/agney.py/prog 14 advanced visualization with seaborn.py(b).py", line 4, in <module>
    df2 = pd.read_csv(r"C:\Users\RVUW243\Desktop\14prog_5ds_salaries (1).xlsx")
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1922, in _make_engine
    return mapping[engine](f, **self.options)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\c_parser_wrapper.py", line 95, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas/_libs/parsers.pyx", line 568, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas/_libs/parsers.pyx", line 657, in pandas._libs.parsers.TextReader._get_header
  File "pandas/_libs/parsers.pyx", line 868, in pandas._libs.parsers.TextReader._tokenize_rows
  File "pandas/_libs/parsers.pyx", line 885, in pandas._libs.parsers.TextReader._check_tokenize_status
  File "pandas/_libs/parsers.pyx", line 2076, in pandas._libs.parsers.raise_parser_error
  File "<frozen codecs>", line 325, in decode
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xac in position 11: invalid start byte

= RESTART: C:/Users/RVUW243/Documents/agney.py/prog 14 advanced visualization with seaborn.py(b).py
Traceback (most recent call last):
  File "C:/Users/RVUW243/Documents/agney.py/prog 14 advanced visualization with seaborn.py(b).py", line 6, in <module>
    df2 = pd.read_csv(r"C:/Users/RVUW243/Desktop/14prog_5ds_salaries (1).xlsx")
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1922, in _make_engine
    return mapping[engine](f, **self.options)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\c_parser_wrapper.py", line 95, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas/_libs/parsers.pyx", line 568, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas/_libs/parsers.pyx", line 657, in pandas._libs.parsers.TextReader._get_header
  File "pandas/_libs/parsers.pyx", line 868, in pandas._libs.parsers.TextReader._tokenize_rows
  File "pandas/_libs/parsers.pyx", line 885, in pandas._libs.parsers.TextReader._check_tokenize_status
  File "pandas/_libs/parsers.pyx", line 2076, in pandas._libs.parsers.raise_parser_error
  File "<frozen codecs>", line 325, in decode
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xac in position 11: invalid start byte

=========== RESTART: C:/Users/RVUW243/Documents/agney.py/lab 16(a).py ==========
Traceback (most recent call last):
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'YearsExperience'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:/Users/RVUW243/Documents/agney.py/lab 16(a).py", line 5, in <module>
    plt.plot(df['YearsExperience'],df['Salary'])
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'YearsExperience'

=========== RESTART: C:/Users/RVUW243/Documents/agney.py/lab 16(b).py ==========
Traceback (most recent call last):
  File "C:/Users/RVUW243/Documents/agney.py/lab 16(b).py", line 4, in <module>
    df = pd.read_csv(r"C:\Users\RVUW243\Desktop\14prog_5ds_salaries (1).xlsx")
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1922, in _make_engine
    return mapping[engine](f, **self.options)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\c_parser_wrapper.py", line 95, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas/_libs/parsers.pyx", line 568, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas/_libs/parsers.pyx", line 657, in pandas._libs.parsers.TextReader._get_header
  File "pandas/_libs/parsers.pyx", line 868, in pandas._libs.parsers.TextReader._tokenize_rows
  File "pandas/_libs/parsers.pyx", line 885, in pandas._libs.parsers.TextReader._check_tokenize_status
  File "pandas/_libs/parsers.pyx", line 2076, in pandas._libs.parsers.raise_parser_error
  File "<frozen codecs>", line 325, in decode
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xac in position 11: invalid start byte

=========== RESTART: C:/Users/RVUW243/Documents/agney.py/lab 16(b).py ==========
Traceback (most recent call last):
  File "C:/Users/RVUW243/Documents/agney.py/lab 16(b).py", line 4, in <module>
    df = pd.read_csv(r"14prog_5ds_salaries (1).xlsx")
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\common.py", line 926, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: '14prog_5ds_salaries (1).xlsx'

= RESTART: C:/Users/RVUW243/Documents/agney.py/prog 14 advanced visualization with seaborn.py(b).py
Traceback (most recent call last):
  File "C:/Users/RVUW243/Documents/agney.py/prog 14 advanced visualization with seaborn.py(b).py", line 6, in <module>
    df2 = pd.read_csv(r"C:/Users/RVUW243/Desktop/14prog_5ds_salaries (1).csv")
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\common.py", line 926, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'C:/Users/RVUW243/Desktop/14prog_5ds_salaries (1).csv'

= RESTART: C:/Users/RVUW243/Documents/agney.py/prog 14 advanced visualization with seaborn.py(b).py
Traceback (most recent call last):
  File "C:/Users/RVUW243/Documents/agney.py/prog 14 advanced visualization with seaborn.py(b).py", line 6, in <module>
    df2 = pd.read_csv(r"C:/Users/RVUW243/Desktop/14prog_5ds_salaries (1).csv")
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\common.py", line 926, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'C:/Users/RVUW243/Desktop/14prog_5ds_salaries (1).csv'

============ RESTART: C:/Users/RVUW243/Documents/agney.py/lab 15.py ============

============ RESTART: C:/Users/RVUW243/Documents/agney.py/lab 15.py ============

= RESTART: C:/Users/RVUW243/Documents/agney.py/prog14.py advanced visualisation with seaborn.py

=========== RESTART: C:/Users/RVUW243/Documents/agney.py/lab 16(a).py ==========
Traceback (most recent call last):
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'YearsExperience'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:/Users/RVUW243/Documents/agney.py/lab 16(a).py", line 5, in <module>
    plt.plot(df['YearsExperience'],df['Salary'])
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'YearsExperience'

=========== RESTART: C:/Users/RVUW243/Documents/agney.py/lab 16(b).py ==========
Traceback (most recent call last):
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'YearsExperience'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:/Users/RVUW243/Documents/agney.py/lab 16(b).py", line 5, in <module>
    plt.scatter(df['YearsExperience'], df['Salary'])
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\RVUW243\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'YearsExperience'
