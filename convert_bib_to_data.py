from pybtex.database import parse_file

path_bib = ["bib/pubs.bib", "bib/unpubs.bib"]
path_out = "_data/paper.yml"

out_data = []
for file in path_bib:
    bib_data = parse_file(file)
    for entry_name in bib_data.entries:
        entry = bib_data.entries[entry_name]

        entry_data = "\n{}:\n".format(entry_name.lower())
        entry_data += '  title: "{}"\n'.format(entry.fields['title'])

        list_authors = entry.persons['author']
        if len(list_authors) < 3:
            list_author_lastnames = []
            for person in list_authors:
                list_author_lastnames.append(" ".join(person.last_names))
            entry_data+= '  author: "{}"\n'.format(" and ".join(list_author_lastnames))
        else:
            first_author_lastnames = list_authors[0].last_names
            entry_data+= '  author: "{} et al."\n'.format(" ".join(first_author_lastnames))

        if "booktitle" in entry.fields:
            entry_data += '  book: "{}"\n'.format(entry.fields['booktitle'].replace("Proc.","").strip())
        elif "journal" in entry.fields:
            entry_data += '  book: "{}"\n'.format(entry.fields['journal'].replace("Proc.","").strip())
        else:
            print("no book or journal info in the entry:")
            print(entry.fields)
        entry_data += '  year: "{}"\n'.format(entry.fields['year'])
        entry_data += '  url: "{}"\n'.format(entry.fields['url'])
        out_data.append(entry_data)

with open(path_out, "w") as file:
    file.write("".join(out_data))