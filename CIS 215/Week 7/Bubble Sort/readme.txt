# Week 7, Working with CSV files

The assignment for our week 7 project is to:

    - Using the files attached (UN.txt and UN_sub.txt)
    - create a dictionary of countries
    - sort that dictionary by country name
  
# Source Code  
  
The code I used in my program 

```python
import json
with open("UN.txt") as file:
    longDictionary = {}
    for line in file:
        temp = line.strip()
        temp = temp.split(",")
        temp[0] = str(temp[0]+', '+temp[1])
        temp[1] = (temp[3] + '\t\t' +temp[2])
        longDictionary.update({temp[0]:temp[1]})
file.close()

print("All Countries sorted by Name")
print()
print("Country, Continent\t\t\tPopulation\t(some number)")
print("======================================================================")

for key in sorted(longDictionary):
    print (key, "\t\t\t", longDictionary[key])

with open("UN_sub.txt") as file:
    shortDictionary = {}
    for line in file:
        temp = line.strip()
        temp = temp.split(",")
        temp[0] = str(temp[0]+', '+temp[1])
        temp[1] = (temp[3] + '\t\t' +temp[2])
        shortDictionary.update({temp[0]:temp[1]})
file.close()

print("All Countries sorted by Name (Short List")
print()
print("Country, Continent\t\t\tPopulation\t(some number)")
print("======================================================================")

for key in sorted(shortDictionary):
    print (key, "\t\t\t", shortDictionary[key])


newFile = open('Countries.bin', 'wb+')
newFile.write(json.dumps(longDictionary).encode('utf-8'))
newFile.write(json.dumps(shortDictionary).encode('utf-8'))
newFile.close()



```
# Output

