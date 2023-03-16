import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_name", type=str,
                    help="Name of the file with the list of words")
parser.add_argument("out_file", type=str,
                    help="Output file")

SQL_FILE_TEMPLATE = f"DROP TABLE IF EXISTS 'words';\n" \
                    f"CREATE TABLE 'words' (\n" \
                    f"   word varchar(55),\n" \
                    f"   first_letter varchar(1),\n" \
                    f"   word_length INTEGER \n" \
                    f");\n" \
                    f"\n" \
                    f"BEGIN TRANSACTION;"


def main(in_file: str, out_file: str):
    with open(out_file, 'w') as o:
        with open(in_file, "r") as f:
            o.writelines(SQL_FILE_TEMPLATE)
            lines = f.readlines()
            for line in lines:
                word = line.strip().lower()
                o.writelines(f"INSERT INTO 'words' VALUES ('{word}','{word[0]}',{len(word)});\n")
        o.writelines("COMMIT;")


if __name__ == "__main__":
    args = parser.parse_args()
    file_name = args.file_name
    output_file = args.out_file
    main(in_file=file_name, out_file=output_file)
