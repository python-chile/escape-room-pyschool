# NOTES

This site was built with quarto and the pyodide extension.

There are several personalizations

## Theme

The theme is based on the sketchy theme.

## Pyodide

The pyodide extension is used to run python code in the browser.
All the verifications are done in python, on the file `verification.py`.
The pyodide loading extension was intervened to load the `verification.py` file,
around line 60 the following code was added:

```js
// Load the verification file
await mainPyodide.runPythonAsync(`
import urllib.request
url = "https://raw.githubusercontent.com/sebastiandres/pyscape/refs/heads/main/quarto/verification.py"
urllib.request.urlretrieve(url, "verification.py");
`);
qpyodideUpdateStatusHeader("Cargando las habitaciones...");
```

