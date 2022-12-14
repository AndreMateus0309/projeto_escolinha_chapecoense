# Generated by Django 4.0.2 on 2022-11-27 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=20)),
                ('posicao', models.CharField(max_length=10)),
                ('possuiProblemaSaude', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=2)),
                ('altura', models.IntegerField()),
                ('massa', models.IntegerField()),
                ('nome', models.CharField(max_length=20)),
                ('sobrenome', models.CharField(max_length=35)),
                ('dataNascimento', models.DateField()),
                ('qualProblema', models.CharField(max_length=50)),
                ('observacao', models.TextField(max_length=255)),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('textoPadrao', models.TextField()),
                ('telefone', models.CharField(max_length=15)),
                ('contato1', models.CharField(max_length=60)),
                ('contato2', models.CharField(max_length=60)),
                ('contato3', models.CharField(max_length=60)),
                ('logo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('serie', models.CharField(max_length=2)),
                ('turno', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('comoSoube', models.CharField(max_length=15)),
                ('formaPagamento', models.CharField(max_length=10)),
                ('aluno_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.aluno')),
                ('empresa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.empresa')),
                ('escola_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.escola')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('nome', models.CharField(max_length=50)),
                ('observacoes', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=20)),
                ('nome', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=15)),
                ('dataNascimento', models.DateField()),
                ('endereco', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=8)),
                ('numero', models.CharField(max_length=5)),
                ('bairro', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Valores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=15)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Financeiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoMovimento', models.CharField(max_length=1)),
                ('dataMovimento', models.DateTimeField()),
                ('valorPago', models.DecimalField(decimal_places=2, max_digits=7)),
                ('situacao', models.CharField(max_length=1)),
                ('ficha_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ficha')),
            ],
        ),
        migrations.AddField(
            model_name='ficha',
            name='professor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.professor'),
        ),
        migrations.AddField(
            model_name='ficha',
            name='responsavel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.responsavel'),
        ),
        migrations.AddField(
            model_name='ficha',
            name='valores_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.valores'),
        ),
        migrations.CreateModel(
            name='Chamada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('descricao', models.CharField(max_length=255)),
                ('ficha_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ficha')),
            ],
        ),
    ]
