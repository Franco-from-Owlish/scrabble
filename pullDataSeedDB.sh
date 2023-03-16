curl -X GET "http://www.mieliestronk.com/corncob_lowercase.txt" > "scripts/words.txt"
python3 scripts/create_seed_files.py "scripts/words.txt" "db_seeding/words.sql"
sqlite3 scrabble.db -init db_seeding/words.sql
rm scripts/words.txt