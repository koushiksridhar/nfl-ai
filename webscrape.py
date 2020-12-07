"""Webscrape Pro Football Reference to create NFL Dataset for PPR"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import csv

from pandas import DataFrame

for x in range(2010, 2020):

    year = x
    url = 'https://www.pro-football-reference.com/years/' + str(year) + '/fantasy.htm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    parsed_table = soup.find_all('table')[0]

    df = []

    for i, row in enumerate(parsed_table.find_all('tr')[2:]):

        player = []

        try:
            ### PLAYER GENERICS ###
            name = row.find('td', attrs={'data-stat': 'player'}).a.get_text()
            team = row.find('td', attrs={'data-stat': 'team'}).a.get_text()
            pos = row.find('td', attrs={'data-stat': 'fantasy_pos'}).text.strip()
            age = row.find('td', attrs={'data-stat': 'age'}).text.strip()

            ### GAMES ###
            games = row.find('td', attrs={'data-stat': 'g'}).text.strip()
            g_start = row.find('td', attrs={'data-stat': 'gs'}).text.strip()

            ### PASSING ###
            pass_cmp = row.find('td', attrs={'data-stat': 'pass_cmp'}).text.strip()
            pass_att = row.find('td', attrs={'data-stat': 'pass_att'}).text.strip()
            pass_yds = row.find('td', attrs={'data-stat': 'pass_yds'}).text.strip()
            pass_td = row.find('td', attrs={'data-stat': 'pass_td'}).text.strip()
            pass_int = row.find('td', attrs={'data-stat': 'pass_int'}).text.strip()

            ### RUSH ###
            rush_att = row.find('td', attrs={'data-stat': 'rush_att'}).text.strip()
            rush_yds = row.find('td', attrs={'data-stat': 'rush_yds'}).text.strip()
            rush_yds_per_att = row.find('td', attrs={'data-stat': 'rush_yds_per_att'}).text.strip()
            rush_td = row.find('td', attrs={'data-stat': 'rush_td'}).text.strip()

            ### RECIEVING ###
            targets = row.find('td', attrs={'data-stat': 'targets'}).text.strip()
            rec = row.find('td', attrs={'data-stat': 'rec'}).text.strip()
            rec_yds = row.find('td', attrs={'data-stat': 'rec_yds'}).text.strip()
            rec_yds_per_rec = row.find('td', attrs={'data-stat': 'rec_yds_per_rec'}).text.strip()
            rec_td = row.find('td', attrs={'data-stat': 'rec_td'}).text.strip()

            ### FUMBLES ###
            fumbles = row.find('td', attrs={'data-stat': 'fumbles'}).text.strip()
            fumbles_lost = row.find('td', attrs={'data-stat': 'fumbles_lost'}).text.strip()

            ### SCORING ###
            all_td = row.find('td', attrs={'data-stat': 'all_td'}).text.strip()
            two_pt_md = row.find('td', attrs={'data-stat': 'two_pt_md'}).text.strip()
            two_pt_pass = row.find('td', attrs={'data-stat': 'two_pt_pass'}).text.strip()

            ### FANTASY ###
            fpts = row.find('td', attrs={'data-stat': 'fantasy_points'}).text.strip()
            fpts_ppr = row.find('td', attrs={'data-stat': 'fantasy_points_ppr'}).text.strip()
            dk_pts = row.find('td', attrs={'data-stat': 'draftkings_points'}).text.strip()
            fd_pts = row.find('td', attrs={'data-stat': 'fanduel_points'}).text.strip()
            vbd = row.find('td', attrs={'data-stat': 'vbd'}).text.strip()
            fantasy_rank_pos = row.find('td', attrs={'data-stat': 'fantasy_rank_pos'}).text.strip()
            fantasy_rank_overall = row.find('td', attrs={'data-stat': 'fantasy_rank_overall'}).text.strip()

            player = [name, team, pos, age, games, g_start, pass_cmp, pass_att, pass_yds, pass_td, pass_int,
                      rush_att, rush_yds, rush_yds_per_att, rush_td, targets, rec, rec_yds, rec_yds_per_rec, rec_td,
                      fumbles, fumbles_lost, all_td, two_pt_md, two_pt_pass, fpts, fpts_ppr, dk_pts, fd_pts, vbd,
                      fantasy_rank_pos, fantasy_rank_overall]

            df.append(player)

        except:
            i += 1
            pass

    player_data = DataFrame (df, columns=['player', 'team', 'pos', 'age', 'games', 'g_start', 'pass_cmp', 'pass_att',
                                         'pass_yds', 'pass_td', 'pass_int', 'rush_att', 'rush_yds', 'rush_yds_per_att',
                                         'rush_td', 'targets', 'rec', 'rec_yds', 'rec_yds_per_rec', 'rec_td', 'fumbles',
                                         'fumbles_lost', 'all_td', 'two_pt_md', 'two_pt_pass', 'fpts', 'fpts_ppr', 'dk_pts',
                                         'fd_pts', 'vbd', 'fantasy_rank_pos', 'fantasy_rank_overall'])

    player_data.to_csv('fantasy' + str(year) + '.csv')
