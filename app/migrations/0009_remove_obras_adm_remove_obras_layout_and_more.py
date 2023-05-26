# Generated by Django 4.1.7 on 2023-05-25 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_delete_planta_remove_obras_planta_baixa_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obras',
            name='ADM',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='Layout',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='SPDA',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='SPT',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='TUE',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='TUG',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='agua_fria',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='agua_quente',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='alimentacao',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='argamassa',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='asfalto',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='biodigestores',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='caderno_tecnico',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='caixa_dagua',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='ceramica',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='checklist_visita_tecnica',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='chumbadores',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='complementos',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='compras',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='comunicacao_visual',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='construtora_cliente',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='construtora_fornecedores',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='construtora_terceiros',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='contencoes',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='contratacoes',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='corpo_de_prova',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='cortes',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='dados',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='drenagem',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='esgoto',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='execucao',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='fachada',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='ficha_verificacao',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='financeiro',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='financeiro1',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='fisico',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='fisico1',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='fisico_financeiro',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='fisico_financeiro1',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='fotos',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='gas',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='historico_compras',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='iluminacao',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='impermeabilizacao',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='implantacao',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='incendio',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='indicador_produtividade',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='informacoes_contato',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='infraestrutura',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='infraestrutura_eletrica',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='instrucao_tecnica',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='jardinagem',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='locacao_de_infraestrurura',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='logistica',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='memorial_calculo',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='memorial_descritivo',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='notificacao',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='paginacao_de_piso',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='pavimentacao',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='piscina',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='plano_acao_macro',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='plano_acao_micro',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='planta_de_cobertura',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='pluvial',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='pos_venda',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='pre_venda',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='previsao_tempo',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='quantitativos',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='ramais_agua_fria',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='ramais_ar_pressurizado',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='ramais_esgoto',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='reboco',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='reuso',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='romaneio',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='solicitacao_compras',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='status_compras',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='superestrutura',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='tabela_de_preco',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='termos_garantia',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='teste_continuidade',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='uso_terreno',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='videos',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='vizinhanca',
        ),
    ]
