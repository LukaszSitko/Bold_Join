import json
from bs4 import BeautifulSoup
import sys
import requests
sys.setrecursionlimit(10**6)

with open('data_1.txt') as x:
    new_list = json.load(x)

cost_countries=['Albania','Austria','Belgium', 'Bosnia and Herzegovina', 'Bulgaria','Croatia','Cyprus','Czech Republic','Denmark','Estonia','Finland','France','Germany','Greece','Hungary','Iceland','Ireland','Italy','Latvia','Lithuania','Luxembourg','Malta','Moldova','Montenegro','Netherlands','Macedonia','Norway','Poland','Portugal','Romania','Serbia','Slovakia','Slovenia','Spain','Sweden','Switzerland','Turkey','United Kingdom','Israel','Algeria','Armenia','Azerbaijan','Belarus','Egypt','Georgia','Jordan','Kosovo','Lebanon','Libya','Morocco','Palestine','Russia','Syria','Tunisia','Ukraine']
output_list=[]
final=len(new_list)
hits=range(0,final)
hits_1=range(1,final)

for h in hits:
    for g in hits:
        taxonomy_h = new_list[h]['taxonomy']
        taxonomy_g = new_list[g]['taxonomy']

        if 'order' in new_list[g]['taxonomy'].keys() and 'order' not in new_list[h]['taxonomy'].keys():

            order_0_g = taxonomy_g['order']['taxon']
            order_g = order_0_g['name']
            order_id = order_0_g['taxID']

            if new_list[h]['bin_uri'] == new_list[g]['bin_uri'] and h != g:
                d = {'order':{'taxon':{'name':str(order_g),'taxID':str(order_id)}}}
                new_list[h]['taxonomy'].update(d)
        else:
            pass

        if 'family' in new_list[g]['taxonomy'].keys() and 'family' not in new_list[h]['taxonomy'].keys():

            family_0_g = taxonomy_g['family']['taxon']
            family_g = family_0_g['name']
            family_id = family_0_g['taxID']

            if new_list[h]['bin_uri'] == new_list[g]['bin_uri'] and h != g:
                d = {'family':{'taxon':{'name':str(family_g),'taxID':str(family_id)}}}
                new_list[h]['taxonomy'].update(d)
        else:
            pass

        if 'genus' in new_list[g]['taxonomy'].keys() and 'genus' not in new_list[h]['taxonomy'].keys():

            genus_0_g = taxonomy_g['genus']['taxon']
            genus_g = genus_0_g['name']
            genus_id = genus_0_g['taxID']

            if new_list[h]['bin_uri'] == new_list[g]['bin_uri'] and h != g:
                d = {'genus':{'taxon':{'name':str(genus_g),'taxID':str(genus_id)}}}
                new_list[h]['taxonomy'].update(d)
        else:
            pass

        if 'species' in new_list[g]['taxonomy'].keys() and 'species' not in new_list[h]['taxonomy'].keys():

            species_0_g = taxonomy_g['species']['taxon']
            species_g = species_0_g['name']
            species_id = species_0_g['taxID']

            if new_list[h]['bin_uri'] == new_list[g]['bin_uri'] and h != g:
                d = {'species':{'taxon':{'name':str(species_g),'taxID':str(species_id)}}}
                new_list[h]['taxonomy'].update(d)
        else:
            pass

#Incorrected names
family_list=[]
family_list_red_flag=[]
genus_list=[]
genus_list_red_flag=[]

