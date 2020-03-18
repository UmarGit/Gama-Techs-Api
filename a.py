import requests
import csv
import json

params = {
  "api_key": "tFO5MS3MqZZ2",
  "format": "csv"
}

data = requests.get('https://www.parsehub.com/api/v2/projects/tb8TVjOOkGtq/last_ready_run/data', params=params)      

array = [[ 'Afghanistan' , 'AF' ],
[ 'Albania' , 'AL' ],
[ 'Algeria' , 'DZ' ],
[ 'American Samoa' , 'AS' ],
[ 'Andorra' , 'AD' ],
[ 'Angola' , 'AO' ],
[ 'Anguilla' , 'AI' ],
[ 'Antarctica' , 'AQ' ],
[ 'Antigua and Barbuda' , 'AG' ],
[ 'Argentina' , 'AR' ],
[ 'Armenia' , 'AM' ],
[ 'Aruba' , 'AW' ],
[ 'Australia' , 'AU' ],
[ 'Austria' , 'AT' ],
[ 'Azerbaijan' , 'AZ' ],
[ 'Bahamas' , 'BS' ],
[ 'Bahrain' , 'BH' ],
[ 'Bangladesh' , 'BD' ],
[ 'Barbados' , 'BB' ],
[ 'Belarus' , 'BY' ],
[ 'Belgium' , 'BE' ],
[ 'Belize' , 'BZ' ],
[ 'Benin' , 'BJ' ],
[ 'Bermuda' , 'BM' ],
[ 'Bhutan' , 'BT' ],
[ 'Bolivia' , 'BO' ],
[ 'Bonaire Sint Eustatius and Saba' , 'BQ' ],
[ 'Bosnia and Herzegovina' , 'BA' ],
[ 'Botswana' , 'BW' ],
[ 'Bouvet Island' , 'BV' ],
[ 'Brazil' , 'BR' ],
[ 'British Indian Ocean Territory' , 'IO' ],
[ 'Brunei Darussalam' , 'BN' ],
[ 'Bulgaria' , 'BG' ],
[ 'Burkina Faso' , 'BF' ],
[ 'Burundi' , 'BI' ],
[ 'Cabo Verde' , 'CV' ],
[ 'Cambodia' , 'KH' ],
[ 'Cameroon' , 'CM' ],
[ 'Canada' , 'CA' ],
[ 'Cayman Islands' , 'KY' ],
[ 'Central African Republic' , 'CF' ],
[ 'Chad' , 'TD' ],
[ 'Chile' , 'CL' ],
[ 'China' , 'CN' ],
[ 'Christmas Island' , 'CX' ],
[ 'Cocos Islands' , 'CC' ],
[ 'Colombia' , 'CO' ],
[ 'Comoros' , 'KM' ],
[ 'Congo' , 'CD' ],
[ 'Congo' , 'CG' ],
[ 'Cook Islands' , 'CK' ],
[ 'Costa Rica' , 'CR' ],
[ 'Croatia' , 'HR' ],
[ 'Cuba' , 'CU' ],
[ 'Curacao' , 'CW' ],
[ 'Cyprus' , 'CY' ],
[ 'Czechia' , 'CZ' ],
[ 'Denmark' , 'DK' ],
[ 'Djibouti' , 'DJ' ],
[ 'Dominica' , 'DM' ],
[ 'Dominican Republic' , 'DO' ],
[ 'Ecuador' , 'EC' ],
[ 'Egypt' , 'EG' ],
[ 'El Salvador' , 'SV' ],
[ 'Equatorial Guinea' , 'GQ' ],
[ 'Eritrea' , 'ER' ],
[ 'Estonia' , 'EE' ],
[ 'Eswatini' , 'SZ' ],
[ 'Ethiopia' , 'ET' ],
[ 'Falkland Islands' , 'FK' ],
[ 'Faroe Islands' , 'FO' ],
[ 'Fiji' , 'FJ' ],
[ 'Finland' , 'FI' ],
[ 'France' , 'FR' ],
[ 'French Guiana' , 'GF' ],
[ 'French Polynesia' , 'PF' ],
[ 'French Southern Territories' , 'TF' ],
[ 'Gabon' , 'GA' ],
[ 'Gambia' , 'GM' ],
[ 'Georgia' , 'GE' ],
[ 'Germany' , 'DE' ],
[ 'Ghana' , 'GH' ],
[ 'Gibraltar' , 'GI' ],
[ 'Greece' , 'GR' ],
[ 'Greenland' , 'GL' ],
[ 'Grenada' , 'GD' ],
[ 'Guadeloupe' , 'GP' ],
[ 'Guam' , 'GU' ],
[ 'Guatemala' , 'GT' ],
[ 'Guernsey' , 'GG' ],
[ 'Guinea' , 'GN' ],
[ 'Guinea-Bissau' , 'GW' ],
[ 'Guyana' , 'GY' ],
[ 'Haiti' , 'HT' ],
[ 'Heard Island and McDonald Islands' , 'HM' ],
[ 'Holy See' , 'VA' ],
[ 'Honduras' , 'HN' ],
[ 'Hong Kong' , 'HK' ],
[ 'Hungary' , 'HU' ],
[ 'Iceland' , 'IS' ],
[ 'India' , 'IN' ],
[ 'Indonesia' , 'ID' ],
[ 'Iran' , 'IR' ],
[ 'Iraq' , 'IQ' ],
[ 'Ireland' , 'IE' ],
[ 'Isle of Man' , 'IM' ],
[ 'Israel' , 'IL' ],
[ 'Italy' , 'IT' ],
[ 'Jamaica' , 'JM' ],
[ 'Japan' , 'JP' ],
[ 'Jersey' , 'JE' ],
[ 'Jordan' , 'JO' ],
[ 'Kazakhstan' , 'KZ' ],
[ 'Kenya' , 'KE' ],
[ 'Kiribati' , 'KI' ],
[ 'Korea' , 'KP' ],
[ 'Korea' , 'KR' ],
[ 'Kuwait' , 'KW' ],
[ 'Kyrgyzstan' , 'KG' ],
[ 'Latvia' , 'LV' ],
[ 'Lebanon' , 'LB' ],
[ 'Lesotho' , 'LS' ],
[ 'Liberia' , 'LR' ],
[ 'Libya' , 'LY' ],
[ 'Liechtenstein' , 'LI' ],
[ 'Lithuania' , 'LT' ],
[ 'Luxembourg' , 'LU' ],
[ 'Macao' , 'MO' ],
[ 'Madagascar' , 'MG' ],
[ 'Malawi' , 'MW' ],
[ 'Malaysia' , 'MY' ],
[ 'Maldives' , 'MV' ],
[ 'Mali' , 'ML' ],
[ 'Malta' , 'MT' ],
[ 'Marshall Islands' , 'MH' ],
[ 'Martinique' , 'MQ' ],
[ 'Mauritania' , 'MR' ],
[ 'Mauritius' , 'MU' ],
[ 'Mayotte' , 'YT' ],
[ 'Mexico' , 'MX' ],
[ 'Micronesia' , 'FM' ],
[ 'Moldova' , 'MD' ],
[ 'Monaco' , 'MC' ],
[ 'Mongolia' , 'MN' ],
[ 'Montenegro' , 'ME' ],
[ 'Montserrat' , 'MS' ],
[ 'Morocco' , 'MA' ],
[ 'Mozambique' , 'MZ' ],
[ 'Myanmar' , 'MM' ],
[ 'Namibia' , 'NA' ],
[ 'Nauru' , 'NR' ],
[ 'Nepal' , 'NP' ],
[ 'Netherlands' , 'NL' ],
[ 'New Caledonia' , 'NC' ],
[ 'New Zealand' , 'NZ' ],
[ 'Nicaragua' , 'NI' ],
[ 'Niger' , 'NE' ],
[ 'Nigeria' , 'NG' ],
[ 'Niue' , 'NU' ],
[ 'Norfolk Island' , 'NF' ],
[ 'Northern Mariana Islands' , 'MP' ],
[ 'Norway' , 'NO' ],
[ 'Oman' , 'OM' ],
[ 'Pakistan' , 'PK' ],
[ 'Palau' , 'PW' ],
[ 'Palestine, State of' , 'PS' ],
[ 'Panama' , 'PA' ],
[ 'Papua New Guinea' , 'PG' ],
[ 'Paraguay' , 'PY' ],
[ 'Peru' , 'PE' ],
[ 'Philippines' , 'PH' ],
[ 'Pitcairn' , 'PN' ],
[ 'Poland' , 'PL' ],
[ 'Portugal' , 'PT' ],
[ 'Puerto Rico' , 'PR' ],
[ 'Qatar' , 'QA' ],
[ 'Republic of North Macedonia' , 'MK' ],
[ 'Romania' , 'RO' ],
[ 'Russian Federation' , 'RU' ],
[ 'Rwanda' , 'RW' ],
[ 'Reunion' , 'RE' ],
[ 'Saint Barthélemy' , 'BL' ],
[ 'Saint Helena, Ascension and Tristan da Cunha' , 'SH' ],
[ 'Saint Kitts and Nevis' , 'KN' ],
[ 'Saint Lucia' , 'LC' ],
[ 'Saint Martin (French part)' , 'MF' ],
[ 'Saint Pierre and Miquelon' , 'PM' ],
[ 'Saint Vincent and the Grenadines' , 'VC' ],
[ 'Samoa' , 'WS' ],
[ 'San Marino' , 'SM' ],
[ 'Sao Tome and Principe' , 'ST' ],
[ 'Saudi Arabia' , 'SA' ],
[ 'Senegal' , 'SN' ],
[ 'Serbia' , 'RS' ],
[ 'Seychelles' , 'SC' ],
[ 'Sierra Leone' , 'SL' ],
[ 'Singapore' , 'SG' ],
[ 'Sint Maarten (Dutch part)' , 'SX' ],
[ 'Slovakia' , 'SK' ],
[ 'Slovenia' , 'SI' ],
[ 'Solomon Islands' , 'SB' ],
[ 'Somalia' , 'SO' ],
[ 'South Africa' , 'ZA' ],
[ 'South Georgia and the South Sandwich Islands' , 'GS' ],
[ 'South Sudan' , 'SS' ],
[ 'Spain' , 'ES' ],
[ 'Sri Lanka' , 'LK' ],
[ 'Sudan' , 'SD' ],
[ 'Suriname' , 'SR' ],
[ 'Svalbard and Jan Mayen' , 'SJ' ],
[ 'Sweden' , 'SE' ],
[ 'Switzerland' , 'CH' ],
[ 'Syrian Arab Republic' , 'SY' ],
[ 'Taiwan' , 'TW' ],
[ 'Tajikistan' , 'TJ' ],
[ 'Tanzania, United Republic of' , 'TZ' ],
[ 'Thailand' , 'TH' ],
[ 'Timor-Leste' , 'TL' ],
[ 'Togo' , 'TG' ],
[ 'Tokelau' , 'TK' ],
[ 'Tonga' , 'TO' ],
[ 'Trinidad and Tobago' , 'TT' ],
[ 'Tunisia' , 'TN' ],
[ 'Turkey' , 'TR' ],
[ 'Turkmenistan' , 'TM' ],
[ 'Turks and Caicos Islands' , 'TC' ],
[ 'Tuvalu' , 'TV' ],
[ 'Uganda' , 'UG' ],
[ 'Ukraine' , 'UA' ],
[ 'United Arab Emirates' , 'AE' ],
[ 'United Kingdom of Great Britain and Northern Ireland' , 'GB' ],
[ 'United States Minor Outlying Islands' , 'UM' ],
[ 'United States of America' , 'US' ],
[ 'Uruguay' , 'UY' ],
[ 'Uzbekistan' , 'UZ' ],
[ 'Vanuatu' , 'VU' ],
[ 'Venezuela' , 'VE' ],
[ 'Viet Nam' , 'VN' ],
[ 'Virgin Islands' , 'VG' ],
[ 'Virgin Islands' , 'VI' ],
[ 'Wallis and Futuna' , 'WF' ],
[ 'Western Sahara' , 'EH' ],
[ 'Yemen' , 'YE' ],
[ 'Zambia' , 'ZM' ],
[ 'Zimbabwe' , 'ZW' ],
[ 'Åland Islands' , 'AX' ]]


y=data.text.split('\n')


country=[]

case=[]

wines = list(csv.reader(y, delimiter=';'))

for x in range(1,len(wines),1):
    x = wines[0:][x]
    result = ''.join([i for i in x[0] if not i.isdigit()])

    q = result.strip(',"')

    country.append(q)


    result2 = x[0].translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwzyzABCDEFGHIJKLMNOPQRSTUVWXYZ._-," '})

    q2 = result2.strip(',"')

    case.append(q2)



def api_gt():
    dictOfWords = {}
    for i in range(0,len(array),1):
        for j in range(0,len(country),1):
            if array[i][0] == country[j]:
                #print(array[i][1])
                #print(case[j])
                dictOfWords[array[i][1]] = case[j]
    y = json.dumps(dictOfWords)
    return y