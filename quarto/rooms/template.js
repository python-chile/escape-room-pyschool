<script>
// Load the answers
mainPyodide.runPythonAsync(`
    import urllib.request
    url = "https://raw.githubusercontent.com/sebastiandres/pyscape/refs/heads/main/quarto/rooms/template.py"
    urllib.request.urlretrieve(url, "sala.py");
    `);
console.log("Completed loading the answers");
</script>