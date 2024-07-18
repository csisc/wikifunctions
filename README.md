# wikifunctions
A Jupyter Notebook to load and reuse Wikifunctions implementations

## Description
The Jupyter Notebook provided is designed to interact with the Wikifunctions API to retrieve and execute a specific function, and then extract detailed metadata about that function, including its implementation, description, argument types, and argument names.

## Dependencies
* [Requests](https://pypi.org/project/requests/)
* [JSON](https://docs.python.org/3/library/json.html)

## Details
* The Function class is initialized with an implementation ID (<code>zid</code>).
* The <code>get_func</code> method retrieves the implementation code of the function.
* The <code>get_desc</code> method retrieves the function's description, names, argument types, and argument descriptions.
* <code>names["Z1002"]</code> returns the function name in English.
* <code>descriptions["Z1002"]</code> returns the function description in English.
* <code>types["<func_id>K1"]</code> returns the type of the first argument where <code><func_id></code> is the function metadata id corresponding to <code>zid</code> implementation.
* <code>vars["<func_id>K1", "Z1002"]</code> returns the name of the first argument in English where <code><func_id></code> is the function metadata id corresponding to <code>zid</code> implementation.
