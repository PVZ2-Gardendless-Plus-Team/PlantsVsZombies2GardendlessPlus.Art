import json
with open(r'E:\worktrees\witty-rocket\art\zombies_BasicZOMBIE\skeleton.json', 'r') as f:
    skeleton = json.load(f)

for arm in skeleton['armature']:
    name = arm['name']
    nested = arm.get('armature', [])
    print(f'{name} - {len(nested)} nested')
    for n in nested:
        nname = n.get('name', '?')
        print(f'  -> {nname}')

bz = [a for a in skeleton['armature'] if a['name'] == 'BasicZombie'][0]
nested = bz.get('armature', [])
if nested:
    names = [n.get('name', '?') for n in nested]
    print('BasicZombie nested armatures:', names)
else:
    print('BasicZombie has no nested armatures')
