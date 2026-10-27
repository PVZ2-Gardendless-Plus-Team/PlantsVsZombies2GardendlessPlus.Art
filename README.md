# MacksPVZ2-Again — Art

The extracted artwork for [MacksPVZ2-Again](https://github.com/Mackery6969/MacksPVZ2-Again),
a moddable reimplementation of PvZ2 Gardendless in Godot. The main repository
mounts it as the `art` submodule, at `res://art`.

See [COPYRIGHT.md](COPYRIGHT.md) first: the art belongs to PopCap Games,
PopCap Games (Shanghai) and Electronic Arts. It is here for development
reference and is not licensed by this repository.

**This is an unofficial fan work**, not developed, authorised or endorsed by
PopCap Games or Electronic Arts.

`.gitattributes` puts the images through Git LFS.

## Regenerating

Everything here comes out of the PVZGE build through the main repository's
tools. From the main repository's root:

```sh
python3 tools/extract_prefabs.py <import dir> <res.config.json> art --native <native dir> \
    plants/PeashooterPLANT plants/SunflowerPLANT plants/WallnutPLANT \
    plants/PotatoMinePLANT zombies/BasicZOMBIE armors/BasicConeARMOR \
    armors/BasicBucketARMOR projectiles/Pea0PRJ lawns/ MowerPRJ
python3 tools/extract_rigs.py <import dir> <res.config.json> art --native <native dir> \
    SunAnimate SunSlot Shovel PlantFoodSlot SeedPacker:Card Particles \n    Pause WorldmapAnimate:WorldmapBG
```

The first pulls named prefabs - entities, every world's lawn (`lawns/`) and
every world's mower (`MowerPRJ`). The second pulls rigs by their DragonBones
name, for the art that lives in scenes and resource packs instead: the sun,
the sun counter, the shovel, the plant food slots, the seed packet art, the
planting dirt, the pause menu crest and the teal sky behind the world map and
the award screen. Run it with no names to list every rig in the build. Both merge
into the same `_index.json`, so either can be re-run on its own.

`res.config.json` is `assets/resources/config.json` from the build, and
`<import dir>` is `assets/resources/import/` and `<native dir>`
`assets/resources/native/` - from the web build, or a desktop build unpacked
with `tools/extract_desktop.py`. Without `--native <dir>`, extract_prefabs.py
pulls the images from the Docker image directly; extract_rigs.py needs it.

`fonts/` holds PVZGE's text face, copied as-is from the build's
`native/86/86615cb2-9939-4358-b8e2-ec2d020efeea/FBUSV8C5EI.ttf` (the font
its seed packet prices and HUD labels use; the main repository maps it as
`font:ui`). `HOUSEOFTERROR.ttf` is the red face of "PLANT!" and the zombie
warnings.

`ui/` holds the flat UI sprites - buttons, windows, counters, the settings
rows, the main menu backdrops - which are plain SpriteFrames rather than rigs.
From the main repository's root: `python3 tools/extract_ui.py <build resources dir> art`.
`ui/_index.json` gives each sprite's size and its nine-slice insets.

Then open the main project in Godot once so it writes the `.import` files for
any new images, bake the rig scenes, and commit them with the art:

```sh
godot --headless -s tools/bake_rigs.gd
```

## Layout

```
_index.json            what each prefab resolved to: skeleton, armature, atlas, texture
_textures/<uuid>.png   the atlas images, shared between entities
fonts/                 the game's fonts
ui/<name>.png          flat UI sprites; ui/_index.json has their nine-slice insets
<bundle>_<Name>/
  skeleton.json        DragonBones armatures, bones, slots, animations
  atlas.json           the regions, in the texture named by _index.json
  <Armature>.tscn      each armature as a Godot scene: slots, sprites and an
                       AnimationPlayer. What the game loads, and what to open
                       in the Godot editor to change an animation. Baked for
                       the bundles the game maps; the rest bake on demand.
```

One texture serves many entities: the basic zombie and both its armors all
read `ZombieAnimate_tex.png`, which is the point of the shared rigs.
