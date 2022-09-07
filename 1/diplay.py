import json

html = ""
with open("./1/imgs/data.json", "r") as fin:
    raw = json.load(fin)[0]
    print(raw)
    for k, v in raw.items():
        v1 = "\\text{" + v[0][1].lower() + "}"
        v2 = "\\text{" + v[0][2].lower() + "}"
        html += (
            f"<blockquote>\n\t<span>\n\t\t<b>{k.replace('_', ' ').title()}:</b>\n\t\t<span>Reference:"
            f" {v[0][0]}, $\\vec v_{v1} = {v[1]},\\ \\vec v_{v2} ="
            f" {v[2]}$</span>\n\t</span>\n\t<img src='./imgs/{k}.jpg'></img>\n</blockquote>\n"
        )
        print(html)

with open("./1/display.html", "w") as fout:
    fout.write(html)
