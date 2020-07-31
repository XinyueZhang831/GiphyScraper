import os
import pandas as pd
import requests
import time


#def clean_df():
    #df = pd.read_csv('./giphy.csv',converters={'image_tag': eval})


    #for i,r in df.iterrows():
        #main_part = 'https://i.giphy.com/'
        #middle_part = ('/').join(r['image_url'].split('/')[4:5])
        #last = '.gif'
        #d_url = main_part+middle_part+last
        #df.at[i, 'dowload_url'] = d_url
        #add tag here
        #tag_list = ['animal', 'cartoon', 'bunny', 'dog', 'cat','anime', 'simpson','spongebob', 'simpsons']
        #print(i)
        #for eachtag in tag_list:
            #for each_tag in r['image_tag']:
                #if eachtag in each_tag:
                    #df.at[i,'download'] = 'No'
        #df.to_csv('download_prep.csv')


def download_gif():

    df = pd.read_csv('./giphy.csv')

    for i,r in df.iterrows():
        #if r['download'] != 'No':
        # windows dir format: 'D:\/your_folder1\/folder2'+'\/'+ str(r['Unnamed: 0']) + '.gif', 'wb'
        main_part = 'https://i.giphy.com/'
        middle_part = ('/').join(r['image_url'].split('/')[4:5])
        last = '.gif'
        link = main_part+middle_part+last
        with open(os.getcwd() + '/' + str(r['Unnamed: 0']) + '.gif', 'wb') as f:
            f.write(requests.get(link).content)
            print('finish:' + str(i))
        # time.sleep(20000)


download_gif()