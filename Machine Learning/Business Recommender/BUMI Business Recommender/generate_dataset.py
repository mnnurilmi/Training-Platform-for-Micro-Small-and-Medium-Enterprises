from json.tool import main
from operator import index
import random
import pandas
import csv
from IPython.display import display

def generate_dummy():
    # Generate dummy data
    num_user_dummy = 50
    df_column = ["user_id","level","bidang_keahlian","hobi","modal_usaha"]
    df = pandas.DataFrame(columns=df_column)
    list_bidang_keahlian = ["kuliner","homecare","healtcare"]
    list_hobi = ["baca","olahraga","travelling","makan","membaca","nonton"]
    list_modal_usaha = ["under_50","between_50_and_100","above_100"]
    level = "" ##level itu yg "udah punya usaha" atau "belum punya usaha"
    for i in range(num_user_dummy):
        user_id = i

        jumlah_milih_maks_3 = random.randint(1,3)
        jumlah_milih_maks_5 = random.randint(1,5)
        bidang_keahlian = random.sample(list_bidang_keahlian, jumlah_milih_maks_3)
        hobi = random.sample(list_hobi, jumlah_milih_maks_5)
        modal_usaha = random.choice(list_modal_usaha)

        df.loc[i] = [user_id,level,bidang_keahlian,hobi,modal_usaha]
    
    df["level"].iloc[:40] = "udah_punya_usaha"
    df["level"].iloc[40:] = "belum_punya_usaha"


    df.to_csv("user_input.csv", index = False)
    print(df)

def main():
    generate_dummy()

if __name__ == "__main__":
    main()