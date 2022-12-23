# KNMI website parser

Small parser-script for KNMI website. Returns average temperature for every day of the year.
Example output:

```text
2022-01-01       12.3
2022-01-02       11.7
2022-01-03       9.7
...
2022-12-29       8.1
2022-12-30       8.1
2022-12-31       8.0
```

Values are tab-separated.

# Usage

To use the script run it with Python 3:

```commandline
python3 knmi_parser.py place year
```

Where

* `place` is the name of weather station (i.e. `"de-bilt"`). Don't forget quotes for hyphenated values.
* `year` is the desired year as `yyyy` (i.e. `2020`)

## Available stations
as of 2022-12-23:
* `arcen`
* `berkhout`
* `cabauw`
* `de-bilt`
* `de-kooy`
* `deelen`
* `eelde`
* `eindhoven`
* `ell`
* `gilze-rijen`
* `heino`
* `herwijnen`
* `hoek-van-holland`
* `hoogeveen`
* `hoorn-(terschelling)`
* `hupsel`
* `lauwersoog`
* `leeuwarden`
* `lelystad`
* `maastricht`
* `marknesse`
* `nieuw-beerta`
* `rotterdam`
* `schiphol`
* `soesterberg`
* `stavoren`
* `twente`
* `valkenburg`
* `vlieland`
* `vlissingen`
* `volkel`
* `voorschoten`
* `westdorpe`
* `wijk-aan-zee`
* `wilhelminadorp`
* `woensdrecht`





















































