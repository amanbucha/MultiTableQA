tokens=['restriction', 'flight_stop', 'food_service', 'time_zone', 'code_description', 'city', 'flight_fare', 'state', 'fare_basis', 'date_day', 'time_interval', 'flight', 'dual_carrier', 'aircraft', 'fare', 'month', 'compartment_class', 'flight_leg', 'days', 'airport_service', 'airport', 'airline', 'equipment_sequence', 'ground_service', 'class_of_service']

def cnt_in_query(st):
    cnt=0
    sst=st.split()
    for token in tokens:
        if token in sst:
            cnt+=1
    return cnt

d=list()
for i in range(100):
    d.append(0)

def parse_sql_queries(input_file, output_file):
    with open(input_file, 'r') as f:
        queries = f.read().split('\n')

    indices=[]

    with open(output_file, 'w') as f:
        ind=0
        for query in queries:
            if query.strip():
                cnt = cnt_in_query(query)
                if cnt>1:
                    f.write(query.strip() + ';\n')
                    indices.append(ind)
                else: 
                    print(query)
                    print('\n')
                d[cnt]+=1
            ind+=1
        
    return indices

def add_lines_at_indices(old_path, file_path, indices):
    with open(old_path, 'r') as file:
        lines = file.readlines()

    modified_lines = [line for i, line in enumerate(lines) if i in indices]

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)



# indices=parse_sql_queries('test.sql', 'newtest.sql')
# add_lines_at_indices('test.nl', 'newtest.nl', indices)

def yo(st):
    oldname=st+".sql"
    newname="./newdata/"+oldname
    indices=parse_sql_queries(oldname, newname)
    oldname=st+".nl"
    newname="./newdata/"+oldname
    add_lines_at_indices(oldname, newname, indices)

yo('train_dev')
