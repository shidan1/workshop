from slimit import minifier

text = """
function hello() {
alert("cruel world");
}
"""

print(minifier.minify(text))
