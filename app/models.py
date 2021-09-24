# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
# import PIL


class Point(models.Model):
    point_string = models.CharField(max_length=50)


class Location(models.Model):
    # that's only what I want to save
    point               = models.OneToOneField(Point, related_name='location', primary_key=True, on_delete=models.CASCADE)
    place_id            = models.CharField(max_length=50)
    full_address        = models.CharField(max_length=150)
    street_address      = models.CharField(max_length=150)
    street_number       = models.CharField(max_length=8)
    street_name         = models.CharField(max_length=50)
    suburb              = models.CharField(max_length=50)
    state               = models.CharField(max_length=50)
    postcode            = models.CharField(max_length=4)
    council             = models.CharField(max_length=50)
    lat                 = models.CharField(max_length=20)
    lon                 = models.CharField(max_length=20)
    link_code           = models.CharField(max_length=10)
    qr_filepath         = models.CharField(max_length=100)
    qr_path             = models.CharField(max_length=100)
    qrcode              = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')


class Estimate(models.Model):
    location                               =   models.OneToOneField(Location, related_name='estimate', primary_key=True, on_delete=models.CASCADE)
    os_identifier                          =   models.CharField(max_length=200, blank=True)   
    os_is_residential                      =   models.CharField(max_length=200, blank=True)
    os_lead_source                         =   models.CharField(max_length=200, blank=True)
    os_notes                               =   models.CharField(max_length=200, blank=True)
    os_lat                                 =   models.CharField(max_length=200, blank=True)
    os_lon                                 =   models.CharField(max_length=200, blank=True)
    os_address                             =   models.CharField(max_length=200, blank=True)
    os_locality                            =   models.CharField(max_length=200, blank=True)
    os_state                               =   models.CharField(max_length=200, blank=True)
    os_country_iso2                        =   models.CharField(max_length=200, blank=True)
    os_zip                                 =   models.CharField(max_length=200, blank=True)
    os_number_of_phases                    =   models.CharField(max_length=200, blank=True)
    os_roof_type_id                        =   models.CharField(max_length=200, blank=True)
    os_assgined_role                       =   models.CharField(max_length=200, blank=True)
    os_access                              =   models.CharField(max_length=200, blank=True)
    os_number_of_storeys                   =   models.CharField(max_length=200, blank=True)
    os_events                              =   models.CharField(max_length=200, blank=True)
    os_org_id                              =   models.CharField(max_length=200, blank=True)
    os_actions                             =   models.CharField(max_length=200, blank=True)
    os_org                                 =   models.CharField(max_length=200, blank=True)
    os_parcel_identifier                   =   models.CharField(max_length=200, blank=True)
    os_assigned_role_data                  =   models.CharField(max_length=200, blank=True)
    os_payment_option_sold                 =   models.CharField(max_length=200, blank=True)
    os_assigned_role_email                 =   models.CharField(max_length=200, blank=True)
    os_priority                            =   models.CharField(max_length=200, blank=True)
    os_assigned_role_id                    =   models.CharField(max_length=200, blank=True)
    os_private_files_data                  =   models.CharField(max_length=200, blank=True)
    os_assigned_role_name                  =   models.CharField(max_length=200, blank=True)
    os_private_files                       =   models.CharField(max_length=200, blank=True)
    os_assigned_role_phone                 =   models.CharField(max_length=200, blank=True)
    os_proposal_message                    =   models.CharField(max_length=200, blank=True)
    os_assigned_role                       =   models.CharField(max_length=200, blank=True)
    os_proposal_content                    =   models.CharField(max_length=200, blank=True)
    os_assigned_role_accreditation         =   models.CharField(max_length=200, blank=True)
    os_contract_terms                      =   models.CharField(max_length=200, blank=True)
    os_assigned_installer_role_data        =   models.CharField(max_length=200, blank=True)
    os_proposal_template                   =   models.CharField(max_length=200, blank=True)
    os_assigned_installer_role             =   models.CharField(max_length=200, blank=True)
    os_roof_type                           =   models.CharField(max_length=200, blank=True)
    os_assigned_site_inspector_role_data   =   models.CharField(max_length=200, blank=True)
    os_serial_numbers_panels               =   models.CharField(max_length=200, blank=True)
    os_assigned_site_inspector_role        =   models.CharField(max_length=200, blank=True)
    os_serial_numbers_inverters            =   models.CharField(max_length=200, blank=True)
    os_available_customer_actions          =   models.CharField(max_length=200, blank=True)
    os_serial_numbers_batteries            =   models.CharField(max_length=200, blank=True)
    os_business_identifier                 =   models.CharField(max_length=200, blank=True)
    os_simulate_first_year_only            =   models.CharField(max_length=200, blank=True)
    os_business_name                       =   models.CharField(max_length=200, blank=True)
    os_site_notes                          =   models.CharField(max_length=200, blank=True)
    os_configuration_override              =   models.CharField(max_length=200, blank=True)
    os_sold_date                           =   models.CharField(max_length=200, blank=True)
    os_configuration                       =   models.CharField(max_length=200, blank=True)
    os_stage                               =   models.CharField(max_length=200, blank=True)
    os_costing_override                    =   models.CharField(max_length=200, blank=True)
    os_stars                               =   models.CharField(max_length=200, blank=True)
    os_costing                             =   models.CharField(max_length=200, blank=True)
    os_contacts_data                       =   models.CharField(max_length=200, blank=True)
    os_systems                             =   models.CharField(max_length=200, blank=True)
    os_contacts                            =   models.CharField(max_length=200, blank=True)
    os_system_sold                         =   models.CharField(max_length=200, blank=True)
    os_contract_date                       =   models.CharField(max_length=200, blank=True)
    os_system_installed                    =   models.CharField(max_length=200, blank=True)
    os_contract                            =   models.CharField(max_length=200, blank=True)
    os_tags_data                           =   models.CharField(max_length=200, blank=True)
    os_tags                                =   models.CharField(max_length=200, blank=True)
    os_country_name                        =   models.CharField(max_length=200, blank=True)
    os_testimonials_data                   =   models.CharField(max_length=200, blank=True)
    os_country                             =   models.CharField(max_length=200, blank=True)
    os_testimonials                        =   models.CharField(max_length=200, blank=True)
    os_county                              =   models.CharField(max_length=200, blank=True)
    os_timezone_offset                     =   models.CharField(max_length=200, blank=True)
    os_created_date                        =   models.CharField(max_length=200, blank=True)
    os_title                               =   models.CharField(max_length=200, blank=True)
    os_events_data                         =   models.CharField(max_length=200, blank=True)
    os_transactions_data                   =   models.CharField(max_length=200, blank=True)
    os_greenlancer_project_id              =   models.CharField(max_length=200, blank=True)
    os_url                                 =   models.CharField(max_length=200, blank=True)
    os_id                                  =   models.CharField(max_length=200, blank=True)
    os_usage_annual_or_guess               =   models.CharField(max_length=200, blank=True)
    os_usage                               =   models.CharField(max_length=200, blank=True)
    os_utility_tariff_current_custom       =   models.CharField(max_length=200, blank=True)
    os_is_pricing_locked                   =   models.CharField(max_length=200, blank=True)
    os_utility_tariff_current_data         =   models.CharField(max_length=200, blank=True)
    os_installation_date                   =   models.CharField(max_length=200, blank=True)
    os_utility_tariff_current              =   models.CharField(max_length=200, blank=True)
    os_language                            =   models.CharField(max_length=200, blank=True)
    os_utility_tariff_or_guess             =   models.CharField(max_length=200, blank=True)
    os_language_override                   =   models.CharField(max_length=200, blank=True)
    os_utility_tariff_proposed_custom      =   models.CharField(max_length=200, blank=True)
    os_last_calculation_error              =   models.CharField(max_length=200, blank=True)
    os_utility_tariff_proposed_data        =   models.CharField(max_length=200, blank=True)
    os_utility_tariff_proposed             =   models.CharField(max_length=200, blank=True)
    os_utility_tariff_proposed_or_guess    =   models.CharField(max_length=200, blank=True)
    os_valid_until_date                    =   models.CharField(max_length=200, blank=True)
    os_wind_region                         =   models.CharField(max_length=200, blank=True)
    os_meter_identifier                    =   models.CharField(max_length=200, blank=True)
    os_has_cellular_coverage               =   models.CharField(max_length=200, blank=True)
    os_modified_date                       =   models.CharField(max_length=200, blank=True)
    os_power_factor                        =   models.CharField(max_length=200, blank=True)
    os_natron                              =   models.CharField(max_length=200, blank=True)
    os_years_to_simulate                   =   models.CharField(max_length=200, blank=True)
    os_customer_proposal_data              =   models.CharField(max_length=200, blank=True)
    os_number_of_wires                     =   models.CharField(max_length=200, blank=True)


