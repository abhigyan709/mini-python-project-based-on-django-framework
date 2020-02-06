# Generated by Django 3.0 on 2020-02-06 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0036_auto_20200206_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictor',
            name='do_you_believe_in_social_justice',
            field=models.CharField(choices=[('yes', 'YES'), ('no', 'NO'), ('notMuch', 'NOT MUCH')], default='notMuch', help_text='Do you believe in Social Justice ?', max_length=25),
        ),
        migrations.AddField(
            model_name='predictor',
            name='do_you_enjoy_logical_thinking_and_reasoning',
            field=models.CharField(choices=[('yes', 'YES'), ('no', 'NO'), ('notMuch', 'NOT MUCH')], default='notMuch', help_text='Are you interested in Logical Thinking and Reasoning', max_length=25),
        ),
        migrations.AddField(
            model_name='predictor',
            name='do_you_feel_comfortable_interacting_with_crowd',
            field=models.CharField(choices=[('yes', 'YES'), ('no', 'NO'), ('notMuch', 'NOT MUCH')], default='notMuch', help_text='Do you feel comfortable interacting with crowd ?', max_length=25),
        ),
        migrations.AddField(
            model_name='predictor',
            name='do_you_have_any_medical_experiences',
            field=models.CharField(choices=[('yes', 'YES'), ('no', 'NO'), ('notMuch', 'NOT MUCH')], default='notMuch', help_text='Do you have any medical experiences ?', max_length=25),
        ),
        migrations.AddField(
            model_name='predictor',
            name='do_you_have_curiosity_about_human_body',
            field=models.CharField(choices=[('yes', 'YES'), ('no', 'NO'), ('notMuch', 'NOT MUCH')], default='notMuch', help_text='Do you have curiosity about human body ?', max_length=25),
        ),
        migrations.AddField(
            model_name='predictor',
            name='do_you_have_interest_in_financial_planning_and_control',
            field=models.CharField(choices=[('yes', 'YES'), ('no', 'NO'), ('notMuch', 'NOT MUCH')], default='notMuch', help_text='Do you have interest in financial planning and control ?', max_length=25),
        ),
        migrations.AddField(
            model_name='predictor',
            name='do_you_have_passion_about_creativity_and_innovations',
            field=models.CharField(choices=[('yes', 'YES'), ('no', 'NO'), ('notMuch', 'NOT MUCH')], default='notMuch', help_text='Do you take interest in Creativity and Innovations', max_length=25),
        ),
        migrations.AddField(
            model_name='predictor',
            name='do_you_love_serving_animals',
            field=models.CharField(choices=[('yes', 'YES'), ('no', 'NO'), ('notMuch', 'NOT MUCH')], default='notMuch', help_text='Do you love serving animals ?', max_length=25),
        ),
        migrations.AddField(
            model_name='predictor',
            name='do_you_take_interest_in_legal_matters',
            field=models.CharField(choices=[('yes', 'YES'), ('no', 'NO'), ('notMuch', 'NOT MUCH')], default='notMuch', help_text='Are you intersted in Legal Matters?', max_length=25),
        ),
        migrations.AddField(
            model_name='predictor',
            name='do_you_take_interest_to_solve_family_and_society_problem',
            field=models.CharField(choices=[('yes', 'YES'), ('no', 'NO'), ('notMuch', 'NOT MUCH')], default='notMuch', help_text='Do you take interest to solve family and society problem ?', max_length=25),
        ),
    ]
