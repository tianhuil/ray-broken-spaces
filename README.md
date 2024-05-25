# Ray Broken Spaces

Examples of broken spaces in Ray.


# Running code

They all pass testing:
```bash
PYTHONPATH=.:$PYTHONPATH poetry run python src/check_env.py
```

Then run
```bash
PYTHONPATH=.:$PYTHONPATH poetry run python src/chase_working.py # works
PYTHONPATH=.:$PYTHONPATH poetry run python src/chase_sequence.py # does not work with Repeated -> Sequence
```
