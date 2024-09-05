# Generated by Django 4.0.6 on 2023-05-30 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('sorting_order', models.IntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False)),
                ('fiscal_year', models.CharField(max_length=20, null=True)),
                ('agent_name', models.CharField(max_length=255, null=True)),
                ('terminal', models.CharField(default='1', max_length=10)),
                ('customer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('customer_address', models.CharField(blank=True, max_length=255, null=True)),
                ('customer_tax_number', models.CharField(blank=True, max_length=255, null=True)),
                ('transaction_date_time', models.DateTimeField(auto_now_add=True)),
                ('transaction_date', models.DateField(auto_now_add=True)),
                ('transaction_miti', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_total', models.FloatField(default=0.0)),
                ('discount_amount', models.FloatField(default=0.0)),
                ('taxable_amount', models.FloatField(default=0.0)),
                ('tax_amount', models.FloatField(default=0.0)),
                ('grand_total', models.FloatField(default=0.0)),
                ('service_charge', models.FloatField(default=0.0)),
                ('invoice_number', models.CharField(blank=True, max_length=255, null=True)),
                ('amount_in_words', models.TextField(blank=True, null=True)),
                ('payment_mode', models.CharField(blank=True, default='Cash', max_length=255, null=True)),
                ('print_count', models.PositiveIntegerField(default=1)),
                ('bill_count_number', models.PositiveIntegerField(blank=True, db_index=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BillItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('sorting_order', models.IntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False)),
                ('product_title', models.CharField(max_length=255, null=True, verbose_name='Product Title')),
                ('product_quantity', models.PositiveBigIntegerField(default=1)),
                ('rate', models.FloatField(default=0.0)),
                ('unit_title', models.CharField(max_length=50, null=True)),
                ('amount', models.FloatField(default=0.0)),
                ('is_taxable', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('sorting_order', models.IntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255, verbose_name='Payment Type Title')),
                ('description', models.TextField(null=True, verbose_name='Payment Type Description')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='payment-type/icons/')),
                ('slug', models.SlugField(unique=True, verbose_name='Payment Type Slug')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TablReturnEntry',
            fields=[
                ('idtblreturnEntry', models.AutoField(primary_key=True, serialize=False)),
                ('bill_date', models.CharField(max_length=20, null=True)),
                ('bill_no', models.CharField(max_length=20, null=True)),
                ('customer_name', models.CharField(max_length=200, null=True)),
                ('customer_pan', models.CharField(max_length=200, null=True)),
                ('amount', models.FloatField(default=0.0, null=True)),
                ('NoTaxSales', models.FloatField(default=0.0)),
                ('ZeroTaxSales', models.FloatField(default=0.0)),
                ('taxable_amount', models.FloatField(default=0.0, null=True)),
                ('tax_amount', models.FloatField(default=0.0, null=True)),
                ('miti', models.CharField(max_length=20, null=True)),
                ('ServicedItem', models.CharField(default='Goods', max_length=20)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('reason', models.TextField(blank=True, null=True)),
                ('exemptedSales', models.CharField(default='0', max_length=20)),
                ('export', models.CharField(default='0', max_length=20)),
                ('exportCountry', models.CharField(default='0', max_length=20)),
                ('exportNumber', models.CharField(default='0', max_length=20)),
                ('exportDate', models.CharField(default='0', max_length=20)),
                ('unit', models.CharField(default='-', max_length=20)),
            ],
            options={
                'db_table': 'tblreturnentry',
            },
        ),
        migrations.CreateModel(
            name='TblSalesEntry',
            fields=[
                ('tblSalesEntry', models.AutoField(primary_key=True, serialize=False)),
                ('bill_date', models.CharField(max_length=20, null=True)),
                ('bill_no', models.CharField(max_length=20, null=True)),
                ('customer_name', models.CharField(max_length=200, null=True)),
                ('customer_pan', models.CharField(max_length=200, null=True)),
                ('amount', models.FloatField(default=0.0, null=True)),
                ('NoTaxSales', models.FloatField(default=0.0)),
                ('ZeroTaxSales', models.FloatField(default=0.0)),
                ('taxable_amount', models.FloatField(default=0.0, null=True)),
                ('tax_amount', models.FloatField(default=0.0, null=True)),
                ('miti', models.CharField(max_length=20, null=True)),
                ('ServicedItem', models.CharField(default='Goods', max_length=20)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('exemptedSales', models.CharField(default='0', max_length=20)),
                ('export', models.CharField(default='0', max_length=20)),
                ('exportCountry', models.CharField(default='0', max_length=20)),
                ('exportNumber', models.CharField(default='0', max_length=20)),
                ('exportDate', models.CharField(default='0', max_length=20)),
                ('unit', models.CharField(default='-', max_length=20)),
            ],
            options={
                'db_table': 'tblSalesEntry',
            },
        ),
        migrations.CreateModel(
            name='TblTaxEntry',
            fields=[
                ('idtbltaxEntry', models.AutoField(primary_key=True, serialize=False)),
                ('fiscal_year', models.CharField(max_length=20)),
                ('bill_no', models.CharField(max_length=20, null=True)),
                ('customer_name', models.CharField(max_length=200, null=True)),
                ('customer_pan', models.CharField(max_length=200, null=True)),
                ('bill_date', models.DateField(null=True)),
                ('amount', models.FloatField(null=True)),
                ('discount', models.FloatField(null=True)),
                ('taxable_amount', models.FloatField(null=True)),
                ('tax_amount', models.FloatField(null=True)),
                ('is_printed', models.CharField(default='Yes', max_length=20)),
                ('is_active', models.CharField(default='Yes', max_length=20)),
                ('printed_time', models.CharField(max_length=20, null=True)),
                ('entered_by', models.CharField(max_length=20, null=True)),
                ('printed_by', models.CharField(max_length=20, null=True)),
                ('is_realtime', models.CharField(default='Yes', max_length=20)),
                ('sync_with_ird', models.CharField(default='Yes', max_length=20)),
                ('payment_method', models.CharField(default='Cash', max_length=20, null=True)),
                ('vat_refund_amount', models.FloatField(default=0.0)),
                ('transaction_id', models.CharField(max_length=20, null=True)),
                ('unit', models.CharField(default='-', max_length=20)),
            ],
            options={
                'db_table': 'tbltaxentry',
            },
        ),
    ]