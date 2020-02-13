import subprocess
import sys
import os
import sqlite3

#TODO: change the function name
def Test():
    #TODO: Create a loop to read through the csv file
    subprocess.call("sqlite3", shell=True)
    subprocess.call(".open test1.db")
    subprocess.call("create table tbll(professor varchar(15), office varchar(15), title varchar(20)")
    subprocess.call(".quit")
    #TODO: Using subprocess to insert rolls with sqlite commands


if __name__=="__main__":
    #TODO: change the function name
    Test()

