import main
mutable = []
immutable = []
for name in dir(main):
    if not name.startswith('_'):
        var = getattr(main, name)
        # check if var is mutable or immutable and append to the right list
sorted_variables = {
    "mutable": mutable,
    "immutable": immutable
}
