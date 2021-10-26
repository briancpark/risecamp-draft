from google_drive_downloader import GoogleDriveDownloader as gdd

for year in range(1804, 2022):
    gdd.download_file_from_google_drive(file_id='1gHdXtzZKpiaUdSyMXyP-9q7x_GQF6Umi', dest_path='./data/' + str(year) + '.csv')
