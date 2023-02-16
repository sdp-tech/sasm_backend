# Generated by Django 4.0 on 2023-02-16 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_merge_20230129_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcommentreport',
            name='category',
            field=models.CharField(choices=[('음란물/불건전한 만남 및 대화', '음란물/불건전한 만남 및 대화'), ('사칭/사기성 댓글', '사칭/사기성 댓글'), ('욕설/비하', '욕설/비하'), ('낚시/도배성 댓글', '낚시/도배성 댓글'), ('상업적 광고 및 판매', '상업적 광고 및 판매')], max_length=30),
        ),
    ]
