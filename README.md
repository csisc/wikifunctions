# wikifunctions
A Jupyter Notebook to load and reuse Wikifunctions implementations

## Description
The Jupyter Notebook provided is designed to interact with the Wikifunctions API to retrieve and execute a specific function, and then extract detailed metadata about that function, including its implementation, description, argument types, and argument names.

## Dependencies
* Requests
* JSON

## Details
* The Function class is initialized with an implementation ID (zid).
* The get_func method retrieves the implementation code of the function.
* The get_desc method retrieves the function's description, names, argument types, and argument descriptions.
* names["Z1002"] returns the function name in English.
* descriptions["Z1002"] returns the function description in English.
* types["<func_id>K1"] returns the type of the first argument.
* vars["<func_id>K1", "Z1002"] returns the name of the first argument in English.
