from json.tool import main
from operator import index
import random
import pandas
import csv
from IPython.display import display

def generate_dummy():
    # Generate dummy data
    num_user_dummy = 50
    df_column = ["user_id","status","bidang_keahlian","hobi","modal_usaha","nama_usaha"]
    df = pandas.DataFrame(columns=df_column)
    list_bidang_keahlian = ["kuliner","homecare","healtcare"]
    list_hobi = ["baca","olahraga","travelling","makan","membaca","nonton"]
    list_modal_usaha = ["under_50","between_50_and_100","above_100"]
    level = "" ##level itu yg "udah punya usaha" atau "belum punya usaha"
    count = 0
    for i in range(num_user_dummy):
        user_id = i

        if count < 40:
            status= "udah_punya_usaha"
            nama_usaha = "nama_usaha-"+str(user_id)
        else:
            status = "belum_punya_usaha"
            nama_usaha = ""
        jumlah_milih_maks_3 = random.randint(1,3)
        jumlah_milih_maks_5 = random.randint(1,5)
        bidang_keahlian = random.sample(list_bidang_keahlian, jumlah_milih_maks_3)
        hobi = random.sample(list_hobi, jumlah_milih_maks_5)
        modal_usaha = random.choice(list_modal_usaha)

        df.loc[i] = [user_id,status,bidang_keahlian,hobi,modal_usaha,nama_usaha]
        count += 1

    df.to_csv("user_input.csv", index = False)
    print(df)

def main():
    generate_dummy()

if __name__ == "__main__":
    main()