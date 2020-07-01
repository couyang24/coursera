# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Food Hunt in downtown Toronto

# ## Introduction/Business Problem 

# As the financial center Canada and one of the multiculutural metropolises, Toronto attracts immigration from all over the world and, therefore, its food culture is significantly influenced by the city's immigrant history, which turned the city into one of the most ideal places to seek for different type of delicious cuisines. 
#
#
# Here is some examples:
#
#
# Central and Eastern European -  bagels, cheesecake, hot dogs, knishes, and delicatessens (or delis)
#
# Italian - New York-style pizza and Italian cuisine
#
# Jewish - pastrami 
#
# Irish - corned beef
#
# Chinese - Hotpot, Dim Sum, Noodle, Fried Rice
#
# Japanese - Sushi
#
# Korea - Fried Chicken, BBQ
#
# This study is aiming to find out whether these different type of cuisines are clustered in different part of the city and found out highly rated resturants at different price level.
#

# ## Data Source

# Data used in the analysis are listed below:
#
# · List of postal codes of Canada: M -- Wikipedia[2].
#
# · Using Geopy to get geological location by address name
#
# · Using Foursquare API to get the most common venues of given Borough of Toronto.
#
# · Using Foursquare API to get the venues' record of given venues of Toronto