class Property(models.Model):
    MATERIAL_TYPE = (
        ('TIN', 'Tin'),
        ('TILE', 'Tile'),
        ('TERRACOTTA', 'Terracotta'),
    )

    HOUSE_AGE = (
        ('L1Y', '<1'),
        ('M1YL15', '1 - 15'),
        ('M15L30', '15 - 30'),
        ('M30', '30 +'),
    )

    verified = models.BooleanField()
    roof_material = models.CharField(max_length=10, choices=MATERIAL_TYPE, default='TILE')
    house_age = models.CharField(max_length=10, choices=HOUSE_AGE, default='M1YL15')
    internal_switchboard = models.BooleanField()
    switchboard_photo_afar = models.BinaryField()
    switchboard_photo_enclosure = models.BinaryField()
    switchboard_photo_upclose = models.BinaryField()

    class Meta:
        verbose_name_plural = "Property"

    def __str__(self):
        return "{} {}".format(self.roof_material, self.verified)


class Rebate(models.Model):
    stcs = models.IntegerField()
    sv_loan = models.IntegerField()
    loan_amount = models.IntegerField()
    loan_requested = models.BooleanField()
    loan_approved = models.BooleanField()
    sv_solar_homes = models.IntegerField()
    solar_homes_amount = models.IntegerField()
    solar_homes_requested = models.BooleanField()
    solar_homes_approved = models.BooleanField()
    sv_battery = models.IntegerField()
    battery_amount = models.IntegerField()
    battery_requested = models.BooleanField()
    battery_approved = models.BooleanField()
    rebate_total = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Rebate'


