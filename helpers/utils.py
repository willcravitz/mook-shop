import json

def parse_book_list(filename):
    """Parses a text file containing book entries into a list of dictionaries.

    Args:
        filename: The path to the text file.

    Returns:
        A list of dictionaries, where each dictionary represents a book with the following keys:
            - TB Number: The TB identification number (e.g., "TB 1").
            - Title: The title of the book.
            - Subtitle: The subtitle of the book (optional).
            - Authors: The author(s) of the book.
            - Additional information: Any additional information found in the entry (optional).
    """

    books_data = []
    with open(filename, "r") as infile:
        for line in infile:
            book_info = line.strip()
            if not book_info:
                continue
            num, rem = book_info.split(".", maxsplit=1)
            
            title_info = rem.split("-", maxsplit=1)
            title = title_info[0]
            if ":" in title:
                title, subtitle = title.split(":", maxsplit=1)
            else:
                subtitle = None
            rem = title_info[1] if len(title_info) > 1 else ""
            
            author_info = rem.split(".", maxsplit=1)
            authors = author_info[0].split("/")
            rem = author_info[1] if len(author_info) > 1 else ""
            
            # Create dictionary for the book and append to the list
            book_data = {
                "TB Number": num,
                "Title": title,
                "Subtitle": subtitle,
                "Authors": authors,
                "Other Information": rem,
            }
            books_data.append(book_data)

    return books_data

def output_to_json(data, filepath):
    json_data = json.dumps(data, indent=4)
    with open(filepath, "w") as outfile:
        outfile.write(json_data)

books = parse_book_list("src/fixtures/torchbooks.txt")
output_to_json(books, "src/fixtures/torchbooks.json")
    