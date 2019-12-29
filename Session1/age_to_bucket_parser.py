import json
import yaml

with open("hw.json") as file:
    parsed_json = json.load(file)
people = parsed_json['ppl_ages']
buckets = parsed_json['buckets']
age_limits = [0, max(people.values()) + 1]
buckets.extend(age_limits)
buckets.sort()

age_groups = []
for age in range(len(buckets) - 1):
    names = []
    for name in people:
        if people[name] >= buckets[age]:
            if people[name] < buckets[age + 1]:
                names.append(name)
    age_groups.append({str(buckets[age]) + "-" + str(buckets[age + 1]): names})
print(yaml.dump(age_groups, allow_unicode=True))


