# -*- coding: utf-8 -*-
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlocaleprofile',
            name='timezone',
            field=models.CharField(
                max_length=48, verbose_name='Timezone', choices=[
                    (b'Africa/Abidjan', b'Africa/Abidjan'),
                    (b'Africa/Accra', b'Africa/Accra'),
                    (b'Africa/Addis_Ababa', b'Africa/Addis_Ababa'),
                    (b'Africa/Algiers', b'Africa/Algiers'),
                    (b'Africa/Asmara', b'Africa/Asmara'),
                    (b'Africa/Bamako', b'Africa/Bamako'),
                    (b'Africa/Bangui', b'Africa/Bangui'),
                    (b'Africa/Banjul', b'Africa/Banjul'),
                    (b'Africa/Bissau', b'Africa/Bissau'),
                    (b'Africa/Blantyre', b'Africa/Blantyre'),
                    (b'Africa/Brazzaville', b'Africa/Brazzaville'),
                    (b'Africa/Bujumbura', b'Africa/Bujumbura'),
                    (b'Africa/Cairo', b'Africa/Cairo'),
                    (b'Africa/Casablanca', b'Africa/Casablanca'),
                    (b'Africa/Ceuta', b'Africa/Ceuta'),
                    (b'Africa/Conakry', b'Africa/Conakry'),
                    (b'Africa/Dakar', b'Africa/Dakar'),
                    (b'Africa/Dar_es_Salaam', b'Africa/Dar_es_Salaam'),
                    (b'Africa/Djibouti', b'Africa/Djibouti'),
                    (b'Africa/Douala', b'Africa/Douala'),
                    (b'Africa/El_Aaiun', b'Africa/El_Aaiun'),
                    (b'Africa/Freetown', b'Africa/Freetown'),
                    (b'Africa/Gaborone', b'Africa/Gaborone'),
                    (b'Africa/Harare', b'Africa/Harare'),
                    (b'Africa/Johannesburg', b'Africa/Johannesburg'),
                    (b'Africa/Juba', b'Africa/Juba'),
                    (b'Africa/Kampala', b'Africa/Kampala'),
                    (b'Africa/Khartoum', b'Africa/Khartoum'),
                    (b'Africa/Kigali', b'Africa/Kigali'),
                    (b'Africa/Kinshasa', b'Africa/Kinshasa'),
                    (b'Africa/Lagos', b'Africa/Lagos'),
                    (b'Africa/Libreville', b'Africa/Libreville'),
                    (b'Africa/Lome', b'Africa/Lome'),
                    (b'Africa/Luanda', b'Africa/Luanda'),
                    (b'Africa/Lubumbashi', b'Africa/Lubumbashi'),
                    (b'Africa/Lusaka', b'Africa/Lusaka'),
                    (b'Africa/Malabo', b'Africa/Malabo'),
                    (b'Africa/Maputo', b'Africa/Maputo'),
                    (b'Africa/Maseru', b'Africa/Maseru'),
                    (b'Africa/Mbabane', b'Africa/Mbabane'),
                    (b'Africa/Mogadishu', b'Africa/Mogadishu'),
                    (b'Africa/Monrovia', b'Africa/Monrovia'),
                    (b'Africa/Nairobi', b'Africa/Nairobi'),
                    (b'Africa/Ndjamena', b'Africa/Ndjamena'),
                    (b'Africa/Niamey', b'Africa/Niamey'),
                    (b'Africa/Nouakchott', b'Africa/Nouakchott'),
                    (b'Africa/Ouagadougou', b'Africa/Ouagadougou'),
                    (b'Africa/Porto-Novo', b'Africa/Porto-Novo'),
                    (b'Africa/Sao_Tome', b'Africa/Sao_Tome'),
                    (b'Africa/Tripoli', b'Africa/Tripoli'),
                    (b'Africa/Tunis', b'Africa/Tunis'),
                    (b'Africa/Windhoek', b'Africa/Windhoek'),
                    (b'America/Adak', b'America/Adak'),
                    (b'America/Anchorage', b'America/Anchorage'),
                    (b'America/Anguilla', b'America/Anguilla'),
                    (b'America/Antigua', b'America/Antigua'),
                    (b'America/Araguaina', b'America/Araguaina'),
                    (
                        b'America/Argentina/Buenos_Aires',
                        b'America/Argentina/Buenos_Aires'
                    ),
                    (
                        b'America/Argentina/Catamarca',
                        b'America/Argentina/Catamarca'
                    ),
                    (
                        b'America/Argentina/Cordoba',
                        b'America/Argentina/Cordoba'
                    ),
                    (b'America/Argentina/Jujuy', b'America/Argentina/Jujuy'),
                    (
                        b'America/Argentina/La_Rioja',
                        b'America/Argentina/La_Rioja'
                    ),
                    (
                        b'America/Argentina/Mendoza',
                        b'America/Argentina/Mendoza'
                    ),
                    (
                        b'America/Argentina/Rio_Gallegos',
                        b'America/Argentina/Rio_Gallegos'
                    ),
                    (b'America/Argentina/Salta', b'America/Argentina/Salta'),
                    (
                        b'America/Argentina/San_Juan',
                        b'America/Argentina/San_Juan'
                    ),
                    (
                        b'America/Argentina/San_Luis',
                        b'America/Argentina/San_Luis'
                    ),
                    (
                        b'America/Argentina/Tucuman',
                        b'America/Argentina/Tucuman'
                    ),
                    (
                        b'America/Argentina/Ushuaia',
                        b'America/Argentina/Ushuaia'
                    ),
                    (b'America/Aruba', b'America/Aruba'),
                    (b'America/Asuncion', b'America/Asuncion'),
                    (b'America/Atikokan', b'America/Atikokan'),
                    (b'America/Bahia', b'America/Bahia'),
                    (b'America/Bahia_Banderas', b'America/Bahia_Banderas'),
                    (b'America/Barbados', b'America/Barbados'),
                    (b'America/Belem', b'America/Belem'),
                    (b'America/Belize', b'America/Belize'),
                    (b'America/Blanc-Sablon', b'America/Blanc-Sablon'),
                    (b'America/Boa_Vista', b'America/Boa_Vista'),
                    (b'America/Bogota', b'America/Bogota'),
                    (b'America/Boise', b'America/Boise'),
                    (b'America/Cambridge_Bay', b'America/Cambridge_Bay'),
                    (b'America/Campo_Grande', b'America/Campo_Grande'),
                    (b'America/Cancun', b'America/Cancun'),
                    (b'America/Caracas', b'America/Caracas'),
                    (b'America/Cayenne', b'America/Cayenne'),
                    (b'America/Cayman', b'America/Cayman'),
                    (b'America/Chicago', b'America/Chicago'),
                    (b'America/Chihuahua', b'America/Chihuahua'),
                    (b'America/Costa_Rica', b'America/Costa_Rica'),
                    (b'America/Creston', b'America/Creston'),
                    (b'America/Cuiaba', b'America/Cuiaba'),
                    (b'America/Curacao', b'America/Curacao'),
                    (b'America/Danmarkshavn', b'America/Danmarkshavn'),
                    (b'America/Dawson', b'America/Dawson'),
                    (b'America/Dawson_Creek', b'America/Dawson_Creek'),
                    (b'America/Denver', b'America/Denver'),
                    (b'America/Detroit', b'America/Detroit'),
                    (b'America/Dominica', b'America/Dominica'),
                    (b'America/Edmonton', b'America/Edmonton'),
                    (b'America/Eirunepe', b'America/Eirunepe'),
                    (b'America/El_Salvador', b'America/El_Salvador'),
                    (b'America/Fortaleza', b'America/Fortaleza'),
                    (b'America/Glace_Bay', b'America/Glace_Bay'),
                    (b'America/Godthab', b'America/Godthab'),
                    (b'America/Goose_Bay', b'America/Goose_Bay'),
                    (b'America/Grand_Turk', b'America/Grand_Turk'),
                    (b'America/Grenada', b'America/Grenada'),
                    (b'America/Guadeloupe', b'America/Guadeloupe'),
                    (b'America/Guatemala', b'America/Guatemala'),
                    (b'America/Guayaquil', b'America/Guayaquil'),
                    (b'America/Guyana', b'America/Guyana'),
                    (b'America/Halifax', b'America/Halifax'),
                    (b'America/Havana', b'America/Havana'),
                    (b'America/Hermosillo', b'America/Hermosillo'),
                    (
                        b'America/Indiana/Indianapolis',
                        b'America/Indiana/Indianapolis'
                    ),
                    (b'America/Indiana/Knox', b'America/Indiana/Knox'),
                    (b'America/Indiana/Marengo', b'America/Indiana/Marengo'),
                    (
                        b'America/Indiana/Petersburg',
                        b'America/Indiana/Petersburg'
                    ),
                    (
                        b'America/Indiana/Tell_City',
                        b'America/Indiana/Tell_City'
                    ),
                    (b'America/Indiana/Vevay', b'America/Indiana/Vevay'),
                    (
                        b'America/Indiana/Vincennes',
                        b'America/Indiana/Vincennes'
                    ),
                    (b'America/Indiana/Winamac', b'America/Indiana/Winamac'),
                    (b'America/Inuvik', b'America/Inuvik'),
                    (b'America/Iqaluit', b'America/Iqaluit'),
                    (b'America/Jamaica', b'America/Jamaica'),
                    (b'America/Juneau', b'America/Juneau'),
                    (
                        b'America/Kentucky/Louisville',
                        b'America/Kentucky/Louisville'
                    ),
                    (
                        b'America/Kentucky/Monticello',
                        b'America/Kentucky/Monticello'
                    ),
                    (b'America/Kralendijk', b'America/Kralendijk'),
                    (b'America/La_Paz', b'America/La_Paz'),
                    (b'America/Lima', b'America/Lima'),
                    (b'America/Los_Angeles', b'America/Los_Angeles'),
                    (b'America/Lower_Princes', b'America/Lower_Princes'),
                    (b'America/Maceio', b'America/Maceio'),
                    (b'America/Managua', b'America/Managua'),
                    (b'America/Manaus', b'America/Manaus'),
                    (b'America/Marigot', b'America/Marigot'),
                    (b'America/Martinique', b'America/Martinique'),
                    (b'America/Matamoros', b'America/Matamoros'),
                    (b'America/Mazatlan', b'America/Mazatlan'),
                    (b'America/Menominee', b'America/Menominee'),
                    (b'America/Merida', b'America/Merida'),
                    (b'America/Metlakatla', b'America/Metlakatla'),
                    (b'America/Mexico_City', b'America/Mexico_City'),
                    (b'America/Miquelon', b'America/Miquelon'),
                    (b'America/Moncton', b'America/Moncton'),
                    (b'America/Monterrey', b'America/Monterrey'),
                    (b'America/Montevideo', b'America/Montevideo'),
                    (b'America/Montserrat', b'America/Montserrat'),
                    (b'America/Nassau', b'America/Nassau'),
                    (b'America/New_York', b'America/New_York'),
                    (b'America/Nipigon', b'America/Nipigon'),
                    (b'America/Nome', b'America/Nome'),
                    (b'America/Noronha', b'America/Noronha'),
                    (
                        b'America/North_Dakota/Beulah',
                        b'America/North_Dakota/Beulah'
                    ),
                    (
                        b'America/North_Dakota/Center',
                        b'America/North_Dakota/Center'
                    ),
                    (
                        b'America/North_Dakota/New_Salem',
                        b'America/North_Dakota/New_Salem'
                    ),
                    (b'America/Ojinaga', b'America/Ojinaga'),
                    (b'America/Panama', b'America/Panama'),
                    (b'America/Pangnirtung', b'America/Pangnirtung'),
                    (b'America/Paramaribo', b'America/Paramaribo'),
                    (b'America/Phoenix', b'America/Phoenix'),
                    (b'America/Port-au-Prince', b'America/Port-au-Prince'),
                    (b'America/Port_of_Spain', b'America/Port_of_Spain'),
                    (b'America/Porto_Velho', b'America/Porto_Velho'),
                    (b'America/Puerto_Rico', b'America/Puerto_Rico'),
                    (b'America/Rainy_River', b'America/Rainy_River'),
                    (b'America/Rankin_Inlet', b'America/Rankin_Inlet'),
                    (b'America/Recife', b'America/Recife'),
                    (b'America/Regina', b'America/Regina'),
                    (b'America/Resolute', b'America/Resolute'),
                    (b'America/Rio_Branco', b'America/Rio_Branco'),
                    (b'America/Santa_Isabel', b'America/Santa_Isabel'),
                    (b'America/Santarem', b'America/Santarem'),
                    (b'America/Santiago', b'America/Santiago'),
                    (b'America/Santo_Domingo', b'America/Santo_Domingo'),
                    (b'America/Sao_Paulo', b'America/Sao_Paulo'),
                    (b'America/Scoresbysund', b'America/Scoresbysund'),
                    (b'America/Sitka', b'America/Sitka'),
                    (b'America/St_Barthelemy', b'America/St_Barthelemy'),
                    (b'America/St_Johns', b'America/St_Johns'),
                    (b'America/St_Kitts', b'America/St_Kitts'),
                    (b'America/St_Lucia', b'America/St_Lucia'),
                    (b'America/St_Thomas', b'America/St_Thomas'),
                    (b'America/St_Vincent', b'America/St_Vincent'),
                    (b'America/Swift_Current', b'America/Swift_Current'),
                    (b'America/Tegucigalpa', b'America/Tegucigalpa'),
                    (b'America/Thule', b'America/Thule'),
                    (b'America/Thunder_Bay', b'America/Thunder_Bay'),
                    (b'America/Tijuana', b'America/Tijuana'),
                    (b'America/Toronto', b'America/Toronto'),
                    (b'America/Tortola', b'America/Tortola'),
                    (b'America/Vancouver', b'America/Vancouver'),
                    (b'America/Whitehorse', b'America/Whitehorse'),
                    (b'America/Winnipeg', b'America/Winnipeg'),
                    (b'America/Yakutat', b'America/Yakutat'),
                    (b'America/Yellowknife', b'America/Yellowknife'),
                    (b'Antarctica/Casey', b'Antarctica/Casey'),
                    (b'Antarctica/Davis', b'Antarctica/Davis'),
                    (
                        b'Antarctica/DumontDUrville',
                        b'Antarctica/DumontDUrville'
                    ),
                    (b'Antarctica/Macquarie', b'Antarctica/Macquarie'),
                    (b'Antarctica/Mawson', b'Antarctica/Mawson'),
                    (b'Antarctica/McMurdo', b'Antarctica/McMurdo'),
                    (b'Antarctica/Palmer', b'Antarctica/Palmer'),
                    (b'Antarctica/Rothera', b'Antarctica/Rothera'),
                    (b'Antarctica/Syowa', b'Antarctica/Syowa'),
                    (b'Antarctica/Troll', b'Antarctica/Troll'),
                    (b'Antarctica/Vostok', b'Antarctica/Vostok'),
                    (b'Arctic/Longyearbyen', b'Arctic/Longyearbyen'),
                    (b'Asia/Aden', b'Asia/Aden'),
                    (b'Asia/Almaty', b'Asia/Almaty'),
                    (b'Asia/Amman', b'Asia/Amman'),
                    (b'Asia/Anadyr', b'Asia/Anadyr'),
                    (b'Asia/Aqtau', b'Asia/Aqtau'),
                    (b'Asia/Aqtobe', b'Asia/Aqtobe'),
                    (b'Asia/Ashgabat', b'Asia/Ashgabat'),
                    (b'Asia/Baghdad', b'Asia/Baghdad'),
                    (b'Asia/Bahrain', b'Asia/Bahrain'),
                    (b'Asia/Baku', b'Asia/Baku'),
                    (b'Asia/Bangkok', b'Asia/Bangkok'),
                    (b'Asia/Beirut', b'Asia/Beirut'),
                    (b'Asia/Bishkek', b'Asia/Bishkek'),
                    (b'Asia/Brunei', b'Asia/Brunei'),
                    (b'Asia/Chita', b'Asia/Chita'),
                    (b'Asia/Choibalsan', b'Asia/Choibalsan'),
                    (b'Asia/Colombo', b'Asia/Colombo'),
                    (b'Asia/Damascus', b'Asia/Damascus'),
                    (b'Asia/Dhaka', b'Asia/Dhaka'),
                    (b'Asia/Dili', b'Asia/Dili'),
                    (b'Asia/Dubai', b'Asia/Dubai'),
                    (b'Asia/Dushanbe', b'Asia/Dushanbe'),
                    (b'Asia/Gaza', b'Asia/Gaza'),
                    (b'Asia/Hebron', b'Asia/Hebron'),
                    (b'Asia/Ho_Chi_Minh', b'Asia/Ho_Chi_Minh'),
                    (b'Asia/Hong_Kong', b'Asia/Hong_Kong'),
                    (b'Asia/Hovd', b'Asia/Hovd'),
                    (b'Asia/Irkutsk', b'Asia/Irkutsk'),
                    (b'Asia/Jakarta', b'Asia/Jakarta'),
                    (b'Asia/Jayapura', b'Asia/Jayapura'),
                    (b'Asia/Jerusalem', b'Asia/Jerusalem'),
                    (b'Asia/Kabul', b'Asia/Kabul'),
                    (b'Asia/Kamchatka', b'Asia/Kamchatka'),
                    (b'Asia/Karachi', b'Asia/Karachi'),
                    (b'Asia/Kathmandu', b'Asia/Kathmandu'),
                    (b'Asia/Khandyga', b'Asia/Khandyga'),
                    (b'Asia/Kolkata', b'Asia/Kolkata'),
                    (b'Asia/Krasnoyarsk', b'Asia/Krasnoyarsk'),
                    (b'Asia/Kuala_Lumpur', b'Asia/Kuala_Lumpur'),
                    (b'Asia/Kuching', b'Asia/Kuching'),
                    (b'Asia/Kuwait', b'Asia/Kuwait'),
                    (b'Asia/Macau', b'Asia/Macau'),
                    (b'Asia/Magadan', b'Asia/Magadan'),
                    (b'Asia/Makassar', b'Asia/Makassar'),
                    (b'Asia/Manila', b'Asia/Manila'),
                    (b'Asia/Muscat', b'Asia/Muscat'),
                    (b'Asia/Nicosia', b'Asia/Nicosia'),
                    (b'Asia/Novokuznetsk', b'Asia/Novokuznetsk'),
                    (b'Asia/Novosibirsk', b'Asia/Novosibirsk'),
                    (b'Asia/Omsk', b'Asia/Omsk'),
                    (b'Asia/Oral', b'Asia/Oral'),
                    (b'Asia/Phnom_Penh', b'Asia/Phnom_Penh'),
                    (b'Asia/Pontianak', b'Asia/Pontianak'),
                    (b'Asia/Pyongyang', b'Asia/Pyongyang'),
                    (b'Asia/Qatar', b'Asia/Qatar'),
                    (b'Asia/Qyzylorda', b'Asia/Qyzylorda'),
                    (b'Asia/Rangoon', b'Asia/Rangoon'),
                    (b'Asia/Riyadh', b'Asia/Riyadh'),
                    (b'Asia/Sakhalin', b'Asia/Sakhalin'),
                    (b'Asia/Samarkand', b'Asia/Samarkand'),
                    (b'Asia/Seoul', b'Asia/Seoul'),
                    (b'Asia/Shanghai', b'Asia/Shanghai'),
                    (b'Asia/Singapore', b'Asia/Singapore'),
                    (b'Asia/Srednekolymsk', b'Asia/Srednekolymsk'),
                    (b'Asia/Taipei', b'Asia/Taipei'),
                    (b'Asia/Tashkent', b'Asia/Tashkent'),
                    (b'Asia/Tbilisi', b'Asia/Tbilisi'),
                    (b'Asia/Tehran', b'Asia/Tehran'),
                    (b'Asia/Thimphu', b'Asia/Thimphu'),
                    (b'Asia/Tokyo', b'Asia/Tokyo'),
                    (b'Asia/Ulaanbaatar', b'Asia/Ulaanbaatar'),
                    (b'Asia/Urumqi', b'Asia/Urumqi'),
                    (b'Asia/Ust-Nera', b'Asia/Ust-Nera'),
                    (b'Asia/Vientiane', b'Asia/Vientiane'),
                    (b'Asia/Vladivostok', b'Asia/Vladivostok'),
                    (b'Asia/Yakutsk', b'Asia/Yakutsk'),
                    (b'Asia/Yekaterinburg', b'Asia/Yekaterinburg'),
                    (b'Asia/Yerevan', b'Asia/Yerevan'),
                    (b'Atlantic/Azores', b'Atlantic/Azores'),
                    (b'Atlantic/Bermuda', b'Atlantic/Bermuda'),
                    (b'Atlantic/Canary', b'Atlantic/Canary'),
                    (b'Atlantic/Cape_Verde', b'Atlantic/Cape_Verde'),
                    (b'Atlantic/Faroe', b'Atlantic/Faroe'),
                    (b'Atlantic/Madeira', b'Atlantic/Madeira'),
                    (b'Atlantic/Reykjavik', b'Atlantic/Reykjavik'),
                    (b'Atlantic/South_Georgia', b'Atlantic/South_Georgia'),
                    (b'Atlantic/St_Helena', b'Atlantic/St_Helena'),
                    (b'Atlantic/Stanley', b'Atlantic/Stanley'),
                    (b'Australia/Adelaide', b'Australia/Adelaide'),
                    (b'Australia/Brisbane', b'Australia/Brisbane'),
                    (b'Australia/Broken_Hill', b'Australia/Broken_Hill'),
                    (b'Australia/Currie', b'Australia/Currie'),
                    (b'Australia/Darwin', b'Australia/Darwin'),
                    (b'Australia/Eucla', b'Australia/Eucla'),
                    (b'Australia/Hobart', b'Australia/Hobart'),
                    (b'Australia/Lindeman', b'Australia/Lindeman'),
                    (b'Australia/Lord_Howe', b'Australia/Lord_Howe'),
                    (b'Australia/Melbourne', b'Australia/Melbourne'),
                    (b'Australia/Perth', b'Australia/Perth'),
                    (b'Australia/Sydney', b'Australia/Sydney'),
                    (b'Canada/Atlantic', b'Canada/Atlantic'),
                    (b'Canada/Central', b'Canada/Central'),
                    (b'Canada/Eastern', b'Canada/Eastern'),
                    (b'Canada/Mountain', b'Canada/Mountain'),
                    (b'Canada/Newfoundland', b'Canada/Newfoundland'),
                    (b'Canada/Pacific', b'Canada/Pacific'),
                    (b'Europe/Amsterdam', b'Europe/Amsterdam'),
                    (b'Europe/Andorra', b'Europe/Andorra'),
                    (b'Europe/Athens', b'Europe/Athens'),
                    (b'Europe/Belgrade', b'Europe/Belgrade'),
                    (b'Europe/Berlin', b'Europe/Berlin'),
                    (b'Europe/Bratislava', b'Europe/Bratislava'),
                    (b'Europe/Brussels', b'Europe/Brussels'),
                    (b'Europe/Bucharest', b'Europe/Bucharest'),
                    (b'Europe/Budapest', b'Europe/Budapest'),
                    (b'Europe/Busingen', b'Europe/Busingen'),
                    (b'Europe/Chisinau', b'Europe/Chisinau'),
                    (b'Europe/Copenhagen', b'Europe/Copenhagen'),
                    (b'Europe/Dublin', b'Europe/Dublin'),
                    (b'Europe/Gibraltar', b'Europe/Gibraltar'),
                    (b'Europe/Guernsey', b'Europe/Guernsey'),
                    (b'Europe/Helsinki', b'Europe/Helsinki'),
                    (b'Europe/Isle_of_Man', b'Europe/Isle_of_Man'),
                    (b'Europe/Istanbul', b'Europe/Istanbul'),
                    (b'Europe/Jersey', b'Europe/Jersey'),
                    (b'Europe/Kaliningrad', b'Europe/Kaliningrad'),
                    (b'Europe/Kiev', b'Europe/Kiev'),
                    (b'Europe/Lisbon', b'Europe/Lisbon'),
                    (b'Europe/Ljubljana', b'Europe/Ljubljana'),
                    (b'Europe/London', b'Europe/London'),
                    (b'Europe/Luxembourg', b'Europe/Luxembourg'),
                    (b'Europe/Madrid', b'Europe/Madrid'),
                    (b'Europe/Malta', b'Europe/Malta'),
                    (b'Europe/Mariehamn', b'Europe/Mariehamn'),
                    (b'Europe/Minsk', b'Europe/Minsk'),
                    (b'Europe/Monaco', b'Europe/Monaco'),
                    (b'Europe/Moscow', b'Europe/Moscow'),
                    (b'Europe/Oslo', b'Europe/Oslo'),
                    (b'Europe/Paris', b'Europe/Paris'),
                    (b'Europe/Podgorica', b'Europe/Podgorica'),
                    (b'Europe/Prague', b'Europe/Prague'),
                    (b'Europe/Riga', b'Europe/Riga'),
                    (b'Europe/Rome', b'Europe/Rome'),
                    (b'Europe/Samara', b'Europe/Samara'),
                    (b'Europe/San_Marino', b'Europe/San_Marino'),
                    (b'Europe/Sarajevo', b'Europe/Sarajevo'),
                    (b'Europe/Simferopol', b'Europe/Simferopol'),
                    (b'Europe/Skopje', b'Europe/Skopje'),
                    (b'Europe/Sofia', b'Europe/Sofia'),
                    (b'Europe/Stockholm', b'Europe/Stockholm'),
                    (b'Europe/Tallinn', b'Europe/Tallinn'),
                    (b'Europe/Tirane', b'Europe/Tirane'),
                    (b'Europe/Uzhgorod', b'Europe/Uzhgorod'),
                    (b'Europe/Vaduz', b'Europe/Vaduz'),
                    (b'Europe/Vatican', b'Europe/Vatican'),
                    (b'Europe/Vienna', b'Europe/Vienna'),
                    (b'Europe/Vilnius', b'Europe/Vilnius'),
                    (b'Europe/Volgograd', b'Europe/Volgograd'),
                    (b'Europe/Warsaw', b'Europe/Warsaw'),
                    (b'Europe/Zagreb', b'Europe/Zagreb'),
                    (b'Europe/Zaporozhye', b'Europe/Zaporozhye'),
                    (b'Europe/Zurich', b'Europe/Zurich'),
                    (b'GMT', b'GMT'),
                    (b'Indian/Antananarivo', b'Indian/Antananarivo'),
                    (b'Indian/Chagos', b'Indian/Chagos'),
                    (b'Indian/Christmas', b'Indian/Christmas'),
                    (b'Indian/Cocos', b'Indian/Cocos'),
                    (b'Indian/Comoro', b'Indian/Comoro'),
                    (b'Indian/Kerguelen', b'Indian/Kerguelen'),
                    (b'Indian/Mahe', b'Indian/Mahe'),
                    (b'Indian/Maldives', b'Indian/Maldives'),
                    (b'Indian/Mauritius', b'Indian/Mauritius'),
                    (b'Indian/Mayotte', b'Indian/Mayotte'),
                    (b'Indian/Reunion', b'Indian/Reunion'),
                    (b'Pacific/Apia', b'Pacific/Apia'),
                    (b'Pacific/Auckland', b'Pacific/Auckland'),
                    (b'Pacific/Bougainville', b'Pacific/Bougainville'),
                    (b'Pacific/Chatham', b'Pacific/Chatham'),
                    (b'Pacific/Chuuk', b'Pacific/Chuuk'),
                    (b'Pacific/Easter', b'Pacific/Easter'),
                    (b'Pacific/Efate', b'Pacific/Efate'),
                    (b'Pacific/Enderbury', b'Pacific/Enderbury'),
                    (b'Pacific/Fakaofo', b'Pacific/Fakaofo'),
                    (b'Pacific/Fiji', b'Pacific/Fiji'),
                    (b'Pacific/Funafuti', b'Pacific/Funafuti'),
                    (b'Pacific/Galapagos', b'Pacific/Galapagos'),
                    (b'Pacific/Gambier', b'Pacific/Gambier'),
                    (b'Pacific/Guadalcanal', b'Pacific/Guadalcanal'),
                    (b'Pacific/Guam', b'Pacific/Guam'),
                    (b'Pacific/Honolulu', b'Pacific/Honolulu'),
                    (b'Pacific/Johnston', b'Pacific/Johnston'),
                    (b'Pacific/Kiritimati', b'Pacific/Kiritimati'),
                    (b'Pacific/Kosrae', b'Pacific/Kosrae'),
                    (b'Pacific/Kwajalein', b'Pacific/Kwajalein'),
                    (b'Pacific/Majuro', b'Pacific/Majuro'),
                    (b'Pacific/Marquesas', b'Pacific/Marquesas'),
                    (b'Pacific/Midway', b'Pacific/Midway'),
                    (b'Pacific/Nauru', b'Pacific/Nauru'),
                    (b'Pacific/Niue', b'Pacific/Niue'),
                    (b'Pacific/Norfolk', b'Pacific/Norfolk'),
                    (b'Pacific/Noumea', b'Pacific/Noumea'),
                    (b'Pacific/Pago_Pago', b'Pacific/Pago_Pago'),
                    (b'Pacific/Palau', b'Pacific/Palau'),
                    (b'Pacific/Pitcairn', b'Pacific/Pitcairn'),
                    (b'Pacific/Pohnpei', b'Pacific/Pohnpei'),
                    (b'Pacific/Port_Moresby', b'Pacific/Port_Moresby'),
                    (b'Pacific/Rarotonga', b'Pacific/Rarotonga'),
                    (b'Pacific/Saipan', b'Pacific/Saipan'),
                    (b'Pacific/Tahiti', b'Pacific/Tahiti'),
                    (b'Pacific/Tarawa', b'Pacific/Tarawa'),
                    (b'Pacific/Tongatapu', b'Pacific/Tongatapu'),
                    (b'Pacific/Wake', b'Pacific/Wake'),
                    (b'Pacific/Wallis', b'Pacific/Wallis'),
                    (b'US/Alaska', b'US/Alaska'),
                    (b'US/Arizona', b'US/Arizona'),
                    (b'US/Central', b'US/Central'),
                    (b'US/Eastern', b'US/Eastern'),
                    (b'US/Hawaii', b'US/Hawaii'),
                    (b'US/Mountain', b'US/Mountain'),
                    (b'US/Pacific', b'US/Pacific'),
                    (b'UTC', b'UTC')
                ]
            ),
            preserve_default=True,
        ),
    ]
