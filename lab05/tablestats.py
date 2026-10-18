def read_rows(lines):
    head = None
    rows = []
    for line in lines:
        clean_line = line.strip()
        if not clean_line:
            continue
        fields = [field.strip() for field in clean_line.split(',')]
        if head is None:
            head = fields
            continue
        if len(fields) != len(head):
            continue
        row_dict = {}
        for i in range(len(head)):
            row_dict[head[i]] = fields[i]
        rows.append(row_dict)
    return rows

def count_types(rows):
    cnt_types = {}
    for row in rows:
        kind = row['тип']
        if kind not in cnt_types:
            cnt_types[kind] = 0
        cnt_types[kind] += 1
    return cnt_types

def total_minutes(rows, kind):
    total = 0.0
    for row in rows:
        if row["тип"] == kind:
            minute_str = row['минуты']
            minute_str = minute_str.replace(',', '.')
            try:
                total += float(minute_str)
            except ValueError:
                continue
    return round(total,1)








