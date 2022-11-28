# Documenting urdf2mjcf

## Changelog generation

### Requirements

```shell
pip install git-changelog
```

### Generating the changelog

```shell
cd path/to/urdf2mjcf
git-changelog -o CHANGELOG.md -s conventional -t path:docs/changelog_templates .
```
