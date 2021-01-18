from django.db import models
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse


class Food(models.Model):
    fdc_id = models.BigIntegerField(
        verbose_name='Идентификационный номер', primary_key=True)
    english_name = models.TextField(
        verbose_name='Имя на английском', blank=True, null=True)
    russian_name = models.TextField(
        verbose_name='Имя на русском', blank=True, null=True)
    protein = models.FloatField(
        verbose_name='Белки', db_column='1003', blank=True, null=True)
    fat = models.FloatField(verbose_name='Жиры',
                            db_column='1004', blank=True, null=True)
    carbohydrate = models.FloatField(
        verbose_name='Углеводы', db_column='1005', blank=True, null=True)
    energy = models.BigIntegerField(
        verbose_name='Энергетическая ценность', db_column='1008', blank=True, null=True)
    alcohol = models.FloatField(
        verbose_name='Этиловый спирт', db_column='1018', blank=True, null=True)
    water = models.FloatField(
        verbose_name='Вода', db_column='1051', blank=True, null=True)
    caffeine = models.BigIntegerField(
        verbose_name='Кофеин', db_column='1057', blank=True, null=True)
    theobromine = models.BigIntegerField(verbose_name='Теобромин',
                                         db_column='1058', blank=True, null=True)
    fiber = models.FloatField(
        verbose_name='Пищевые волокна', db_column='1079', blank=True, null=True)
    calcium = models.BigIntegerField(
        verbose_name='Кальций', db_column='1087', blank=True, null=True)
    iron = models.FloatField(verbose_name='Железо',
                             db_column='1089', blank=True, null=True)
    magnesium = models.BigIntegerField(
        verbose_name='Магний', db_column='1090', blank=True, null=True)
    phosphorus = models.BigIntegerField(verbose_name='Фосфор',
                                        db_column='1091', blank=True, null=True)
    potassium = models.BigIntegerField(
        verbose_name='Калий', db_column='1092', blank=True, null=True)
    sodium = models.BigIntegerField(
        verbose_name='Натрий', db_column='1093', blank=True, null=True)
    zinc = models.FloatField(
        verbose_name='Цинк', db_column='1095', blank=True, null=True)
    copper = models.FloatField(
        verbose_name='Медь', db_column='1098', blank=True, null=True)
    selenium = models.FloatField(
        verbose_name='Селен', db_column='1103', blank=True, null=True)
    retinol = models.BigIntegerField(
        verbose_name='Ретинол', db_column='1105', blank=True, null=True)
    rae = models.BigIntegerField(
        verbose_name='RAE (эквивалент активности ретинола)',
        db_column='1106', blank=True, null=True)
    carotene_beta = models.BigIntegerField(verbose_name='Бета-каротин',
                                           db_column='1107', blank=True, null=True)
    carotene_alpha = models.BigIntegerField(verbose_name='Альфа-каротин',
                                            db_column='1108', blank=True, null=True)
    alpha_tocopherol = models.FloatField(verbose_name='Витамин E',
                                         db_column='1109', blank=True, null=True)
    d2_d3 = models.FloatField(verbose_name='Витамин D',
                              db_column='1114', blank=True, null=True)
    cryptoxanthin_beta = models.BigIntegerField(verbose_name='Бета-криптоксантин',
                                                db_column='1120', blank=True, null=True)
    lycopene = models.BigIntegerField(
        verbose_name='Ликопен', db_column='1122', blank=True, null=True)
    lutein_zeaxanthin = models.BigIntegerField(verbose_name='Лютеин + зеаксантин',
                                               db_column='1123', blank=True, null=True)
    ascorbic_acid = models.FloatField(
        verbose_name='Витамин C', db_column='1162', blank=True, null=True)
    thiamin = models.FloatField(
        verbose_name='Тиамин', db_column='1165', blank=True, null=True)
    riboflavin = models.FloatField(
        verbose_name='Рибофлавин', db_column='1166', blank=True, null=True)
    niacin = models.FloatField(
        verbose_name='Ниацин', db_column='1167', blank=True, null=True)
    b6 = models.FloatField(verbose_name='Витамин B6',
                           db_column='1175', blank=True, null=True)
    folate = models.BigIntegerField(
        verbose_name='Фолаты, общие', db_column='1177', blank=True, null=True)
    b12 = models.FloatField(verbose_name='Витамин B12',
                            db_column='1178', blank=True, null=True)
    choline = models.FloatField(
        verbose_name='Холин', db_column='1180', blank=True, null=True)
    phylloquinone = models.FloatField(
        verbose_name='Филлохинон', db_column='1185', blank=True, null=True)
    folic_acid = models.BigIntegerField(verbose_name='Фолиевая кислота',
                                        db_column='1186', blank=True, null=True)
    food_folate = models.BigIntegerField(verbose_name='Фолаты в пище',
                                         db_column='1187', blank=True, null=True)
    dfe_folate = models.BigIntegerField(verbose_name='Пищевой фолатный эквивалент',
                                        db_column='1190', blank=True, null=True)
    added_e = models.FloatField(db_column='1242', blank=True, null=True)
    added_b12 = models.FloatField(db_column='1246', blank=True, null=True)
    cholesterol = models.BigIntegerField(verbose_name='Холестерин',
                                         db_column='1253', blank=True, null=True)
    saturated = models.FloatField(
        verbose_name='Насыщенные жирные кислоты', db_column='1258', blank=True, null=True)
    lipid_4_0 = models.FloatField(db_column='1259', blank=True, null=True)
    lipid_6_0 = models.FloatField(db_column='1260', blank=True, null=True)
    lipid_8_0 = models.FloatField(db_column='1261', blank=True, null=True)
    lipid_10_0 = models.FloatField(db_column='1262', blank=True, null=True)
    lipid_12_0 = models.FloatField(db_column='1263', blank=True, null=True)
    lipid_14_0 = models.FloatField(db_column='1264', blank=True, null=True)
    lipid_16_0 = models.FloatField(db_column='1265', blank=True, null=True)
    lipid_18_0 = models.FloatField(db_column='1266', blank=True, null=True)
    lipid_18_1 = models.FloatField(db_column='1268', blank=True, null=True)
    lipid_18_2 = models.FloatField(db_column='1269', blank=True, null=True)
    lipid_18_3 = models.FloatField(db_column='1270', blank=True, null=True)
    lipid_20_4 = models.FloatField(db_column='1271', blank=True, null=True)
    lipid_dha = models.FloatField(db_column='1272', blank=True, null=True)
    lipid_16_1 = models.FloatField(db_column='1275', blank=True, null=True)
    lipid_18_4 = models.FloatField(db_column='1276', blank=True, null=True)
    lipid_20_1 = models.FloatField(db_column='1277', blank=True, null=True)
    lipid_epa = models.FloatField(db_column='1278', blank=True, null=True)
    lipid_22_1 = models.FloatField(db_column='1279', blank=True, null=True)
    lipid_dpa = models.FloatField(db_column='1280', blank=True, null=True)
    monounsaturated = models.FloatField(verbose_name='Мононенасыщ. жирные кислоты',
                                        db_column='1292', blank=True, null=True)
    polyunsaturated = models.FloatField(verbose_name='Полиненасыщ. жирные кислоты',
                                        db_column='1293', blank=True, null=True)
    sugars = models.FloatField(
        verbose_name='Сахара, всего', db_column='2000', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food'

    def __str__(self):
        return self.russian_name

    def important_nutrients(self):
        units_of_important_nutrients = {'protein': 'г',
                                        'fat': 'г',
                                        'carbohydrate': 'г',
                                        'energy': 'ккал',
                                        'fiber': 'г',
                                        'iron': 'мг',
                                        'magnesium': 'мг',
                                        'phosphorus': 'мг',
                                        'potassium': 'мг',
                                        'sodium': 'мг',
                                        'zinc': 'мг',
                                        'copper': 'мг',
                                        'selenium': 'мкг',
                                        'rae': 'мкг',
                                        'alpha_tocopherol': 'мг',
                                        'd2_d3': 'мкг',
                                        'ascorbic_acid': 'мг',
                                        'thiamin': 'мг',
                                        'riboflavin': 'мг',
                                        'niacin': 'мг',
                                        'b6': 'мг',
                                        'b12': 'мкг',
                                        'cholesterol': 'мг',
                                        'saturated': 'г',
                                        'monounsaturated': 'г',
                                        'polyunsaturated': 'г',
                                        'sugars': 'г',
                                        'alcohol': 'г',
                                        'water': 'г', }
        for name, unit in units_of_important_nutrients.items():
            yield {'name': self._meta.get_field(name).verbose_name,
                   'amount': getattr(self, name),
                   'unit': unit}

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('food-detail', args=[str(self.fdc_id)])
