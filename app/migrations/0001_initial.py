# Generated by Django 2.2.10 on 2021-09-23 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_string', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('point', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='location', serialize=False, to='app.Point')),
                ('place_id', models.CharField(max_length=50)),
                ('full_address', models.CharField(max_length=150)),
                ('street_address', models.CharField(max_length=150)),
                ('street_number', models.CharField(max_length=8)),
                ('street_name', models.CharField(max_length=50)),
                ('suburb', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('postcode', models.CharField(max_length=4)),
                ('council', models.CharField(max_length=50)),
                ('lat', models.CharField(max_length=20)),
                ('lon', models.CharField(max_length=20)),
                ('link_code', models.CharField(max_length=10)),
                ('qr_filepath', models.CharField(max_length=100)),
                ('qr_path', models.CharField(max_length=100)),
                ('qrcode', models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='estimate', serialize=False, to='app.Location')),
                ('os_identifier', models.CharField(blank=True, max_length=200)),
                ('os_is_residential', models.CharField(blank=True, max_length=200)),
                ('os_lead_source', models.CharField(blank=True, max_length=200)),
                ('os_notes', models.CharField(blank=True, max_length=200)),
                ('os_lat', models.CharField(blank=True, max_length=200)),
                ('os_lon', models.CharField(blank=True, max_length=200)),
                ('os_address', models.CharField(blank=True, max_length=200)),
                ('os_locality', models.CharField(blank=True, max_length=200)),
                ('os_state', models.CharField(blank=True, max_length=200)),
                ('os_country_iso2', models.CharField(blank=True, max_length=200)),
                ('os_zip', models.CharField(blank=True, max_length=200)),
                ('os_number_of_phases', models.CharField(blank=True, max_length=200)),
                ('os_roof_type_id', models.CharField(blank=True, max_length=200)),
                ('os_assgined_role', models.CharField(blank=True, max_length=200)),
                ('os_access', models.CharField(blank=True, max_length=200)),
                ('os_number_of_storeys', models.CharField(blank=True, max_length=200)),
                ('os_events', models.CharField(blank=True, max_length=200)),
                ('os_org_id', models.CharField(blank=True, max_length=200)),
                ('os_actions', models.CharField(blank=True, max_length=200)),
                ('os_org', models.CharField(blank=True, max_length=200)),
                ('os_parcel_identifier', models.CharField(blank=True, max_length=200)),
                ('os_assigned_role_data', models.CharField(blank=True, max_length=200)),
                ('os_payment_option_sold', models.CharField(blank=True, max_length=200)),
                ('os_assigned_role_email', models.CharField(blank=True, max_length=200)),
                ('os_priority', models.CharField(blank=True, max_length=200)),
                ('os_assigned_role_id', models.CharField(blank=True, max_length=200)),
                ('os_private_files_data', models.CharField(blank=True, max_length=200)),
                ('os_assigned_role_name', models.CharField(blank=True, max_length=200)),
                ('os_private_files', models.CharField(blank=True, max_length=200)),
                ('os_assigned_role_phone', models.CharField(blank=True, max_length=200)),
                ('os_proposal_message', models.CharField(blank=True, max_length=200)),
                ('os_assigned_role', models.CharField(blank=True, max_length=200)),
                ('os_proposal_content', models.CharField(blank=True, max_length=200)),
                ('os_assigned_role_accreditation', models.CharField(blank=True, max_length=200)),
                ('os_contract_terms', models.CharField(blank=True, max_length=200)),
                ('os_assigned_installer_role_data', models.CharField(blank=True, max_length=200)),
                ('os_proposal_template', models.CharField(blank=True, max_length=200)),
                ('os_assigned_installer_role', models.CharField(blank=True, max_length=200)),
                ('os_roof_type', models.CharField(blank=True, max_length=200)),
                ('os_assigned_site_inspector_role_data', models.CharField(blank=True, max_length=200)),
                ('os_serial_numbers_panels', models.CharField(blank=True, max_length=200)),
                ('os_assigned_site_inspector_role', models.CharField(blank=True, max_length=200)),
                ('os_serial_numbers_inverters', models.CharField(blank=True, max_length=200)),
                ('os_available_customer_actions', models.CharField(blank=True, max_length=200)),
                ('os_serial_numbers_batteries', models.CharField(blank=True, max_length=200)),
                ('os_business_identifier', models.CharField(blank=True, max_length=200)),
                ('os_simulate_first_year_only', models.CharField(blank=True, max_length=200)),
                ('os_business_name', models.CharField(blank=True, max_length=200)),
                ('os_site_notes', models.CharField(blank=True, max_length=200)),
                ('os_configuration_override', models.CharField(blank=True, max_length=200)),
                ('os_sold_date', models.CharField(blank=True, max_length=200)),
                ('os_configuration', models.CharField(blank=True, max_length=200)),
                ('os_stage', models.CharField(blank=True, max_length=200)),
                ('os_costing_override', models.CharField(blank=True, max_length=200)),
                ('os_stars', models.CharField(blank=True, max_length=200)),
                ('os_costing', models.CharField(blank=True, max_length=200)),
                ('os_contacts_data', models.CharField(blank=True, max_length=200)),
                ('os_systems', models.CharField(blank=True, max_length=200)),
                ('os_contacts', models.CharField(blank=True, max_length=200)),
                ('os_system_sold', models.CharField(blank=True, max_length=200)),
                ('os_contract_date', models.CharField(blank=True, max_length=200)),
                ('os_system_installed', models.CharField(blank=True, max_length=200)),
                ('os_contract', models.CharField(blank=True, max_length=200)),
                ('os_tags_data', models.CharField(blank=True, max_length=200)),
                ('os_tags', models.CharField(blank=True, max_length=200)),
                ('os_country_name', models.CharField(blank=True, max_length=200)),
                ('os_testimonials_data', models.CharField(blank=True, max_length=200)),
                ('os_country', models.CharField(blank=True, max_length=200)),
                ('os_testimonials', models.CharField(blank=True, max_length=200)),
                ('os_county', models.CharField(blank=True, max_length=200)),
                ('os_timezone_offset', models.CharField(blank=True, max_length=200)),
                ('os_created_date', models.CharField(blank=True, max_length=200)),
                ('os_title', models.CharField(blank=True, max_length=200)),
                ('os_events_data', models.CharField(blank=True, max_length=200)),
                ('os_transactions_data', models.CharField(blank=True, max_length=200)),
                ('os_greenlancer_project_id', models.CharField(blank=True, max_length=200)),
                ('os_url', models.CharField(blank=True, max_length=200)),
                ('os_id', models.CharField(blank=True, max_length=200)),
                ('os_usage_annual_or_guess', models.CharField(blank=True, max_length=200)),
                ('os_usage', models.CharField(blank=True, max_length=200)),
                ('os_utility_tariff_current_custom', models.CharField(blank=True, max_length=200)),
                ('os_is_pricing_locked', models.CharField(blank=True, max_length=200)),
                ('os_utility_tariff_current_data', models.CharField(blank=True, max_length=200)),
                ('os_installation_date', models.CharField(blank=True, max_length=200)),
                ('os_utility_tariff_current', models.CharField(blank=True, max_length=200)),
                ('os_language', models.CharField(blank=True, max_length=200)),
                ('os_utility_tariff_or_guess', models.CharField(blank=True, max_length=200)),
                ('os_language_override', models.CharField(blank=True, max_length=200)),
                ('os_utility_tariff_proposed_custom', models.CharField(blank=True, max_length=200)),
                ('os_last_calculation_error', models.CharField(blank=True, max_length=200)),
                ('os_utility_tariff_proposed_data', models.CharField(blank=True, max_length=200)),
                ('os_utility_tariff_proposed', models.CharField(blank=True, max_length=200)),
                ('os_utility_tariff_proposed_or_guess', models.CharField(blank=True, max_length=200)),
                ('os_valid_until_date', models.CharField(blank=True, max_length=200)),
                ('os_wind_region', models.CharField(blank=True, max_length=200)),
                ('os_meter_identifier', models.CharField(blank=True, max_length=200)),
                ('os_has_cellular_coverage', models.CharField(blank=True, max_length=200)),
                ('os_modified_date', models.CharField(blank=True, max_length=200)),
                ('os_power_factor', models.CharField(blank=True, max_length=200)),
                ('os_natron', models.CharField(blank=True, max_length=200)),
                ('os_years_to_simulate', models.CharField(blank=True, max_length=200)),
                ('os_customer_proposal_data', models.CharField(blank=True, max_length=200)),
                ('os_number_of_wires', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
