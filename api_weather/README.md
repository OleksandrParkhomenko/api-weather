## To generate random data use:

```python manage.py generate_data [--n <number of records>]```

### It saves number of records with such fields to DB:
- datetime - DateTimeField
- temperature - FloatField (max_value = 0.0, min_value =40.0)

### Return average temperature for requested periods from begin to end date

```/api/average/?begin=<date of begin>&end=<date of end>&step=<step>```

### Return temperature points from begin to end date

```/api/temperature/?begin=<date of begin>&end=<date of end>```

