
from string import Template

def get_spec_list():
    result = []
    with open("specs.txt", "r") as spec_file:
        for line in spec_file:
            result.append(line.strip())
    return result


colors = ["#9fc5e8", "#ea9999", "#ffe599", #guard, rene, warr
            "#fce5cd", "#b6d7a8", "#f4cccc", #engi, ranger, thief
            "#e06666", "#df8bf0", "#93c47d"] #ele, mes, necro
specs = get_spec_list()
t_main  = Template(".$spec {background: $color;}\n")
t_image = Template(".$spec > .spec-image {background-image: url('images/$spec.png');}\n")
s = t_main.safe_substitute(spec="fb", color="#9fc5e8")
s = t_image.safe_substitute(spec="fb", color="#9fc5e8")
# print(s)
with open("output.css", "w") as out_file:
    for i, spec in enumerate(specs):
        s1 =t_main.safe_substitute(spec=spec, color=colors[i // 4])
        s2 = t_image.safe_substitute(spec=spec)
        out_file.write(s1)
        out_file.write(s2)
