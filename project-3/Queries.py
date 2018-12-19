#!/usr/bin/env python3
import psycopg2


def art_views():
    """Return the most popular three articles """
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""select articles.title, subq.views
              from ( select subq1.slug, count(*) as views from (
              select articles.slug, log.path from articles cross join log
              where log.path like ('%'|| articles.slug ||'%')) as subq1
              group by subq1.slug) as subq cross join articles where
              articles.slug = subq.slug order by subq.views desc limit 3;""")
    views = c.fetchall()
    db.close()
    print("The most popular three articles of all time are:")
    print('')
    for row in views:
        print(row[0])
        print(str(row[1]) + ' views')


art_views()
print('')


def aut_views():
    """ Return all the most popular article authors from the 'database' """
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""select authors.name, subq.views from (
              select subq1.slug, count(*) as views from ( select articles.slug,
              log.path from articles cross join log where log.path like
              ('%'|| articles.slug ||'%')) as subq1 group by subq1.slug) as
              subq cross join articles, authors where articles.author =
              authors.id and articles.slug = subq.slug
              order by subq.views desc;""")
    views = c.fetchall()
    db.close()
    print("The most popular article authors of all time are:")
    print('')
    for row in views:
        print(row[0])
        print(str(row[1]) + ' views')


aut_views()
print('')


def req_errorperc():
    """ Return days that lead more than 1% of errors """
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""select concat(date_part
             ('day', date(time)),'-',date_part('month', date(time)),'-',
             date_part('year', date(time)))as Date, percentage from
             ( select day, percentage from ( select qdayerr.day,
             qdayerr.errors * 100 / qdayall.views as percentage from
             ( select date_part('day', date(time)) as day, count(*) as errors
             from log where status != '200 OK' group by day order by day)
             as qdayerr join ( select date_part('day', date(time)) as day,
             count(*) as views from log group by day order by day) as qdayall
             on qdayerr.day = qdayall.day) as qr where percentage > 1) as qf
             join log on date_part('day', date(time)) = qf.day limit 1;""")
    views = c.fetchall()
    db.close()
    print("Day that lead Requests errors more than 1% is:")
    print('')
    for row in views:
        print(row[0])
        print(str(row[1]) + ' %')


req_errorperc()
print('')
