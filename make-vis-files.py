import sys

infi = sys.argv[1]
outfi = "vis" + infi[:-4]

if infi[:2] == "tb" or infi[:2] == "ma":
	metadata = ""
	if infi[:2] == "tb":
		metadata = "tb-BAAI-bge-base-en-v1.5-titles.tsv"
	else:
		metadata = "many_titles.tsv"
	text = '''
{
  "embeddings": [
    {
      "tensorName": "My tensor",
      "tensorShape": [
        1000,
        50
      ],
      "tensorPath": "https://media.githubusercontent.com/media/generic-account/visualizations/main/''' + infi + '''",
      "metadataPath": "https://media.githubusercontent.com/media/generic-account/visualizations/main/''' + metadata + '''"
    }
  ]
}
'''
	with open(outfi,"w") as f:
		f.write(text+"\n")
else:
	print("sf data " + infi)
