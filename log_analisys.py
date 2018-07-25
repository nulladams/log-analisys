#! /usr/bin/python3

import psycopg2

# Open file to safe results from queries
file = open("results.txt", "w")

# Open connection with database
conn = psycopg2.connect(dbname="news")
cursor = conn.cursor()

file.write("\n\nLOG ANALISYS PROJECT")

file.write("\n\n---------------------------------"
           "-------------------------")

# 1st query - 3 most popular articles
file.write("\n1st QUERY - 3 most popular articles\n")
cursor.execute("select articles.title, logs.num_views "
               "from articles, "
               "(select log.path, "
               "split_part(log.path, '/article/', 2) as slug, "
               "count(*) as num_views "
               "from log, articles "
               "where log.status = '200 OK' "
               "and log.path like '/article/%' "
               "group by log.path) as logs "
               "where articles.slug = logs.slug "
               "order by num_views desc limit 3;")

# Recover, format and safe results from query 1 to file
results1 = cursor.fetchall()
for register in results1:
    title = "\"" + register[0] + "\""
    num_views = register[1]

    # Format output
    register_output = ('{title:<40} - {num_views!s:>10} views'
                       .format(title=title, num_views=num_views))
    print(register_output)

    # Safe output to file
    file.write("\n" + register_output)

file.write("\n---------------------------------------"
           "-------------------\n\n")

file.write("\n---------------------------------------"
           "-------------------")

# 2nd query - Authors of the most popular articles
file.write("\n2nd QUERY - Authors of the most popular articles\n")
cursor.execute("select authors.name, count(*) as num_views "
               "from authors, articles, "
               "(select log.path, "
               "split_part(log.path, '/article/', 2) as slug, "
               "log.time from log where log.status = '200 OK' "
               "and log.path like '/article/%') as logs "
               "where articles.slug = logs.slug "
               "and articles.author = authors.id "
               "group by authors.name "
               "order by num_views desc;")

# Recover, format and safe results from query 2 to file
results2 = cursor.fetchall()
for register in results2:
    author = register[0]
    num_views = register[1]

    # Format output
    register_output = ('{author:<40} - {num_views!s:>10} views'
                       .format(author=author, num_views=num_views))
    print(register_output)

    # Safe output to file
    file.write("\n" + register_output)

file.write("\n---------------------------------------"
           "-------------------\n\n")

file.write("\n---------------------------------------"
           "-------------------")

# 3rd - Days where errors from requests are more the 1%
file.write("\n3rd QUERY - Days where errors from requests are more the 1%\n")
cursor.execute("select errors.date, errors.num_errors, "
               "request_day.num_requests, request_day.date "
               "from (select count(*) as num_errors, time::date as date "
               "from log where status = '404 NOT FOUND' "
               "group by date) as errors, "
               "(select count(*) as num_requests, time::date as date "
               "from log group by date) as request_day "
               "where errors.date = request_day.date "
               "group by (errors.date, errors.num_errors, "
               "request_day.num_requests, request_day.date) "
               "having errors.num_errors > request_day.num_requests*0.01;")

# Recover, format and safe results from query 3 to file
results3 = cursor.fetchall()
for register in results3:
    register_date = register[0].strftime("%b %d, %Y")
    num_errors = register[1]
    num_requests = register[2]

    # Percentage of errors in the date
    errors_percentage = (num_errors/num_requests)*100

    # Format output
    register_output = ('{register_date} - {errors_percentage:02.2f}%'
                       .format(register_date=register_date,
                               errors_percentage=errors_percentage))
    print(register_output)

    # Safe output to file
    file.write("\n" + str(register_output))

file.write("\n---------------------------------------"
           "-------------------")

# Close connection with database
conn.close()

# Close and safe file with qyeries results
file.close()
