import sqlite3
import os
import sys


class Image(object):

    def __init__(self):
        self.image_name = []
        self.unrecognized_img_name = []
        self.recognized_img_text = []

    def load_unrecognized_dir(self, path='D:\All Laptop Data\CyberTrone\Resources\detect_Personel'):
        """
        param path: Provide Path of File Directory
        :return: List of image Names
                """
        for y in os.listdir(path):
            self.unrecognized_img_name.append(y)

        return self.unrecognized_img_name

    def load_text_dir(self, path='D:\All Laptop Data\CyberTrone\Resources\detected_text_records\detected_images_text'):
        """
        param path: Provide Path of File Directory
        :return: List of image Names
                """
        for y in os.listdir(path):
            self.recognized_img_text.append(y)

        return self.recognized_img_text

    def connect_text_db(self, Text, Image):

        conn = sqlite3.connect("D:\All Laptop Data\CyberTrone\Resources\Database_file\Cybertrone.db")
        cursor = conn.cursor()

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS Text_detected
                (Text TEXT,Image BLOB)
                """)

        cursor.execute(""" INSERT INTO Text_detected 
                (Text, Image) VALUES (?,?)""", (Text, Image))


        conn.commit()
        cursor.close()
        conn.close()



    def connect_db(self, Name, Images, Text, Image):

        conn = sqlite3.connect("D:\All Laptop Data\CyberTrone\Resources\Database_file\Cybertrone.db")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Unrecognize_persons
        (Name TEXT,Images BLOB)
        """)

        cursor.execute(""" INSERT INTO Unrecognize_persons 
        (Name, Images) VALUES (?,?)""", (Name, Images))

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS Text_detected
                (Text TEXT,Image BLOB)
                """)

        cursor.execute(""" INSERT INTO Text_detected 
                (Text, Images) VALUES (?,?)""", (Text, Image))


        conn.commit()
        cursor.close()
        conn.close()

    def load_directory(self, path='D:\All Laptop Data\CyberTrone\Resources\Recognized_Personel'):
        """
        :param path: Provide Path of File Directory
        :return: List of image Names
        """
        for x in os.listdir(path):
            self.image_name.append(x)

        return self.image_name

    def create_database(self, Name, Images):
        """
        :param name: String
        :param image:  BLOB Data
        :return: None
        """

        conn = sqlite3.connect("D:\All Laptop Data\CyberTrone\Resources\Database_file\Cybertrone.db")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Recognize_persons
        (Name TEXT,Images BLOB)
        """)

        cursor.execute(""" INSERT INTO Recognize_persons 
        (Name, Images) VALUES (?,?)""", (Name, Images))

        conn.commit()
        cursor.close()
        conn.close()


def save_recognized_text():
    obj = Image()
    os.chdir("D:\All Laptop Data\CyberTrone\Resources\detected_text_records\detected_images_text")
    for y in obj.load_text_dir():
        if ".png" in y:
            with open(y, "rb") as f:
                saving_text = f.read()
                obj.connect_text_db(Text=y, Image=saving_text)
                print("{} Added to database ".format(y))

        elif ".jpg" in y:
            with open(y, "rb") as f:
                saving_text = f.read()
                obj.connect_text_db(Text=y, Image=saving_text)
                print("{} added to Database".format(y))


def fetch_recognized_text():
    counter = 1
    os.chdir("D:\All Laptop Data\CyberTrone\Resources\detected_text_records\Retrieved_text_data")
    conn = sqlite3.connect("D:\All Laptop Data\CyberTrone\Resources\Database_file\Cybertrone.db")
    cursor = conn.cursor()

    data = cursor.execute("""SELECT * FROM Text_detected""")
    for x in data.fetchall():
        print(x[1])
        with open("{}.png".format(counter), "wb") as f:
            f.write(x[1])
            counter = counter + 1

    conn.commit()
    cursor.close()
    conn.close()


def save_unrecognized_data():
    obj = Image()
    os.chdir("D:\All Laptop Data\CyberTrone\Resources\detect_Personel")
    for y in obj.load_unrecognized_dir():
        if ".png" in y:
            with open(y, "rb") as f:
                saving_data = f.read()
                obj.connect_db(Name=y, Images=saving_data)
                print("{} Added to database ".format(y))

        elif ".jpg" in y:
            with open(y, "rb") as f:
                saving_data = f.read()
                obj.connect_db(Name=y, Images=saving_data)
                print("{} added to Database".format(y))

def fetch_unrecognized_data():
    counter = 1
    os.chdir("D:\All Laptop Data\CyberTrone\Resources\Retrieved_detect_personel_data")
    conn = sqlite3.connect("D:\All Laptop Data\CyberTrone\Resources\Database_file\Cybertrone.db")
    cursor = conn.cursor()

    data = cursor.execute("""SELECT * FROM Unrecognize_persons""")
    for x in data.fetchall():
        print(x[1])
        with open("{}.png".format(counter), "wb") as f:
            f.write(x[1])
            counter = counter + 1

    conn.commit()
    cursor.close()
    conn.close()


def fetch_unrecognized_data():
    counter = 1
    os.chdir("D:\All Laptop Data\CyberTrone\Resources\Retrieved_detect_personel_data")
    conn = sqlite3.connect("D:\All Laptop Data\CyberTrone\Resources\Database_file\Cybertrone.db")
    cursor = conn.cursor()

    data = cursor.execute("""SELECT * FROM Unrecognize_persons""")
    for x in data.fetchall():
        print(x[1])
        with open("{}.png".format(counter), "wb") as f:
            f.write(x[1])
            counter = counter + 1

    conn.commit()
    cursor.close()
    conn.close()


def Save_recognized_data():
    obj = Image()
    os.chdir("D:\All Laptop Data\CyberTrone\Resources\Recognized_Personel")
    for x in obj.load_directory():
        if ".png" in x:
            with open(x,"rb") as f:
                data = f.read()
                obj.create_database(Name=x, Images=data)
                print("{} Added to database ".format(x))

        elif ".jpg" in x:
            with open(x,"rb") as f:
                data = f.read()
                obj.create_database(Name=x,Images=data)
                print("{} added to Database".format(x))


def fetch_recognized_data():
    counter = 1
    os.chdir("D:\All Laptop Data\CyberTrone\Resources\Recognized_personel_Records")
    conn = sqlite3.connect("D:\All Laptop Data\CyberTrone\Resources\Database_file\Cybertrone.db")
    cursor = conn.cursor()

    data = cursor.execute("""SELECT * FROM Recognize_persons""")
    for x in data.fetchall():
        print(x[1])
        with open("{}.png".format(counter), "wb") as f:
            f.write(x[1])
            counter = counter + 1

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    #Save_data()
    #fetch_data()
    #Save_recognized_data()
    #save_unrecognized_data()
    #save_unrecognized_data()
    #save_recognized_text()
    fetch_recognized_text()