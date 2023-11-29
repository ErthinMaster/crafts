from utils import read_json, write_txt

def get_item(name, data, header, header_type):
    if header_type == "key": return name        
    if header not in data.keys(): return ""
    if header_type == "link": return f"[[{data[header]}]]"
    if header_type == "text": return data[header]
    if header_type == "dict": return "\n" + "\n".join(f"*{k} : ({v})" for k,v in data[header])

def get_line(name, data, headers):
    return " || ".join(get_item(name, data, header, header_type) for header, header_type in headers.items())

def generate_table_text(data, headers, title):
    table_text =  '{| class="darkTable" \n|+ ' + title + "\n"
    table_text += '!' + "!!".join(header.title() for header in headers.keys())+ '\n|-'
    table_text += '\n|-'.join(get_line(k, d, headers) for k, d in data.items())
    table_text += '|}'
    return table_text

if __name__ == '__main__':
    potions = read_json("./potions.json")
    headers = {
        "nom" : "key",
        "auteur" : "link",
        "niveau" : "text",
        "ingrédients" : "dict",
        "descriptions" : "text"
    }
    table_text = generate_table_text(potions, headers, "Liste des potions d'Alchimiste")
    write_txt(table_text, "potions_wiki_table.txt")
