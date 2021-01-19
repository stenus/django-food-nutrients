Сайт о содержании питательных веществ в еде (7083 продуктов питания). Данные о продуктах питания взяты из [Food and Nutrient Database for Dietary Studies 2017-2018](https://fdc.nal.usda.gov/download-datasets.html).

Для извлечения данных из csv-файлов и загрузки в базу данных создан Jupyter notebook в папке csv_data_processing

Информация о конфигурации базы данных PostgresSQL должна быть помещена в файл private_config.py в папке food в следующем формате (заполните поля соответствующими значениями для вашей базы данных):
db = {
    'name': '',
    'username': '',
    'password': '',
    'host': '',
    'port': '',
}
