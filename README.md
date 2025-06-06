# xianxia-quotes

> Generate immersive xianxia‑style proverbs for any Python project or CLI usage.

**xianxia-quotes** provides a simple API and command‑line interface to produce memorable ‘‘Even a dragon will…’’‑style aphorisms.

---

## Features

* 🐉 **Single‑Quote CLI**: Run `xianxia-quotes` (or `python -m xianxia_quotes`) to print a random proverb.
* 📜 **Infinite Generator**: Import `quote_stream()` for an endless stream of proverbs.
* 🎯 **Simple API**: Call `single_quote()` to retrieve one aphorism as a string.
* ⚙️ **PEP 8‑Compliant**: Well‑structured code with documentation.

---

## Installation

```bash
pip install xianxia-quotes
```

Or from source:

```bash
git clone https://github.com/yourusername/xianxia-quotes.git
cd xianxia-quotes
pip install .
```

---

## Quickstart

### CLI usage

```bash
$ xianxia-quotes
“Even a phoenix will cower before a wolf in the forest”
```

### As a module

```python
from xianxia_quotes import single_quote, quote_stream

print(single_quote())  # one proverb

# infinite stream example
quotes = quote_stream()
for _ in range(5):
    print(next(quotes))
```

---

## API Reference

```python
single_quote() -> str
    Return a single xianxia‑style proverb.

quote_stream() -> Iterator[str]
    Infinite generator yielding proverbs.
```

---

## Development

1. Clone the repo and install dev dependencies:

   ```bash
   ```

git clone [https://github.com/yourusername/xianxia-quotes.git](https://github.com/yourusername/xianxia-quotes.git) cd xianxia-quotes pip install -e .$dev$

````
2. Run tests (if any):
   ```bash
pytest
````

3. Build and publish:

   ```bash
   ```

pip install build twine python -m build twine upload dist/\*

```

---

## License

This project is licensed under the [GNU GPL v3 (or later)](https://www.gnu.org/licenses/gpl-3.0.html).

```
