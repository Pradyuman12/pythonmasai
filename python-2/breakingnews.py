import random

subjucts=[
  "shahrukh khan",
  "nirmala shitaramn",
  "virat kohali",
  "Mumbai a cat",
  "group of monkys",
  "prime ministar modi",
  "auto ricsha drive from dehli"
]

action=[
  "launches",
  "canceles",
  "dance with",
  "eits",
  "decaler war",
  "oders",
  "celebrates"
]

plece_this=[
  "red frde",
  "mubai local train",
  "a plete of samosha",
  "into parliament",
  "in ganga ghat",
  "during ipl match"
]

while True:
  redoms_subjective=random.choice(subjucts)
  redoms_actions=random.choice(action)
  redmos_place=random.choice(plece_this)

  handler=f"BREKING NEWS: {redoms_subjective} {redoms_actions} {redmos_place}"
  print("\n" + handler)

  users=input("\ndo you want more news?  (yes/no)").strip().lower()
  if users == "no":
    break
  
  
  print("\n thanks for use for fake news genrater")