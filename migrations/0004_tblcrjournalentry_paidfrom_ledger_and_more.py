# Generated by Django 4.0.6 on 2023-09-13 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0003_alter_accountsubledger_ledger'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblcrjournalentry',
            name='paidfrom_ledger',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='credit_entries_paidfrom', to='accounting.accountledger'),
        ),
        migrations.AddField(
            model_name='tbldrjournalentry',
            name='paidfrom_ledger',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='debit_entries_paidfrom', to='accounting.accountledger'),
        ),
        migrations.AlterField(
            model_name='tblcrjournalentry',
            name='journal_entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.tbljournalentry'),
        ),
        migrations.AlterField(
            model_name='tblcrjournalentry',
            name='ledger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='credit_entries', to='accounting.accountledger'),
        ),
        migrations.AlterField(
            model_name='tbldrjournalentry',
            name='journal_entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.tbljournalentry'),
        ),
        migrations.AlterField(
            model_name='tbldrjournalentry',
            name='ledger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='debit_entries', to='accounting.accountledger'),
        ),
    ]