```Output
All Countries sorted by Name

Country, Continent			Population	(some number)
======================================================================
Afghanistan, Asia 			 251772		31.8
Albania, Europe 			 11100		3.0
Algeria, Africa 			 919595		38.3
Andorra, Europe 			 181		.085
Angola, Africa 			 481354		19.1
Antigua and Barbuda, North America 			 108		.091
Argentina, South America 			 1068302		44.0
Armenia, Asia 			 11506		3.1
Australia, Australia/Oceania 			 2967909		22.5
Austria, Europe 			 32383		8.2
Azerbaijan, Asia 			 33436		9.7
Bahamas, North America 			 5358		.32
Bahrain, Asia 			 253		1.3
Bangladesh, Asia 			 55599		166.3
Barbados, North America 			 167		.29
Belarus, Europe 			 80155		9.6
Belgium, Europe 			 11787		10.4
Belize, North America 			 8867		.34
Benin, Africa 			 43484		10.2
Bhutan, Asia 			 14824		.73
Bolivia, South America 			 424163		10.6
Bosnia and Herzegovina, Europe 			 19767		3.9
Botswana, Africa 			 224606		2.2
Brazil, South America 			 3287597		202.7
Brunei Darussalam, Asia 			 2226		.42
Bulgaria, Europe 			 42823		6.9
Burkina Faso, Africa 			 105792		18.4
Burundi, Africa 			 10745		10.4
Cambodia, Asia 			 69898		15.5
Cameroon, Africa 			 183568		23.1
Canada, North America 			 3855000		34.8
Cape Verde, Africa 			 1557		.54
Central African Republic, Africa 			 240534		5.3
Chad, Africa 			 495753		11.4
Chile, South America 			 292183		17.4
China, Asia 			 3696100		1355.7
Colombia, South America 			 440839		46.2
Comoros, Africa 			 863		.77
Costa Rica, North America 			 19730		4.8
Cote D'Ivoire, Africa 			 124502		22.8
Croatia, Europe 			 21831		4.5
Cuba, North America 			 42803		11.0
Cyprus, Asia 			 3572		1.2
Czech Republic, Europe 			 30450		10.6
Democratic People's Republic of Korea, Asia 			 46528		24.9
Democratic Republic of the Congo, Africa 			 905355		77.4
Denmark, Europe 			 16640		5.6
Djibouti, Africa 			 8958		.81
Dominica, North America 			 290		.073
Dominican Republic, North America 			 18704		10.4
Ecuador, South America 			 98985		14.0
Egypt, Africa 			 387048		86.9
El Salvador, North America 			 8124		6.2
Equatorial Guinea, Africa 			 10828		.72
Eritrea, Africa 			 45405		6.3
Estonia, Europe 			 17413		1.3
Ethiopia, Africa 			 426371		96.6
Fiji, Australia/Oceania 			 7056		.90
Finland, Europe 			 130596		5.3
France, Europe 			 211209		66.3
Gabon, Africa 			 103347		1.7
Gambia, Africa 			 4007		1.9
Georgia, Asia 			 26916		4.9
Germany, Europe 			 137847		81.0
Ghana, Africa 			 92098		25.8
Greece, Europe 			 50944		11.8
Grenada, North America 			 132		.11
Guatemala, North America 			 42042		14.7
Guinea Bissau, Africa 			 13948		1.7
Guinea, Africa 			 94926		11.5
Guyana, South America 			 83000		.74
Haiti, North America 			 10714		10.2
Honduras, North America 			 43278		8.6
Hungary, Europe 			 35919		10.0
Iceland, Europe 			 39770		.32
India, Asia 			 1269210		1236.3
Indonesia, Asia 			 735355		253.6
Iran, Asia 			 636372		80.8
Iraq, Asia 			 169234		32.6
Ireland, Europe 			 31520		4.8
Israel, Asia 			 8019		7.8
Italy, Europe 			 116346		61.7
Jamaica, North America 			 4444		2.9
Japan, Asia 			 145883		127.1
Jordan, Asia 			 45495		7.9
Kazakhstan, Asia 			 1052085		18.0
Kenya, Africa 			 224080		45.0
Kiribati, Australia/Oceania 			 280		.10
Kuwait, Asia 			 6880		2.7
Kyrgyzstan, Asia 			 77181		5.6
Lao People's Democratic Republic, Asia 			 91429		6.8
Latvia, Europe 			 24938		2.2
Lebanon, Asia 			 4035		5.9
Lesotho, Africa 			 12727		1.9
Liberia, Africa 			 43000		4.1
Libyan Arab Jamahiriya, Africa 			 679359		6.2
Liechtenstein, Europe 			 62		.037
Lithuania, Europe 			 25173		3.5
Luxembourg, Europe 			 998		.52
Madagascar, Africa 			 226597		23.2
Malawi, Africa 			 45747		17.4
Malaysia, Asia 			 127355		30.1
Maldives, Asia 			 115		.39
Mali, Africa 			 478839		16.5
Malta, Europe 			 121		.41
Marshall Islands, Australia/Oceania 			 69		.071
Mauritania, Africa 			 397954		3.5
Mauritius, Africa 			 787		1.3
Mexico, North America 			 761606		120.3
Micronesia, Australia/Oceania 			 271		.11
Monaco, Europe 			 0.76		.031
Mongolia, Asia 			 603909		3.0
Montenegro, Europe 			 5019		.65
Morocco, Africa 			 172414		33.0
Mozambique, Africa 			 309496		24.7
Myanmar, Asia 			 261227		55.7
Namibia, Africa 			 318696		2.2
Nauru, Australia/Oceania 			 8		.0095
Nepal, Asia 			 56827		31.0
Netherlands, Europe 			 16033		16.59
New Zealand, Australia/Oceania 			 103738		4.4
Nicaragua, North America 			 50193		6.1
Niger, Africa 			 489678		17.5
Nigeria, Africa 			 356669		177.2
Norway, Europe 			 148746		5.1
Oman, Asia 			 119498		3.2
Pakistan, Asia 			 310403		196.2
Palau, Australia/Oceania 			 177		.021
Panama, North America 			 29157		3.6
Papua New Guinea, Australia/Oceania 			 178703		6.6
Paraguay, South America 			 157048		6.7
Peru, South America 			 496226		30.1
Philippines, Asia 			 115831		107.7
Poland, Europe 			 120726		38.3
Portugal, Europe 			 35645		10.9
Qatar, Asia 			 4416		2.1
Republic of Korea, Asia 			 38622		49.0
Republic of Moldova, Europe 			 13067		3.6
Republic of the Congo, Africa 			 132047		4.7
Romania, Europe 			 92043		21.7
Russian Federation, Europe 			 6592800		142.5
Rwanda, Africa 			 10169		12.3
Saint Kitts and Nevis, North America 			 101		.052
Saint Lucia, North America 			 239		.16
Saint Vincent and the Grenadines, North America 			 150		.10
Samoa, Australia/Oceania 			 1093		.20
San Marino, Europe 			 23.5		.033
Sao Tome and Principe, Africa 			 372		.19
Saudi Arabia, Asia 			 829996		27.3
Senegal, Africa 			 76000		13.6
Serbia, Europe 			 34116		7.2
Seychelles, Africa 			 174		.092
Sierra Leone, Africa 			 27699		5.7
Singapore, Asia 			 274.2		5.6
Slovakia, Europe 			 18932		5.4
Slovenia, Europe 			 7827		2.0
Solomon Islands, Australia/Oceania 			 43		.61
Somalia, Africa 			 246201		10.4
South Africa, Africa 			 471443		48.4
South Sudan, Africa 			 239285		11.6
Spain, Europe 			 195364		47.7
Sri Lanka, Asia 			 25332		22.9
Sudan, Africa 			 967495		35.5
Suriname, South America 			 63251		.57
Swaziland, Africa 			 6704		1.4
Sweden, Europe 			 173732		9.7
Switzerland, Europe 			 15940		8.1
Syrian Arab Republic, Asia 			 71479		18.0
Tajikistan, Asia 			 55251		8.1
Thailand, Asia 			 198115		67.7
The former Yugoslav Republic of Macedonia, Europe 			 205		2.1
Timor-Leste, Asia 			 5743		1.2
Togo, Africa 			 21925		7.4
Tonga, Australia/Oceania 			 289		.11
Trinidad and Tobago, North America 			 1978		1.2
Tunisia, Africa 			 63170		10.9
Turkey, Asia 			 302535		81.6
Turkmenistan, Asia 			 188456		5.1
Tuvalu, Australia/Oceania 			 10		.011
Uganda, Africa 			 91136		35.9
Ukraine, Europe 			 233090		44.3
United Arab Emirates, Asia 			 32278		5.6
United Kingdom, Europe 			 94526		66.7
United Republic of Tanzania, Africa 			 364898		50.0
United States, North America 			 3794066		318.9
Uruguay, South America 			 68037		3.3
Uzbekistan, Asia 			 172742		28.9
Vanuatu, Australia/Oceania 			 4706		.27
Venezuela, South America 			 353841		28.9
Vietnam, Asia 			 128527		93.4
Yemen, Asia 			 203849		26.1
Zambia, Africa 			 290587		14.7
Zimbabwe, Africa 			 150871		13.8
All Countries sorted by Name (Short List

Country, Continent			Population	(some number)
======================================================================
Afghanistan, Asia 			 251772		31.8
Albania, Europe 			 11100		3.0
Algeria, Africa 			 919595		38.3
Andorra, Europe 			 181		.085
Angola, Africa 			 481354		19.1
Antigua and Barbuda, North America 			 108		.091
Argentina, South America 			 1068302		44.0
Armenia, Asia 			 11506		3.1
Australia, Australia/Oceania 			 2967909		22.5
Austria, Europe 			 32383		8.2
Azerbaijan, Asia 			 33436		9.7
Bahamas, North America 			 5358		.32
Bahrain, Asia 			 253		1.3
Bangladesh, Asia 			 55599		166.3
Barbados, North America 			 167		.29
Belarus, Europe 			 80155		9.6
```
along with the file Countries.bin