j=0
while j < len(new_list):
    taxonomy = new_list[j]['taxonomy']

    if 'phylum' in taxonomy.keys():
        phylum_0 = taxonomy['phylum']['taxon']
        phylum = phylum_0['name']
        phylum_taxid_0 = taxonomy['phylum']['taxon']
        phylum_taxid=phylum_taxid_0['taxID']
    else:
        phylum = (' ')
        phylum_taxid = (' ')

    if 'class' in taxonomy.keys():
        tclass_0 = taxonomy['class']['taxon']
        tclass = tclass_0['name']
        tclass_taxid_0 = taxonomy['class']['taxon']
        tclass_taxid = tclass_taxid_0['taxID']
    else:
        tclass = (' ')
        tclass_taxid = (' ')

    if 'order' in taxonomy.keys():
        order_0 = taxonomy['order']['taxon']
        order = order_0['name']
        order_taxid_0 = taxonomy['order']['taxon']
        order_taxid = order_taxid_0['taxID']
    elif 'order' in new_list[j].keys():
        order = new_list[j]['order']
        order_taxid = new_list[j]['order_id']
    else:
        order = (' ')
        order_taxid = (' ')

    if 'family' in taxonomy.keys():
        family_0 = taxonomy['family']['taxon']
        family = family_0['name']
        family_taxid_0 = taxonomy['family']['taxon']
        family_taxid = family_taxid_0['taxID']
    elif 'family' in new_list[j].keys():
        family = new_list[j]['family']
        family_taxid = new_list[j]['family_id']
    else:
        family = (' ')
        family_taxid=(' ')

    if 'genus' in taxonomy.keys():
        genus_0 = taxonomy['genus']['taxon']
        genus = genus_0['name']
        genus_taxid_0 = taxonomy['genus']['taxon']
        genus_taxid = genus_taxid_0['taxID']
    elif 'genus' in new_list[j].keys():
        genus=new_list[j]['genus']
        genus_taxid = new_list[j]['genus_id']
    else:
        genus = (' ')
        genus_taxid = (' ')

    if 'species' in taxonomy.keys():
        species_0 = taxonomy['species']['taxon']
        species = species_0['name']
        species_taxid_0 = taxonomy['species']['taxon']
        species_taxid = species_taxid_0['taxID']
    elif 'species' in new_list[j].keys():
        species = new_list[j]['species']
        species_taxid = new_list[j]['species_id']
    else:
        species = (' ')
        species_taxid = (' ')

    if 'read' in new_list[j].keys():
        col_date = new_list[j]['read']
        zet = col_date[0]
        col_date=str(zet['run_date'])
        head, sep, tail = col_date.partition('T')
    else:
        zet=(' ')
        head=(' ')
        col_date=(' ')

    if family not in family_list_red_flag and family not in family_list:
        source = ('https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?name=', family)
        y = str(''.join(source))
        source = requests.get(str(y)).text
        soup = BeautifulSoup(source, "html.parser")
        soup = str(soup)
        if 'No result' in soup:
            family_list_red_flag.append(family)
            print('Found error in taxonomy: ', family)
            family=('To review:', family)
            new_list[j]['taxonomy']['family']['taxon']['name'] = 'To review: ' + new_list[j]['taxonomy']['family']['taxon']['name']
        else:
            family_list.append(family)
    elif family in family_list:
        family=family
    elif family in family_list_red_flag:
        family = ('To review:', family)
        new_list[j]['taxonomy']['family']['taxon']['name'] = 'To review: ' + new_list[j]['taxonomy']['family']['taxon']['name']
    else:
        pass

    if genus not in genus_list_red_flag and genus not in genus_list:
        source = ('https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?name=', genus)
        y = str(''.join(source))
        source = requests.get(str(y)).text
        soup = BeautifulSoup(source, "html.parser")
        soup = str(soup)
        if 'No result' in soup:
            genus_list_red_flag.append(genus)
            print('Found error in taxonomy: ',genus )
            genus=('To review', genus)
            new_list[j]['taxonomy']['genus']['taxon']['name'] = 'To review: ' + new_list[j]['taxonomy']['genus']['taxon']['name']
        else:
            genus_list.append(genus)
    elif genus in genus_list:
        genus=genus
    elif genus in genus_list_red_flag:
        genus = ('To review', family)
        new_list[j]['taxonomy']['genus']['taxon']['name'] = 'To review: ' + new_list[j]['taxonomy']['genus']['taxon'][
            'name']
    else:
        pass

    print('Progress: ', j,)
    #If family exist save to file

    if 'read' in new_list[j].keys():
        new_list[j]['read']=new_list[j]['read'][0]
        if 'markercode' in new_list[j]['read'].keys():
            #print(new_list[j]['read']['markercode'])
            markercode=new_list[j]['read']['markercode']
            markercode={'markercode':markercode}
            new_list[j].update(markercode)
            new_list[j].pop('read')
        else:
            new_list[j].pop('read')

    if 'specimen_identifiers' in new_list[j].keys():
        if 'institution_storing' in new_list[j]['specimen_identifiers'].keys():
            #print(new_list[j]['read']['markercode'])
            inst=new_list[j]['specimen_identifiers']['institution_storing']
            inst={'Institution storing':inst}
            new_list[j].update(inst)
            new_list[j].pop('specimen_identifiers')
        else:
            new_list[j].pop('specimen_identifiers')

    if family !=' ' and 'family' in taxonomy.keys() and new_list[j]['country'] in cost_countries:
        output_list.append(new_list[j])

        with open('Output.json', 'w') as f:
            json.dump(output_list, f)
            j=j+1
    else:
        j=j+1

print('Progress: Completed')




