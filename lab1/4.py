names = ["Ana", "Petar", "Ana", "Lucija", "Vanja", "Pavao", "Lucija"]

def reverse_sort(names: list) -> list:
    return sorted(names, reverse=True)

names_desc = reverse_sort(names)
selected_names = names_desc[1:-1]
unique_selected_names = set(selected_names)

pass_names = [f"{i}-pass" for i in unique_selected_names]
