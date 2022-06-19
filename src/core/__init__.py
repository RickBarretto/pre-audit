"""Core is the business logic

src.core has Models and Functions
that are used by `src.commands`

## Modules

### `src.core.fetch_api`
Module Abstraction to fetch the OsvApi
and returns a `json: dict`

### `src.core.filter_report`
Module that filter the reports getted from api

### `src.core.utils.exceptions`
Module that have exceptions types

### `src.core.utils.flatten_list`
Module that have the function to flat a list,
used by `src.core.filter_report`

### `src.core.utils.get_all_affected_versions_functions`
Module that have the function to get a list of affected versions,
used by `src.core.filter_report`

### `src.core.utils.requesting`
Deals with Api directly
Low level for `src.core.fetch_api`

"""
