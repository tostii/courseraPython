text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(":")
text = text[pos+1:]
text = text.strip()
text = float(text)
print(text)