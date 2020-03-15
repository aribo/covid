#!python3
from selenium import webdriver
from time import sleep
import re
from datetime import datetime
import smtplib


class Coronavirus():
    def __init__(self):
        self.driver = webdriver.Chrome()