class Eligibility(models.Model):
    verified = models.BooleanField()
    has_solar = models.BooleanField()
    year_installed = models.IntegerField()
    previously_approved = models.BooleanField()
    combined_income_value = models.IntegerField()
    combined_income_approved = models.BooleanField()
    property_value = models.IntegerField()
    property_value_approved = models.BooleanField()
    is_eligible = models.BooleanField()

    class Meta:
        verbose_name_plural = "Eligibility"


class Consumption(models.Model):
    RETAILERS = (
        ('1st_energy', '1st Energy'),
        ('agl', 'AGL'),
        ('alinta_energy', 'Alinta Energy'),
        ('amber_electrica', 'Amber Electrica'),
        ('blue_NRG', 'Blue NRG'),
        ('covaU', 'CovaU'),
        ('diamond_energy', 'Diamond Energy'),
        ('discover_energy', 'Discover Energy'),
        ('dodo_power_and_gas', 'Dodo Power & Gas'),
        ('elysian_energy', 'Elysian Energy'),
        ('energy_locals', 'Energy Locals'),
        ('energyAustralia', 'EnergyAustralia'),
        ('loBird_energy', 'GloBird Energy'),
        ('kogan_energy', 'Kogan Energy'),
        ('lumo_energy', 'Lumo Energy'),
        ('momentum_energy', 'Momentum Energy'),
        ('next_business_energy', 'Next Business Energy'),
        ('origin_energy', 'Origin Energy'),
        ('OVO_energy', 'OVO Energy'),
        ('people_energy', 'People Energy'),
        ('powerclub', 'Powerclub'),
        ('powerdirect', 'Powerdirect'),
        ('powershop_australia', 'Powershop Australia'),
        ('QEnergy_limited', 'QEnergy Limited'),
        ('reAmped_energy', 'ReAmped Energy'),
        ('red_energy', 'Red Energy'),
        ('simply_energy', 'Simply Energy'),
        ('sumo', 'Sumo'),
        ('tango_energy', 'Tango Energy'),
    )

    PHASES = (
        ('ONE', '1'),
        ('THREE', '3'),
        ('OTHER', 'Other'),
    )

    verified = models.BooleanField()
    retailer = models.CharField(max_length=2, choices=RETAILERS, default='1st_energy')
    interval_data = models.BinaryField()
    manual_input = models.BooleanField()
    electricity_bill = models.BinaryField()
    nphases = models.CharField(max_length=10, choices=PHASES, default='ONE')
    daily_usage = models.FloatField()
    usage_estimated = models.BooleanField()
    nmi = models.IntegerField()
    meter_a = models.CharField(max_length=100)
    meter_b = models.CharField(max_length=100)
    meter_c = models.CharField(max_length=100)
    service_charge = models.FloatField()
    off_peak_price = models.FloatField()
    on_peak_price = models.FloatField()

    class Meta:
        verbose_name_plural = "Consumption"


"""
"""