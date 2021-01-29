Сайт о содержании питательных веществ в еде (7083 продуктов питания). Данные о продуктах питания взяты из [Food and Nutrient Database for Dietary Studies 2017-2018](https://fdc.nal.usda.gov/download-datasets.html).

Для извлечения данных из csv-файлов и загрузки в базу данных создан Jupyter notebook в папке csv_data_processing.

Перед деплоем сайта нужно завершить подготовку по [списку](https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/). Информация о базе данных PostgresSQL и секретный ключ должны быть помещены в файл private_config_sample.py в папке food, после чего он должен быть переименован в private_config.py.

Статическую версию сайта можно посмотреть на [Vercel](https://nutrients.vercel.app).
