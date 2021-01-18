# Generated by Django 3.1.3 on 2020-12-18 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0002_delete_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fdc_id', models.BigIntegerField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('protein', models.FloatField(blank=True, db_column='1003', null=True)),
                ('fat', models.FloatField(blank=True, db_column='1004', null=True)),
                ('carbohydrate', models.FloatField(blank=True, db_column='1005', null=True)),
                ('energy', models.BigIntegerField(blank=True, db_column='1008', null=True)),
                ('alcohol', models.FloatField(blank=True, db_column='1018', null=True)),
                ('water', models.FloatField(blank=True, db_column='1051', null=True)),
                ('caffeine', models.BigIntegerField(blank=True, db_column='1057', null=True)),
                ('theobromine', models.BigIntegerField(blank=True, db_column='1058', null=True)),
                ('fiber', models.FloatField(blank=True, db_column='1079', null=True)),
                ('calcium', models.BigIntegerField(blank=True, db_column='1087', null=True)),
                ('iron', models.FloatField(blank=True, db_column='1089', null=True)),
                ('magnesium', models.BigIntegerField(blank=True, db_column='1090', null=True)),
                ('phosphorus', models.BigIntegerField(blank=True, db_column='1091', null=True)),
                ('potassium', models.BigIntegerField(blank=True, db_column='1092', null=True)),
                ('sodium', models.BigIntegerField(blank=True, db_column='1093', null=True)),
                ('zinc', models.FloatField(blank=True, db_column='1095', null=True)),
                ('copper', models.FloatField(blank=True, db_column='1098', null=True)),
                ('selenium', models.FloatField(blank=True, db_column='1103', null=True)),
                ('retinol', models.BigIntegerField(blank=True, db_column='1105', null=True)),
                ('rae', models.BigIntegerField(blank=True, db_column='1106', null=True)),
                ('carotene_beta', models.BigIntegerField(blank=True, db_column='1107', null=True)),
                ('carotene_alpha', models.BigIntegerField(blank=True, db_column='1108', null=True)),
                ('alpha_tocopherol', models.FloatField(blank=True, db_column='1109', null=True)),
                ('d2_d3', models.FloatField(blank=True, db_column='1114', null=True)),
                ('cryptoxanthin_beta', models.BigIntegerField(blank=True, db_column='1120', null=True)),
                ('lycopene', models.BigIntegerField(blank=True, db_column='1122', null=True)),
                ('lutein_zeaxanthin', models.BigIntegerField(blank=True, db_column='1123', null=True)),
                ('ascorbic_acid', models.FloatField(blank=True, db_column='1162', null=True)),
                ('thiamin', models.FloatField(blank=True, db_column='1165', null=True)),
                ('riboflavin', models.FloatField(blank=True, db_column='1166', null=True)),
                ('niacin', models.FloatField(blank=True, db_column='1167', null=True)),
                ('b6', models.FloatField(blank=True, db_column='1175', null=True)),
                ('folate', models.BigIntegerField(blank=True, db_column='1177', null=True)),
                ('b12', models.FloatField(blank=True, db_column='1178', null=True)),
                ('choline', models.FloatField(blank=True, db_column='1180', null=True)),
                ('phylloquinone', models.FloatField(blank=True, db_column='1185', null=True)),
                ('folic_acid', models.BigIntegerField(blank=True, db_column='1186', null=True)),
                ('food_folate', models.BigIntegerField(blank=True, db_column='1187', null=True)),
                ('dfe_folate', models.BigIntegerField(blank=True, db_column='1190', null=True)),
                ('added_e', models.FloatField(blank=True, db_column='1242', null=True)),
                ('added_b12', models.FloatField(blank=True, db_column='1246', null=True)),
                ('cholesterol', models.BigIntegerField(blank=True, db_column='1253', null=True)),
                ('saturated', models.FloatField(blank=True, db_column='1258', null=True)),
                ('lipid_4_0', models.FloatField(blank=True, db_column='1259', null=True)),
                ('lipid_6_0', models.FloatField(blank=True, db_column='1260', null=True)),
                ('lipid_8_0', models.FloatField(blank=True, db_column='1261', null=True)),
                ('lipid_10_0', models.FloatField(blank=True, db_column='1262', null=True)),
                ('lipid_12_0', models.FloatField(blank=True, db_column='1263', null=True)),
                ('lipid_14_0', models.FloatField(blank=True, db_column='1264', null=True)),
                ('lipid_16_0', models.FloatField(blank=True, db_column='1265', null=True)),
                ('lipid_18_0', models.FloatField(blank=True, db_column='1266', null=True)),
                ('lipid_18_1', models.FloatField(blank=True, db_column='1268', null=True)),
                ('lipid_18_2', models.FloatField(blank=True, db_column='1269', null=True)),
                ('lipid_18_3', models.FloatField(blank=True, db_column='1270', null=True)),
                ('lipid_20_4', models.FloatField(blank=True, db_column='1271', null=True)),
                ('lipid_dha', models.FloatField(blank=True, db_column='1272', null=True)),
                ('lipid_16_1', models.FloatField(blank=True, db_column='1275', null=True)),
                ('lipid_18_4', models.FloatField(blank=True, db_column='1276', null=True)),
                ('lipid_20_1', models.FloatField(blank=True, db_column='1277', null=True)),
                ('lipid_epa', models.FloatField(blank=True, db_column='1278', null=True)),
                ('lipid_22_1', models.FloatField(blank=True, db_column='1279', null=True)),
                ('lipid_dpa', models.FloatField(blank=True, db_column='1280', null=True)),
                ('monounsaturated', models.FloatField(blank=True, db_column='1292', null=True)),
                ('polyunsaturated', models.FloatField(blank=True, db_column='1293', null=True)),
                ('sugars', models.FloatField(blank=True, db_column='2000', null=True)),
            ],
            options={
                'db_table': 'food',
                'managed': False,
            },
        ),
    ]