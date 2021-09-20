import sqlite3
import pandas as pd
import jellyfish

try:
    sqliteConnection = sqlite3.connect('DEI Database with Sierra.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")
    
    sql_query = """SELECT *
                FROM title_list
                WHERE AUTHOR LIKE "%Kendra Allen%"
                """
    cursor.execute(sql_query)
    sqliteConnection.commit()
    dei_rows = cursor.fetchall()
    cursor.close()
except sqlite3.Error as error:
    print("Failed to run query", error)
    
column_names = ["Genre","Author","Title","Year"]
dei_df = pd.DataFrame(dei_rows, columns=column_names)  
print(dei_df) 

try:
    sqliteConnection = sqlite3.connect('DEI Database with Sierra.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")
    
    sql_query = """SELECT *
                FROM holdings
                WHERE AUTHOR LIKE "%Kendra Allen%"
                """
    cursor.execute(sql_query)
    sqliteConnection.commit()
    holdings_rows = cursor.fetchall()
    cursor.close()
except sqlite3.Error as error:
    print("Failed to run query", error)
    
column_names = ["Title","Author","Location"]
holdings_df = pd.DataFrame(holdings_rows, columns=column_names)  
print(holdings_df) 

print("levenshtein_distance")
print(dei_df['Title'].values[1])
print(holdings_df['Title'].values[1])
print(jellyfish.levenshtein_distance(dei_df['Title'].values[1], holdings_df['Title'].values[1]))
print(dei_df['Title'].values[0])
print(holdings_df['Title'].values[0])
print(jellyfish.levenshtein_distance(dei_df['Title'].values[0], holdings_df['Title'].values[0]))

print("damerau_levenshtein_distance")
print(dei_df['Title'].values[1])
print(holdings_df['Title'].values[1])
print(jellyfish.damerau_levenshtein_distance(dei_df['Title'].values[1], holdings_df['Title'].values[1]))
print(dei_df['Title'].values[0])
print(holdings_df['Title'].values[0])
print(jellyfish.damerau_levenshtein_distance(dei_df['Title'].values[0], holdings_df['Title'].values[0]))

print("jaro_winkler_similarity")
print(dei_df['Title'].values[1])
print(holdings_df['Title'].values[1])
print(jellyfish.jaro_winkler_similarity(dei_df['Title'].values[1], holdings_df['Title'].values[1]))
print(dei_df['Title'].values[0])
print(holdings_df['Title'].values[0])
print(jellyfish.jaro_winkler_similarity(dei_df['Title'].values[0], holdings_df['Title'].values[0]))

print("match_rating_comparison")
print(dei_df['Title'].values[1])
print(holdings_df['Title'].values[1])
print(jellyfish.match_rating_comparison(dei_df['Title'].values[1], holdings_df['Title'].values[1]))
print(dei_df['Title'].values[0])
print(holdings_df['Title'].values[0])
print(jellyfish.match_rating_comparison(dei_df['Title'].values[0], holdings_df['Title'].values[0]))

dei_df.rename(columns={"Title": "Title_Sierra"})
matched = pd.merge(holdings_df,dei_df, on='Author')
matched['match'] = jellyfish.match_rating_comparison(matched['Title'].values, matched['Title_Sierra'].values)
print(matched)
