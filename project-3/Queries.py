#!/usr/bin/env python3
import psycopg2


query1 = """select articles.title, subq.views
              from ( select subq1.slug, count(*) as views from (
              select articles.slug, log.path from articles cross join log
              where log.path like ('%'|| articles.slug ||'%')
              and status = '200 OK') as subq1 group by subq1.slug) as subq
              cross join articles where articles.slug = subq.slug
              order by subq.views desc limit 3;"""

query2 = """select authors.name,  sum(subq.views) as view from (
              select subq1.slug, count(*) as views from ( select articles.slug,
              log.path from articles cross join log where log.path like
              ('%'|| articles.slug ||'%') and status = '200 OK') as subq1 group
              by subq1.slug) as subq cross join articles, authors where
              articles.author = authors.id and articles.slug = subq.slug
              group by authors.id order by view desc;"""

query3 = """select concat(date_part
             ('day', date(time)),'-',date_part('month', date(time)),'-',
             date_part('year', date(time)))as Date, percentage from
             ( select day, percentage from ( select qdayerr.day,
             qdayerr.errors * 100 / qdayall.views as percentage from
             ( select date_part('day', date(time)) as day, count(*) as errors
             from log where status != '200 OK' group by day order by day)
             as qdayerr join ( select date_part('day', date(time)) as day,
             count(*) as views from log group by day order by day) as qdayall
             on qdayerr.day = qdayall.day) as qr where percentage > 1) as qf
             join log on date_part('day', date(time)) = qf.day limit 1;"""


def execute_query(query):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    views = c.fetchall()
    db.close()
    if query == query3:
        for row in views:
            print(row[0] + ': ' + str(row[1]) + ' %')
    else:
        for row in views:
            print(row[0] + ': ' + str(row[1]) + ' views')


print("The most popular three articles of all time are:")
print('')
execute_query(query1)
print('')
print("The most popular article authors of all time are:")
print('')
execute_query(query2)
print('')
print("Day that lead Requests errors more than 1% is:")
print('')
execute_query(query3)
