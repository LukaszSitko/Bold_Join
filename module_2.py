import json

with open('data.txt') as x:
    data = json.load(x)

#Constant variables
zero = []
number_of_hits = []
crucial_values=['coordinates']
crucial_values_1=['collection_event']
new_list=[]
curated=[]
redflags=[]
key_list = ['processid', 'record_id', 'bin_uri', "collectors", 'country', 'lat', 'lon', 'taxonomy','read','markercode','institution_storing','run_date','collection_event']
results_id=[]



try:
    x = data['bold_records']
    x = x['records']
    results_id = []

    for keys in x:
        results_id.append(str(keys))
        number_of_hits.append(results_id)


        #Individual record extraction
    u=0
    while u < len(results_id):
        indiv = x[results_id[u]]

        #Testing if results pass required threshold - geographical coordinates and BIN information
        check_1=indiv
        taxonomy_check = indiv['taxonomy']
        if 'collection_event' in check_1.keys() and 'bin_uri' in indiv.keys() and indiv['bin_uri']!='':
            check = indiv['collection_event']

            if 'coordinates' in check.keys():
                hit='hit'
                curated.append(hit)
                def get_vals(indiv, key_list):
                    for i, j in indiv.items():
                        if i in key_list:
                            yield (i, j)
                        yield from [] if not isinstance(j, dict) else get_vals(j, key_list)

                res = dict(get_vals(indiv, key_list))
                res_copy = res.copy()
                zero.append(res_copy)
                u = u+1

            elif 'coordinates' not in check.keys():
                u=u+1
                print('RED FLAG: No Information about coordinates is available.')

        else:
            print('RED FLAG: No information about collection is available')
            u=u+1

except ValueError:
    print("No data available")
    print('      ')
    flag='x'
    redflags.append(flag)
    pass

if 'x' not in redflags:
        #Total number of all obtained results and results that meet our requirments
    print('Total number of results from BOLD:')
    print(len(number_of_hits))

    results = (len(curated))
    print('Total number of results that meet required thresholds:')
    print(results)
    print('            ')

    hits = range(0,results)
    hits_1 = range(1,results)


        #Checking for duplication and appending key information to the first duplicated hit
    for h in hits:
        for g in hits_1:
            if  zero[h]['bin_uri'] == zero[g]['bin_uri'] and zero[h]['taxonomy'] == zero[g]['taxonomy'] and zero[h]['lat'] == zero[g]['lat'] and zero[h]['lon'] == zero[g]['lon'] and h<g:
                zero[g]['record_id']='duplicate'
                zero[h]['processid'] = zero[h]['processid']+', '+ zero[g]['processid']
                if zero[g]['collectors'] not in zero[h]['collectors']:
                    zero[h]['collectors'] = zero[h]['collectors']+' | '+ zero[g]['collectors']
                if 'specimen_identifiers' in zero[g].keys() and 'specimen_identifiers' in zero[h].keys():
                    if zero[g]['specimen_identifiers']['institution_storing'] not in zero[g]['specimen_identifiers']['institution_storing']:
                        zero[h]['specimen_identifiers']['institution_storing'] = zero[h]['specimen_identifiers']['institution_storing'] + ' | ' + zero[g]['specimen_identifiers']['institution_storing']

    for h in hits:
        if zero[h]['record_id']!='duplicate':
            new_list.append(zero[h])

with open('data_1.txt', 'w') as outfile:
    json.dump(new_list, outfile)

print('Progress: Completed')
