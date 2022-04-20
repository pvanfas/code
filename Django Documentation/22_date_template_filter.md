#### Date Template Filter

List of the most used Django date template filters to format date according to a given format, semantically ordered.

Usage `{{ date|date:"j" }}`

| Code | Description                                                | Output                   |
| ---- | ---------------------------------------------------------- | ------------------------ |
| d    | Day of the month, 2 digits with leading zeros              | `01` to `31`             |
| j    | Day of the month without leading zeros.                    | `1` to `31`              |
| S    | English ordinal suffix for day of the month, 2 characters. | `st`, `nd`, `rd` or `th` |
| m    | Month, 2 digits with leading zeros.                        | `01` to `12`             |
| n    | Month without leading zeros.                               | `1` to `12`              |
| b    | Month, textual, 3 letters, lowercase.                      | `jan`                    |
| M    | Month, textual, 3 letters.                                 | `Jan`                    |
| F    | Month, textual, long.                                      | `January`                |
| y    | Year, 2 digits.                                            | `20`                     |
| Y    | Year, 4 digits.                                            | `2020`                   |
| D    | Day of the week, textual, 3 letters.                       | `Fri`                    |
| l    | Day of the week, textual, long.                            | `Friday`                 |
| G    | Hour, 24-hour format without leading zeros.                | `0` to `23`              |
| H    | Hour, 24-hour format.                                      | `00` to `23`             |
| g    | Hour, 12-hour format without leading zeros.                | `1` to `12`              |
| h    | Hour, 12-hour format.                                      | `01` to `12`             |
| a    | a.m. or p.m.                                               | `a.m`                    |
| A    | AM or PM.                                                  | `AM`                     |
| i    | Minutes.                                                   | `00` to `59`             |
| s    | Seconds, 2 digits with leading zeros.                      | `0` to `59`              |
