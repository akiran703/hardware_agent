import glob
import pandas as pd
import csv
import os
import glob

class DATA:
    def create_sql_table():
        path = '/Users/kirakumar/Desktop/codedegen/hardware_debug'


        files = glob.glob(path +'/*.csv')



        content = []

        for file in files:
            df = pd.read_csv(file)
            content.append(df)

        hardware_data_frame = pd.concat(content)



        from sqlalchemy import create_engine, MetaData, Table
        engine = create_engine("sqlite:///database.sqlite")
        # Create a metadata object
        metadata = MetaData()

        # Reflect the database schema
        metadata.reflect(bind=engine)

        # Store in the qualifying table
        hardware_data_frame.to_sql("hardware_issues", engine, if_exists="append")

        hardware_issues_Table = Table("hardware_issues", metadata, autoload_with=engine)
        
        return hardware_issues_Table

  







